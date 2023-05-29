#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
	count = 0
	new_list = []

	for i in range(x):
		try:
			if (my_list.index(my_list[i]) <= x - 1):
				try:
					print("{:d}".format(my_list[i]), end='')
					count += 1
				except (TypeError, ValueError):
					continue

		except IndexError:
			print()
			print("IndexError: list index out of range", end = '')
	return (count)
