def main():
    print(distinct_words("Mary had a Mary little lamb a".split()))


def distinct_words(value: list) -> list:
    return sorted(list(set(value)))


if __name__ == '__main__':
    main()
