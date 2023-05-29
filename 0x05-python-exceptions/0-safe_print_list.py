#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if isinstance(my_list, list):
        count = 0
        try:

            for row in my_list:
                if (my_list.index(row) <= x - 1):
                    count += 1
                else:
                    break
            return (count)
        except IndexError:
            print("Error: index")
