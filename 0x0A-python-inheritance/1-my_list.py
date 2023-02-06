#!/usr/bin/python3
"""
Mylist class that inherits from list
"""

class MyList(list):
    """
    MyList class that inherits from list
    """

    def __init__(self):
        """Object initialization"""
        super().__init__()

    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
