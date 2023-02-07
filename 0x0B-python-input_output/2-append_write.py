#!/usr/bin/python3
"""
Module for appends text function
"""


def append_write(filename="", text=""):
    """
    appends a string and returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as file:
        files = file.write(text)
        return files
