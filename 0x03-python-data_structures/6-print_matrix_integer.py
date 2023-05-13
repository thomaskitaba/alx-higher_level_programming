#!/urs/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arg in matrix:
        for i in range(len(arg)):
            if i == len(arg) - 1:
                print("{}".format(arg[i]), end='')
            else:
                print("{}".format(arg[i]), end=' ')

        print('')