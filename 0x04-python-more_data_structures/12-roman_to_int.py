#!/usr/bin/python3
def roman_to_int(roman_string):
    d_r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_key = list(d_r.keys())
    sum = 0
    for roman in roman_string:
        for i in range(len(roman_key)):
            if roman == roman_key[i]:
                sum += d_r[roman_key[i]]
    print(sum)


roman_to_int("II")
