#!/usr/bin/python3
""" linked list implementaion using class"""


class Node:

    def __init__(self, data, next_node=None):
        """ instantiate Node """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ getter for data """
        return self.__data

    @data.setter
    def data(self, value):
        """ setter for data """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ getter for next_node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ setter for next_node """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ create and manage a linked list """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """ insert node on sorted position"""
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            """ check the head first """
            current = self.__head

            while current.next_node is not None and value > current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """ print the linked list """
        current = self.__head
        temp_list = []

        while current is not None:
            temp_list.append(str(current.data))
            current = current.next_node
        return ('\n'.join(temp_list))
