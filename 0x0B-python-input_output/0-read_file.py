#!/usr/bin/python3
"""
Module for read_file function
"""


def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, "r", encoding="utf-8") as file:
        files = file.read()
        print(files, end="")
