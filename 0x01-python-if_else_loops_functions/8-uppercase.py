#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str) >= 97 and ord(str) <= 122:
            str[i] = chr(i - 32)
    print("{}".format(str))
