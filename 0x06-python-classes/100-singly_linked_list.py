#!/usr/bin/python3
""" linked list implementaion using """


class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """ insert node on sorted position"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            """ check the head first """
            current = self.__head
            Next = self.__head
            Next = Next.next_node

            if value < self.__head.data:
                new_node.next_node = self.__head
                self.__head = new_node

            while Next.next_node:
                if value < Next.data:
                    current.next_node = new_node
                    new_node.next_node = Next
                    return
            """ means it reaced the end of the list"""
            Next.next_node = new_node

    def __str__(self):
        current = self.__head
        temp_list = []

        while current is not None:
            temp_list.append(str(current.data_))
            current = current.next_node
        return ('\n'.join(temp_list))
