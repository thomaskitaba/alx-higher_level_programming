#!/usr/bin/python3
def roman_to_int(roman_string):
    dict_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_key = list(dict_roman.keys())
    sum = 0
    for roman in roman_string:
        for i in range(len(roman_key)):
            if roman == roman_key[i]:
                sum += dict_roman[roman_key[i]]
    print(sum)

roman_to_int("II")