#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    if isinstance(my_list_1, list) and isinstance(my_list_2, list):
        new_list = []
        result = 0
        for i in range(list_length):
            try:
                result = my_list_1[i] / my_list_2[i]
            except (TypeError, ValueError):
                result = 0
                print("wrong type")
            except IndexError:
                result = 0
                print("out of range")
            except (ZeroDivisionError, ValueError):
                result = 0
                print("division by 0")
            finally:
                new_list.append(result)
        return (new_list)
