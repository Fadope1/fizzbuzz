"""
Small program that tries to solve the fizzbuzz puzzle
Python=3.10
Made by Fabian (Fadope1)
"""


def standard_fizzbuzz(number: int) -> str:
    """Most standard way of solving the fizzbuzz puzzle."""
    if number%3 == 0 and number%5 == 0: return "fizzbuzz"
    if number%3 == 0: return "fizz"
    if number%5 == 0: return "buzz"
    return str(number)


def flexible_fizzbuzz(number: int, div_nums=None) -> str:
    """Most flexible way of solving the fizzbuzz puzzle."""
    output = ""
    # if no div_nums are given, use normal nums/ words
    div_numbers = div_nums if div_nums is dict else {3: "fizz", 5: "buzz"}
    for div_nr in div_numbers:
        # if current number is divisable by div_nr add corresponding word to output
        if number%div_nr == 0:
            output += div_numbers.get(div_nr)

    return str(number) if not output else output


if __name__ == "__main__":
    # standard way
    for index in range(0, 101):
        print(f"{index=} => {flexible_fizzbuzz(index)} | {standard_fizzbuzz(index)}")

    # flexible way
    for index in range(0, 101):
        print(f"{index=} => {flexible_fizzbuzz(index, div_nums={2: "fizz", 4: "buzz", 7: "sizz"})}")
