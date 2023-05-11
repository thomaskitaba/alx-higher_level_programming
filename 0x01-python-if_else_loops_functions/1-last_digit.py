#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
revert = 0
if number < 0:
    number *= -1
    revert = 1
main_num = number // 10
if main_num != 0:
    last_digit = number - 10 * main_num
else:
    last_digit = 0
if revert != 0:
    last_digit *= -1
    number *= -1
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    print(
        f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
