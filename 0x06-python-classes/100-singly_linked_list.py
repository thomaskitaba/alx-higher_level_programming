#!/usr/bin/python3
""" linked list implementaion using """

class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value
    @property
    def next_node(self):
        return (self.__next_node)

    @data.setter
    def next_node(self, value):
        if type(value) !=  Node(): #check for node()
            raise TypeError("data must be an integer")
        else:
            self.__next_node = value

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        """ insert node on sorted position"
