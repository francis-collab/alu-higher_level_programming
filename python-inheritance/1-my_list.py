#!/usr/bin/python3
"""
Module containing MyList class.
"""

class MyList(list):
    """
    MyList inherits from list and adds a method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
