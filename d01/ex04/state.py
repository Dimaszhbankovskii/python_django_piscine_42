import sys


def get_key(dictionary: dict[str, str], elem: str) -> str:
    for key, value in dictionary.items():
        if value == elem:
            return key


def find_state():
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey" : "NJ",
        "Colorado" : "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    if len(sys.argv) == 2:
        city: str = sys.argv[1]
        if city in capital_cities.values():
            state: str = get_key(states, get_key(capital_cities, city))
            print(state)
        else:
            print('Unknown capital city')


if __name__ == '__main__':
    find_state()
