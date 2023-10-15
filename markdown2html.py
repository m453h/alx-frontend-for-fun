#!/usr/bin/python3

"""
This module converts Markdown file to HTML

Usage:
    ./markdown2html.py <input_file> <output_file>

Args:
 - input_file: name of the input Markdown file
 - output_file: name of the output HTML file

Example:
    ./markdown2html.py README.md README.html
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
                print("Missing {}".format(sys.argv[1]), file=sys.stderr)
                exit(1)


if __name__ == "__main__":
    converter = MarkDown2HTML()
