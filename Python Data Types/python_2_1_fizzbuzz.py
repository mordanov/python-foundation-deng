def main():
    for i in range(1, 101):
        print(fizzbuzz(i))


def fizzbuzz(number) -> str:
    if number % 5 == 0 and number % 3 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "Buzz"    
    elif number % 3 == 0:
        return "Fizz"
    else:
        return str(number)


if __name__ == '__main__':
    main()
