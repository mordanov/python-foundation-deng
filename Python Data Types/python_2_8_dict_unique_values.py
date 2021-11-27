def main():
    print(dict_unique_values([{"C1": "banana"}, {"C2": "apple", "C3": "plum"}, {"C4": "peach"},
                              {"C5": "grape", "C6": "pear", "C7": "feijoa"}, {}]))
    print(dict_unique_values(
        [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
         {"VIII": "S007"}]))


def dict_unique_values(value: list) -> list:
    uniq = set()
    for d in value:
        if isinstance(d, dict):
            uniq.update(d.values())
    return list(uniq)


if __name__ == '__main__':
    main()


def main():
    print(convert_tuple((4, 8, 15, 16, 23, 42)))
