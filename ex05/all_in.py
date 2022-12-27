import sys


def get_key(dictionary: dict[str, str], elem: str) -> str:
    for key, value in dictionary.items():
        if value == elem:
            return key


def find_city(state: str, states: dict[str, str], capital_cities: dict[str, str]) -> bool:
    if state in states:
        city: str = capital_cities.get(states.get(state))
        print(f'{city} is the capital of {state}')
        return True
    return False


def find_state(city: str, states: dict[str, str], capital_cities: dict[str, str]) -> bool:
    if city in capital_cities.values():
        state: str = get_key(states, get_key(capital_cities, city))
        print(f'{city} is the capital of {state}')
        return True
    return False


def search_capital_or_state():
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
        expression: str = sys.argv[1]
        data: list[str] = expression.split(',')
        data: list[str] = [arg.strip().lower().title() for arg in data]
        for arg in data:
            if arg:
                flag: bool = False
                if not flag:
                    flag = find_city(arg, states, capital_cities)
                if not flag:
                    flag = find_state(arg, states, capital_cities)
                if not flag:
                    print(f'{arg} is neither a capital city nor a state')


if __name__ == '__main__':
    search_capital_or_state()
