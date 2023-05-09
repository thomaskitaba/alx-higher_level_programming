#!/usr/bin/python3
def uppercase(str):
    temp = []
    for char in range(len(str)):
        if ord(str[char]) >= 97 and ord(str[char]) <= 122:
            temp.append(chr(ord(str[char]) - 32))
            continue
        temp.append(str[char])
    print("{}".format(temp))
