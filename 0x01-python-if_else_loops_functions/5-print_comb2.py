#!/usr/bin/python3
for i in range(100):
    if i == 99:
        print("{}".fromat(i))
    else:
        print("{:02}".fromat(i), end=', ')
