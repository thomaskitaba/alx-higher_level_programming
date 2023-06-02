#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if not tuple_a and not tuple_b:
        return(0, 0)
    if not tuple_a:
        return tuple_b
    elif not tuple_b:
        return tuple_a
    elif len(tuple_a) == 1:
        if len(tuple_b) == 0:
            return (tuple_a[0], 0)
        elif len(tuple_b) == 1:
            return (tuble_a[0] + tuble_b[0], 0)
        else:
           return(tuple_a[0] + tuple_b[0], tuple_b[1])
    elif len(tuple_b) == 1:
        if len(tuple_a) == 0:
            return(tuple_b[0], 0)
        elif len(tuple_a) == 2:
            return(tuple_a[0] + tuple_b[0], tuple_a[1])
    else:
        return(tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])