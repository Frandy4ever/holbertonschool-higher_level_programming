#!/usr/bin/python3
def fizzbuzz():
    # Loop through numbers from 1 to 100.
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            # If the number is divisible by both 3 and 5, print "FizzBuzz" without a space.
            print("FizzBuzz", end=" ")
        elif number % 3 == 0:
            # If the number is divisible by 3, print "Fizz" without a space.
            print("Fizz", end=" ")
        elif number % 5 == 0:
            # If the number is divisible by 5, print "Buzz" without a space.
            print("Buzz", end=" ")
        else:
            # For all other numbers, print the number itself without a space.
            print(number, end=" ")

