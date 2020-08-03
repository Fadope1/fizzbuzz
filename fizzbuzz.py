def fizzbuzz(number: int, div_nums=None) -> str:
    output = ""
    # if no div_nums are given, use normal nums/ words
    div_numbers = div_nums if type(div_nums) == dict else {3: "fizz", 5: "buzz"}
    for div_nr in div_numbers:
        # if current number is divisable by div_nr add corresponding word to output
        if number%div_nr == 0: output += div_numbers[div_nr]

    if not output:
        return number # if output empty return number
    return output

for i in range(1, 101):
    print(i, fizzbuzz(i))
