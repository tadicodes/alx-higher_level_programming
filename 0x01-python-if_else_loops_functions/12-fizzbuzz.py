#!/usr/bin/python3
# 12-fizzbuzz.py


def fizzbuzz():
    """Print the numbers from 1 to 100 separated by a space
    if multiples of three, print Fizz instead of number
    if multiples of five, print Buzz instead of number
    if multiples of three and five, print FizzBuzz instead of number
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
