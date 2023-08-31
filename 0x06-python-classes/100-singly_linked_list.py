#!/usr/bin/python3
""" This module contains a class 'Node'"""


class Node:
    """This class represents a 'Node'"""
    def __init__(self, data, next_node=None):
        """Instantiating data and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method for data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method for next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method for next_node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class represents a SinglyLinkedList"""
    def __init__(self):
        """Instantiating"""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the current position"""
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """The string rep of the class instance"""
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
