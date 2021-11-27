def main():
    print(chars_count("Mary had a little lamb"))
    print(chars_count("Its fleece was white as snow"))
    print(chars_count("Everywhere the child went"))
    print(chars_count("The little lamb was sure to go"))
    print(chars_count('Oh, it is python'))
    print(chars_count(""))


def chars_count(value: str) -> dict:
    d = {}
    if isinstance(value, str):
        for c in list(value.lower()):
            d[c] = 1 if d.get(c) is None else d[c] + 1
    return d


if __name__ == '__main__':
    main()
