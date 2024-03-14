#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    allfunctions = dir()
    for i in range (0, len(allfunctions)):
        if allfunctions[i] [:2] != "__":
            print("{:s}".format(allfunctions[i]))
