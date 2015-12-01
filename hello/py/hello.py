#!/usr/bin/env python3

import skilstak.colors as c

def hello(who):
    """Print Hello world!"""
    print(c.clear + "Hello " + who + c.reset)

def multi(message):
    """print hello world in multicolored letters"""
    while True:
        print(c.clear + c.multi(message))

def nyan(message):
    """print hello world in nyan"""
    while True:
        print(c.rc() + message, end= " ")


if __name__ == "__main__":
    import sys
    
    option = ""
    message = ""
    who = "world"
    
    if len(sys.argv) > 2:
        option = sys.argv[1]
        who = sys.argv[2]
    elif len(sys.argv) == 2:
        if sys.argv[1].startswith("-"):
            option = sys.argv[1]
        else:
            who = sys.argv[1]

        message = "Hello " + who

    if option == "-n":
        nyan(message)
    if option == "-m":
        multi(message)
    else:
        hello(who)
