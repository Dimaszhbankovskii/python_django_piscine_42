def my_var():
    var_int: int = 42
    var_str1: str = '42'
    var_str2: str = 'quarante-deux'
    var_float: float = 42.0
    var_bool: bool = True
    var_list: list = [42]
    var_dict: dict = {42: 42}
    var_tuple: tuple = (42,)
    var_set: set = set()

    print(f'{var_int} has a type {type(var_int)}')
    print(f'{var_str1} has a type {type(var_str1)}')
    print(f'{var_str2} has a type {type(var_str2)}')
    print(f'{var_float} has a type {type(var_float)}')
    print(f'{var_bool} has a type {type(var_bool)}')
    print(f'{var_list} has a type {type(var_list)}')
    print(f'{var_dict} has a type {type(var_dict)}')
    print(f'{var_tuple} has a type {type(var_tuple)}')
    print(f'{var_set} has a type {type(var_set)}')


if __name__ == '__main__':
    my_var()
