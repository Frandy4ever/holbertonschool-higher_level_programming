#!/usr/bin/python3
def fizzbuzz():
    # Generate the FizzBuzz values for numbers from 1 to 100.
    fizzbuzz_values = []
    for number in range(1, 101):
        value = ""
        if number % 3 == 0:
            value += "Fizz"
        if number % 5 == 0:
            value += "Buzz"
        fizzbuzz_values.append(value or str(number))

    # Print the FizzBuzz values separated by spaces.
    print(" ".join(fizzbuzz_values))