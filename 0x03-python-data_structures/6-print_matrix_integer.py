#!/urs/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arg in matrix:
        for count, i in enumerat(arg):
            if count == len(arg) - 1:
                print("{:d}".format(i), end="")
            else:
                print("{:d}".format(i), end=" ")
        print()
