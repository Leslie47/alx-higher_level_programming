#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10  # gets the last digit of the number

if number < 0:  # Check if the original number was negative
    last_digit = -(last_digit)   # adjusts last digit to be negative

output = "Last digit of {} is {}".format(number, last_digit)

if last_digit > 5:
    print(f"{output} and is greater than 5")
elif last_digit == 0:
    print(f"{output} and is 0")
else:
    print(f"{output} and is less than 6 and not 0")
