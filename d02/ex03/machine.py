import random
from beverages import HotBeverages, Coffee, Tea, Chocolate, Cappuccino


class CoffeeMachine:

    class EmptyCup(HotBeverages):
        def __init__(self) -> None:
            super().__init__()
            self.name = "empty cup"
            self.price = 0.90

        @staticmethod
        def description() -> str:
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self) -> None:
            super().__init__("This coffee machine has to be repaired.")

    def __init__(self):
        self.broken_count = 10

    def repair(self):
        self.broken_count = 10

    def serve(self, drink: HotBeverages) -> HotBeverages:
        if self.broken_count <= 0:
            raise self.BrokenMachineException
        self.broken_count -= 1
        if random.randint(0, 5) == 0:
            return self.EmptyCup()
        return drink()


def test_coffee_machine():
    coffee_machine = CoffeeMachine()
    for _ in range(22):
        try:
            print(
                coffee_machine.serve(
                    random.choice(
                        [Coffee, Tea, Chocolate, Cappuccino]
                    )
                )
            )
        except CoffeeMachine.BrokenMachineException as exc:
            print(exc)
            coffee_machine.repair()


if __name__ == '__main__':
    test_coffee_machine()
