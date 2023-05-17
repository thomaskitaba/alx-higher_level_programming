#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    prod = 1
    sum_of_prod = 0
    total = 0
    for data in my_list:
        prod = data[0] * data[1]
        sum_of_prod += prod
        total += data[1]
    # print("Average: {:0.2f}".format(sum_of_prod / total))
    return (sum_of_prod / total)
