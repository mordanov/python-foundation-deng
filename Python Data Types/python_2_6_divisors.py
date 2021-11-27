def main():
    n = input("Enter your number:")
    print(divisors(int(n)))


def divisors(number: int) -> list:
    divisors = []
    for n in range(1, number + 1):
        if number % n == 0:
            divisors.append(n)
    return divisors


if __name__ == '__main__':
    main()
