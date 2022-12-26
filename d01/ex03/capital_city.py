import sys


def find_city():
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    if len(sys.argv) == 2:
        state: str = sys.argv[1]
        if state in states:
            city: str = capital_cities.get(states.get(state))
            print(city)
        else:
            print('Unknown state')


if __name__ == '__main__':
    find_city()
