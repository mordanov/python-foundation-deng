def main():
    print(new_len("abc"))
    print(new_len("123"))
    print(new_len(123))
    print(new_len())
    print(new_len(["1","2","3"]))


def new_len(value = None) -> int:
    if isinstance(value, str):
        c = 0
        for _ in list(value):
            c += 1
        return c
    else:
        return 0


if __name__ == '__main__':
    main()
