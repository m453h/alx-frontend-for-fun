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
import re


class MarkDown2HTML:
    def __init__(self):
        """
        Initializes a new instance of Markdown2HTML class

        Raises:
            FileNotFoundError: if input file is missing
        """
        if len(sys.argv) < 3:
            print('Usage: ./markdown2html.py README.md README.html',
                  file=sys.stderr)
            exit(1)
        else:
            try:
                with open(sys.argv[1]) as f:
                    self.input_file_content = f.read()
                    self.output_file_path = sys.argv[2]
                    self.output_file_lines = []
            except FileNotFoundError:
                print("Missing {}".format(sys.argv[1]), file=sys.stderr)
                exit(1)

    def parse_input_file(self):
        """
        Parses an input markdown file and converts it to HTML

        Returns (string): The string containing the HTML output
        """
        input_file_lines = self.input_file_content.split('\n')

        for line in input_file_lines:
            self.output_file_lines.append(self.parse_markdown_headings(line))

    @staticmethod
    def parse_markdown_headings(line):
        """
        Parses markdown heading content

        Args:
             line (string) : line from input file to parse

        Returns (string): The parsed markdown string
        """
        levels = ["######", "#####", "####", "###", "##", "#"]

        for level in levels:
            if line.startswith(level):
                line = line.replace(level, "").strip()
                output = "<h{}>{}</h{}>".format(len(level), line, len(level))
                return output
        return line

    def save_output_file(self):
        """
        Writes string content to a specified output file
        """
        with open(self.output_file_path, "w", encoding="utf-8") as output_file:
            for line in self.output_file_lines:
                output_file.write(line + "\n")
        output_file.close()
        return True


if __name__ == "__main__":
    converter = MarkDown2HTML()
    converter.parse_input_file()
    converter.save_output_file()
