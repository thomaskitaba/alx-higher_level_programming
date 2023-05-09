#!/usr/bin/python3
def uppercase(str):
    for char in range(len(str)):
        if ord(str[char]) >= 97 and ord(str[char]) <= 122:
            str[char] = chr(char - 32)
    print("{}".format(str))
