from match import match
from weather_api import *
from typing import List, Tuple, Callable, Any

def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt

pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what's the temperature in %"), temperature),
    (str.split("when was the weather last updated in %"), updated),
    (str.split("what's the current condition in %"), cond),
    (str.split("what's the condition in %"), cond),
    (str.split("what's the wind speed in %"), wind_speed),
    (str.split("what's the wind degree in %"), wind_deg),
    (str.split("what's the wind direction in %"), wind_dir),
    (str.split("what's the precipitation in %"), precip),
    (str.split("what's the feels like in %"), feels),
    (str.split("what's the visibility in %"), vis),
    (str.split("what's the uv in %"), uv),
    (str.split("what's the gust in %"), gust),
    (str.split("what's the air quality in %"), aqi),
    (str.split("give me all the data on %"), all),
    (str.split("bye"), bye_action),
]


def search_pa_list(src: List[str], srcs: str) -> List[str]:
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

    city_user = input("What's the city in that string? \n").lower()
    stri = ""
    skip_amount = 0
    for i in range(len(srcs)):
        strb = srcs[i:i+len(city_user)].lower()
        if(strb == city_user):
            stri += "% "
            skip_amount = len(city_user)
            continue
        if skip_amount > 0:
            skip_amount -= 1
            continue
        stri += srcs[i]     
    add_pat = input(f"\nDo you want to add this pattern, --- {stri} --- \ny/n \n")
    if(add_pat == "y"):
        a = [temperature, updated, cond, wind_deg, wind_speed, wind_dir, precip, feels, vis, uv, gust, aqi, all]
        b = ["temperature", "last updated", "conditon", "wind degree", "wind speed", "wind direction", "precipitation", "feels like", "visibility", "uv", "gust", "air quality", "everything"]
        user_input = input(f"\nWhich function should this pattern point to, {b}: ")
        try:
            pa_list.append((str.split(stri), a[b.index(user_input)]))
            return [f"\n \nSuccessfully added pattern \033[31m{stri}\033[0m paired with function \033[31m{user_input}\033[0m \n \n"]
        except: 
            return("Not a valid function")
    return []

def run() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    print("Welcome to the weather machine!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower()
            answers = search_pa_list(query.split(), query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")