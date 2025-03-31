#!/usr/bin/python3
"""
This module defines two classes: Node and SinglyLinkedList for managing
a singly linked list where nodes are inserted in sorted order.
"""

class Node:
    """
    Class to define a node in a singly linked list.
    
    Attributes:
        data (int): The data stored in the node.
        next_node (Node or None): A reference to the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new node with given data and next_node.

        Args:
            data (int): The data stored in the node.
            next_node (Node or None): Reference to the next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data of the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data of the node.

        Args:
            value (int): The data to store in the node.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the reference to the next node in the list.

        Returns:
            Node or None: The next node in the list or None.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the reference to the next node in the list.

        Args:
            value (Node or None): The next node in the list or None.

        Raises:
            TypeError: If the value is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Class to define a singly linked list where nodes are inserted in sorted order.

    Attributes:
        head (Node or None): The first node in the list.
    """

    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.head = None

    def __str__(self):
        """
        Returns a string representation of the list by printing the data of each node.

        Returns:
            str: A string containing all the data values in the list, one per line.
        """
        current = self.head
        result = []
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        Inserts a new node with the given value into the list in sorted order.

        Args:
            value (int): The data to store in the new node.
        """
        new_node = Node(value)

        # Case 1: If the list is empty or the new value should be placed at the head
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            # Case 2: Traverse the list to find the correct insertion point
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            # Insert the new node at the correct position
            new_node.next_node = current.next_node
            current.next_node = new_node

