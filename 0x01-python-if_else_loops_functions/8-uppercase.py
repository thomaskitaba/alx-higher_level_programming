#!/usr/bin/python3
def uppercase(str):
    temp
    for char in range(len(str)):
        if ord(str[char]) >= 97 and ord(str[char]) <= 122:
            # temp.append(chr(ord(str[char]) - 32))
            temp = chr(ord(str[char]) - 32)

        print("{}".format(temp), end='')
    print("")
    # temp.append(str[char])
