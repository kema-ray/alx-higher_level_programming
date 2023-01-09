#!/usr/bin/python3
def multiple_returns(sentence):
    this_tuple = ()
    if len(sentence) == 0:
        this_tuple = 0, "None"
    else:
        this_tuple = len(sentence), sentence[0]
    return this_tuple
