#!/usr/bin/python3
"""
Reads a text file (UTF8) and prints it to stdout"""

def read_file(filename=""):
    """Reads a file and prints its content"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")

if __name__ == "__main__":
    read_file("my_file_0.txt")
