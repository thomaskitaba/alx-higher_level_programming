#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
  if idx < 0 or idx > len(my_list) - 1:
    return (my_list)
  new_list = []
  for i in range(len(my_list)):
    # if i != idx:
    #   new_list.append(my_list[i])

    if i == idx:
      my_list = my_list[:i] + my_list[i + 1:]
  my_list = new_list
  return (my_list)