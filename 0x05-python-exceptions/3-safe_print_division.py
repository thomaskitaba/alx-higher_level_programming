#!/usr/bin/python3
def safe_print_division(a, b):
	result = 1
	try:
		result = a / b
		return (result)
	except ZeroDivisionError:
		return None
	finally:
		print("Inside result: ", end = '')
		print("{}".format(result))
