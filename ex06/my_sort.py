def my_sort():
    d: dict[str, str] = {
        'Hendrix': '1942',
        'Allman': '1946',
        'King': '1925',
        'Clapton': '1945',
        'Johnson': '1911',
        'Berry': '1926',
        'Vaughan': '1954',
        'Cooder': '1947',
        'Page': '1944',
        'Richards': '1943',
        'Hammett': '1962',
        'Cobain': '1967',
        'Garcia': '1942',
        'Beck': '1944',
        'Santana': '1947',
        'Ramone': '1948',
        'White': '1975',
        'Frusciante': '1970',
        'Thompson': '1949',
        'Burton': '1939',
    }

    sorted_list_tuple_by_year: list[tuple[str, str]] = sorted(d.items(), key=lambda item: item[1])

    i: int = 0
    sorted_list_list_tuple_by_year: list[list[tuple[str, str]]] = []
    while i < len(sorted_list_tuple_by_year):
        tmp: list[tuple[str, str]] = [sorted_list_tuple_by_year[i]]
        while i < len(sorted_list_tuple_by_year) - 1 and tmp[0][1] == sorted_list_tuple_by_year[i + 1][1]:
            tmp.append(sorted_list_tuple_by_year[i + 1])
            i += 1
        sorted_list_list_tuple_by_year.append(tmp)
        i += 1

    for index, elem in enumerate(sorted_list_list_tuple_by_year):
        sorted_list_list_tuple_by_year[index] = sorted(elem, key=lambda item: item[0])

    sorted_list_tuple_by_year_name: list[tuple[str, str]] = \
        [item for sublist in sorted_list_list_tuple_by_year for item in sublist]

    sorted_d: dict[str, str] = {name: year for name, year in sorted_list_tuple_by_year_name}

    for name, year in sorted_d.items():
        print(f'{name} : {year}')


if __name__ == '__main__':
    my_sort()
