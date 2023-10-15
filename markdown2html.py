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
                    self.input_file_lines = f.read().split('\n')
                    self.output_file_path = sys.argv[2]
                    self.output_file_lines = []
                    self.has_opened_ul_tag = False
            except FileNotFoundError:
                print("Missing {}".format(sys.argv[1]), file=sys.stderr)
                exit(1)

    def parse_input_file(self):
        """
        Parses an input markdown file and converts it to HTML

        Returns (string): The string containing the HTML output
        """
        for index, line in enumerate(self.input_file_lines):
            parsed_line = self.parse_markdown_headings(line)
            parsed_line = self.parse_unordered_list(parsed_line, index)
            self.output_file_lines.append(parsed_line)

    @staticmethod
    def parse_markdown_headings(line):
        """
        Parses markdown heading content

        Args:
             line (string) : line from input file to parse

        Returns (string): The parsed markdown string
        """
        levels = ["###### ", "##### ", "#### ", "### ", "## ", "# "]

        for level in levels:
            if line.startswith(level):
                line = line.replace(level, "")
                return "<h{}>{}</h{}>".format(len(level), line, len(level))
        return line

    def parse_unordered_list(self, line, index):
        """
        Parses markdown unordered list content

        Args:
             line (string) : line from input file to parse
             index (int): the line number being parsed

        Returns (string): The parsed markdown string
        """
        if line.startswith("- ") and not self.has_opened_ul_tag:
            self.has_opened_ul_tag = True
            output = "<ul>\n\t<li>{}</li>".format(line.replace("- ", ""))
            return self.return_closing_tag(index, output)
        elif line.startswith("- ") and self.has_opened_ul_tag:
            output = "\t<li>{}</li>".format(line.replace("- ", ""))
            return self.return_closing_tag(index, output)
        elif not line.startswith("- ") and self.has_opened_ul_tag:
            self.has_opened_ul_tag = False
            output = "</ul>\n{}".format(line)
            return output
        return line

    def return_closing_tag(self, index, output):
        """
        Returns closing ul tag based on the rendering status

        Args:
            index (int): The current iteration number
            output (string): The current string being parsed

        Returns (string): The parsed markdown string
        """
        if index == len(self.input_file_lines) - 1:
            output += "\n</ul>"
        return output

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
