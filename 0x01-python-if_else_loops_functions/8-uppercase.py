#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            # temp.append(chr(ord(str[char]) - 32))
            char = chr(ord(str[char]) - 32)

        print("{}".format(char), end='')
    print("")
    # temp.append(str[char])
