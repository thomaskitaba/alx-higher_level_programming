#!/usr/bin/python3
"""
return True or False based on the object type
"""

def is_same_class(obj, a_class):
	if isinstance(obj, a_class):
		return (True)
	return (False)