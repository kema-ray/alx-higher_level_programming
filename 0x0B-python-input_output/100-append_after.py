#!/usr/bin/python3
"""
append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each 
    line containing a specific string 
    """
    read = []
    with open(filename, "r", encoding="utf-8") as file:
        read = file.readlines()
        index = 0

        while index < len(read):
            if search_string in read[index]:
                read[index:index + 1] = [read[index],new_string]
                index += 1
            index += 1

    with open(filename, "w", encoding="utf-8") as files:
        files.writelines(read)
