#!/usr/bin/python3
"""linked list implementaion using class."""



class Node:
    """ create Node """

    def __init__(self, data, next_node=None):

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ setter for next node """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """setter next_node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ create and mangage a singly linked list """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """ insert node on sorted position"""
        new_node = Node(value)
        """ if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        """
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            """ continue checking the other nodes """
            current = self.__head

            while (current.next_node is not None and value > current.next_node.data):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """ print the linked list using print method """
        current = self.__head
        temp_list = []

        while current is not None:
            temp_list.append(str(current.data))
            current = current.next_node
        return ('\n'.join(temp_list))
