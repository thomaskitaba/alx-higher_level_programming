#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    count = 0
    new_list = []

    for row in my_list:
        try:
            if (my_list.index(row) <= x - 1):
                new_list.append(row)
                count += 1
        except IndexError:
            break
    for new_row in new_list:
        try:
            print("{}".format(new_row), end='')
        except (TypeError, ValueError):
            break
        finally:
            print()
    return (count)
