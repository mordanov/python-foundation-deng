def main():
    print(print_lower_5([1, 2, 3, 1, 2, 5, 6, 7, 8]))


def print_lower_5(value: list) -> str:
    return " ".join(map(lambda x: str(x), filter(lambda x: x < 5, list(set(value)))))


if __name__ == '__main__':
    main()
