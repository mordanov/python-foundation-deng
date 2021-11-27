def main():
    print(convert_tuple((1,2,3,5,8,13)))

def convert_tuple(value: tuple) -> int:
    s = 0
    digit = 1
    for v in reversed(value):
        s += v * digit
        digit *= 10 ** len(str(v))
    return s


if __name__ == '__main__':
    main()
