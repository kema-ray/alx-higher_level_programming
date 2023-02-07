#!/usr/bin/python3
"""
Module for write_file function
"""


def write_file(filename="", text=""):
    """
    write_file writes a string to a text file.
    Args:
        filename (str): name of file.
        text (str): text to be written.
    Return: the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        files = file.write(text)
        return(files)
