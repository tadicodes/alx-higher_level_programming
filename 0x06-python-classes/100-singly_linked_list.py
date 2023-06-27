#!/usr/bin/python3
"""define classes for a singly linked list"""


class Node:
    """represent a node in a singly linked list"""

    def __init__(self, data, next_node=None):
        """initialize a new node

        Args:
            data (int): data of the new node
            next_node (Node): next node of the new node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """set the data of the node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an int")
        self.__data = value

    @property
    def next_node(self):
        """set the next_node of the node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a node object")
        self.__next_node = value


class SinglyLinkedList:
    """represent singly linked list"""

    def __init__(self):
        """initalize new singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """insert a new node to singly linked list

        node is inserted into the list at the correct
        ordered numerical position

        Args:
            value (Node): new node to insert
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """define the print() representation of singly linked list"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
