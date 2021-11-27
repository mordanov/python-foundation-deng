from collections import OrderedDict

from python_2_2_chars_count import chars_count


def main():
    d = chars_count("Hello from Hell")
    print(sort_dict_by_value(d))
    d = chars_count('Oh, it is python')
    print(sort_dict_by_value(d))
    d = chars_count('abcdefghilklmnopqrstufwxyz')
    print(sort_dict_by_value(d))


def sort_dict_by_value(value: dict) -> dict:
    d = OrderedDict()
    for v in sorted(value.items(), reverse=True):
        key = list(value.keys())[list(value.items()).index(v)]
        d[key] = v[1]
    return dict(d)


if __name__ == '__main__':
    main()
