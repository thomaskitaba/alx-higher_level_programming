#!/usr/bin/python3
for ascii_num in range(97, 123):
    if chr(ascii_num) != "e" and chr(ascii_num) != "q":
        print("{}".format(chr(ascii_num)), end='')
