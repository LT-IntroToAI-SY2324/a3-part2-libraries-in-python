from match import match
from typing import List, Tuple, Callable, Any
from weather_api import *

def curr_temp(city: str):
    return weather(city)

pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what's the temperature in %"), temperature),    
]


def search_pa_list(src: List[str]) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """

    for i in range(len(pa_list)):
        if(match(pa_list[i][0], src) != None):
            if(pa_list[i][1](match(pa_list[i][0], src)) == []):
                return ["No answers"]
            else:
                return pa_list[i][1](match(pa_list[i][0], src))

    return ["I don't understand"]

def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    print("Welcome to the weather machine!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")

query_loop()