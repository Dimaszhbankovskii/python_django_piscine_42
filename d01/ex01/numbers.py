def proccess_file(file: str):
    with open(file, 'r') as infile:
        data = infile.read()
        numbers: list = data.split(',')
        for num in numbers:
            print(num)


if __name__ == '__main__':
    proccess_file('numbers.txt')
