#!/urs/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arg in matrix:
        for i in range(len(arg)):
            print("{:d}".format(arg[i]), end="" if i == len(arg) - 1 else " ")
            # if i == len(arg) - 1:
            #     print("{:d}".format(arg[i]), end="")
            # else:
            #     print("{:d}".format(arg[i]), end=" ")
        print()
