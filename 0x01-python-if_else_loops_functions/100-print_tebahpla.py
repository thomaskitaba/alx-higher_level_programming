#!/usr/bin/python3
num = 0
for i in range(122, 96, -1):
    num = i
    if (i % 2 != 0):
        num = i - 32
    print("{}".format(chr(num)), end='')
