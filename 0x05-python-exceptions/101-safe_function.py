#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        f = fct(*args)
        return (f)
    except Exception as error:
        print("Exception: {}".format(error), file=stderr)
        return None
