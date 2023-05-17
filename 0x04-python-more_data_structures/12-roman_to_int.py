#!/usr/bin/python3
def roman_to_int(roman_string):
    d_r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_key = list(d_r.keys())
    sum = 0
    Next = 0
    for j in range(len(roman_string)):
        for i in range(len(roman_key)):
            current = d_r[roman_key[i]]
            if j < len(roman_string) - 1:
                Next = d_r[roman_string[j + 1]] #change it to roman string

            if roman_string[j] == roman_key[i]:
                if current < Next:
                    sum -= d_r[roman_key[i]]
                else:
                    sum += d_r[roman_key[i]]
    return (sum)
