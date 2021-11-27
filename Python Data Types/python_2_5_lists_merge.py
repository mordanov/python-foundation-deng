def main():
    print(lists_merge([1, 4, 6, 2, 3, 9, 6, 4, 2], [10, 1, 2, 3, 4, 5]))


def lists_merge(value1: list, value2: list) -> list:
    return list(set(value2) & set(value1))


if __name__ == '__main__':
    main()
