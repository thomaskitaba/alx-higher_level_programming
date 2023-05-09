#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(len(str)):
        if i == n:
            if i == len(str) - 1:
                str[i] = ''
            else:
                for j in range(i, len(str)):
                    if j == len(str) - 1:
                        str[j] = ''
                    else:
                        str[j] = str[j + 1]
                break
    return str
