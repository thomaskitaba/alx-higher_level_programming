#!/usr/bin/python3
def print_last_digit(number):
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
    return last_digit
