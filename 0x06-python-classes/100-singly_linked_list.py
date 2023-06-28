#!/usr/bin/python3
"""
Module: linked_list
Defines classes for singly linked list and its nodes.
"""


class Node:
    """
    Represents a node in a singly linked list.

    Attributes:
        data (int): The data value stored in the node.
        next_node (Node): The reference to the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Args:
            data (int): The data value to be stored in the node.
            next_node (Node, optional): The reference \
                    to the next node in the list.
                Defaults to None.

        Raises:
            TypeError: If the data value is not an integer.
            TypeError: If the next_node is not a Node object or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data value of the node.

        Returns:
            int: The data value of the node.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Sets the data value of the node.

        Args:
            value (int): The data value to be set.

        Raises:
            TypeError: If the data value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer.")
        self._data = value

    @property
    def next_node(self):
        """
        Retrieves the reference to the next node in the list.

        Returns:
            Node: The reference to the next node.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the reference to the next node in the list.

        Args:
            value (Node): The reference to the next node.

        Raises:
            TypeError: If the next_node is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next node must be a Node object or None.")
        self._next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
        head (Node): The reference to the head node of the list.
    """

    def __init__(self):
        """
        Initializes a new instance of the SinglyLinkedList class.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new node into the correct sorted position in the list.

        The list is sorted in increasing order.

        Args:
            value (int): The data value of the new node.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and\
                    value > current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        node = self.head
        result = ""
        while node is not None:
            result += str(node.data) + "\n"
            node = node.next_node
        return result.strip()
