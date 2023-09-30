#!/usr/bin/python3

""" defines a node of a singly linked list """


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):

        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):

        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None
        self.new = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
        """
        self.new = Node(value)

        if self.__head is None or value < self.__head.data:
            """ Create head of the linked list if there is no head """
            self.new.next_node = self.__head
            self.__head = self.new
            return

        traverse = self.__head
        while traverse.next_node and traverse.next_node.data < value:
            traverse = traverse.next_node

        self.new.next_node = traverse.next_node
        traverse.next_node = self.new

    def __repr__(self):
        result = ""
        traverse = self.__head
        while traverse:
            result += "{}".format(traverse.data)
            traverse = traverse.next_node
            if traverse:
                result += '\n'

        return result
