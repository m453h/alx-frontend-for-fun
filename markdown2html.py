#!/usr/bin/python3

"""
This module takes an argument with 2 strings:
 - First argument is the name of the Markdown file
- Second argument is the output file name
"""
import sys


class MarkDown2HTML:
    def __init__(self):
        """
        Initialize a new instance of Markdown2HTML class
        """
        if len(sys.argv) < 3:
            print('Usage: ./markdown2html.py README.md README.html',
                  file=sys.stderr)
            exit(1)
        else:
            try:
                with open(sys.argv[1]) as f:
                    self.input_file_content = f.read()
            except FileNotFoundError:
                print("Missing {}".format(sys.argv[1]))
                exit(1)


if __name__ == "__main__":
    converter = MarkDown2HTML()
