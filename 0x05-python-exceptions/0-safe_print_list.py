#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    new_list = []

    for i in x:
        try:
            new_list.append(my_list[i])
                count += 1
        except IndexError:
            break
    for new_row in new_list:
        print("{}".format(new_row), end='')
    print()
    return (count)
