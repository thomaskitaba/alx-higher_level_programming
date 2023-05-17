#!/usr/bin/python3
def roman_to_int(roman_string):
    d_r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_key = list(d_r.keys())
    sum = 0
    Next = 0
    for roman in roman_string:
        for i in range(len(roman_key)):
            current = d_r[roman_key[i]]
            if i < len(roman_key) - 1:
                Next = d_r[roman_key[i + 1]]

            if roman == roman_key[i]:
                if current < Next and roman_key[i] == 'I':
                    sum -= 1
                else:
                    sum += d_r[roman_key[i]]
    return (sum)
