#!/usr/bin/python3
"""linked list implementaion using class."""


class Node:
    """Create Node"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for data"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for next node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Create and manage a singly linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Insert node on sorted position"""
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and value > current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Print the linked list"""
        current = self.__head
        temp_list = []
        while current is not None:
            temp_list.append(str(current.data))
            current = current.next_node
        return "\n".join(temp_list)
