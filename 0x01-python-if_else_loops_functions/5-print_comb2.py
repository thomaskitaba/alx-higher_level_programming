#!/usr/bin/python3
for num in range(0, 100):
    if num == 99:
        print("{}".fromat(num))
    else:
        print("{:02}".format(num), end=", ")
