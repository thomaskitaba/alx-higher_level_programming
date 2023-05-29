#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
	count = 0
	new_list = []

	for row in my_list:
		try:
			if (my_list.index(row) <= x - 1):
				try:
					print("{:d}".format(row), end='')
					count += 1
				except (TypeError, ValueError):
					break
		except IndexError:
			break
	print()
	return (count)
