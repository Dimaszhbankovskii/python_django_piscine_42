class Intern:

    class Coffee:
        def __str__(self) -> str:
            return "This is the worst coffee you ever tasted."

    def __init__(self, name: str | None = None) -> None:
        self.name = name if name else "My name? I’m nobody, an intern, I have no name."

    def __str__(self) -> str:
        return self.name

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self) -> Coffee:
        return self.Coffee()


def test():
    intern = Intern()
    mark = Intern('Mark')
    print(intern)
    print(mark)

    try:
        intern.work()
    except Exception as exc:
        print(exc)

    print(mark.make_coffee())


if __name__ == '__main__':
    test()
