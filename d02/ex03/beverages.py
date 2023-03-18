class HotBeverages:

    def __init__(self) -> None:
        self.name = 'hot beverage'
        self.price = 0.30

    @staticmethod
    def description() -> str:
        return "Just some hot water in a cup."

    def __str__(self) -> str:
        template: str = (
            'name : "{name}"\n'
            'price : {price:0.2f}\n'
            'description : {description}'
        )
        return template.format(
            name=self.name,
            price=self.price,
            description=self.description()
        )


class Coffee(HotBeverages):

    def __init__(self) -> None:
        super().__init__()
        self.name = 'coffee'
        self.price = 0.40

    @staticmethod
    def description() -> str:
        return "A coffee, to stay awake."


class Tea(HotBeverages):

    def __init__(self) -> None:
        super().__init__()
        self.name = 'tea'


class Chocolate(HotBeverages):

    def __init__(self) -> None:
        super().__init__()
        self.name = 'chocolate'
        self.price = 0.50

    @staticmethod
    def description() -> str:
        return "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverages):

    def __init__(self) -> None:
        super().__init__()
        self.name = "cappuccino"
        self.price = 0.45

    @staticmethod
    def description() -> str:
        return "Un po’ di Italia nella sua tazza!"


def test_hot_beverage():
    print(HotBeverages())
    print(Coffee())
    print(Tea())
    print(Chocolate())
    print(Cappuccino())


if __name__ == '__main__':
    test_hot_beverage()
