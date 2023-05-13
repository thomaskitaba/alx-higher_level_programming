#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a == 0:
        a_x = 0
        a_y = 0
    elif len_a == 1:
        a_x = tuple_a[0]
        a_y = 0
    else:
        a_x = tuple_a[0]
        a_y = tuple_a[1]

    if len_b == 0:
        b_x = 0
        b_y = 0
    elif len_b == 1:
        b_x = tuple_b[0]
        b_y = 0
    else:
        b_x = tuple_b[0]
        b_y = tuple_b[1]
    new_tuple = (a_x + b_x, a_y + b_y)
    return (new_tuple)
