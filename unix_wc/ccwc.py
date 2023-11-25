#!/usr/bin/env python3

from argparse import ArgumentParser
import os
import sys
import string
import io


class INPUT:
    NONE = "none"
    BYTES = "bytes"
    LINES = "lines"
    WORDS = "words"
    CHARS = "chars"


def get_file_size_in_bytes(content):
    return len(content.encode("utf-8"))


def get_number_of_lines(content):
    return len(content.split("\n"))


def get_number_of_words(content):
    lines = content.split("\n")
    word_count_per_line = [len(line.split()) for line in lines if len(line.strip()) > 0]
    return sum(word_count_per_line)
    

def get_number_of_chars(content):
    return len(content)


def process(content, arg):
    if arg == INPUT.BYTES:
        return [get_file_size_in_bytes(content)]
    if arg == INPUT.LINES:
        return [get_number_of_lines(content)]
    if arg == INPUT.WORDS:
        return [get_number_of_words(content)]
    if arg == INPUT.CHARS:
        return [get_number_of_chars(content)]
    if arg == INPUT.NONE:
        return [get_number_of_lines(content), get_number_of_words(content), get_file_size_in_bytes(content)]


def wc():
    arg_parser = ArgumentParser("ccwc")
    arg_parser.add_argument("-c", "--characters", action="store_true")
    arg_parser.add_argument("-l", "--lines", action="store_true")
    arg_parser.add_argument("-w", "--words", action="store_true")
    arg_parser.add_argument("-m", "--multibyte", action="store_true")
    arg_parser.add_argument("file", type=str, nargs="?")
    args = arg_parser.parse_args()

    arg = INPUT.NONE
    if args.characters:
        arg = INPUT.BYTES
    elif args.lines:
        arg = INPUT.LINES
    elif args.words:
        arg = INPUT.WORDS
    elif args.multibyte:
        arg = INPUT.CHARS
    
    if args.file is not None:
        with open(args.file, "r") as file:
            content = file.read()
    else:
        content = sys.stdin.read()
        

    output = process(content, arg)
    print(" ", *output, args.file if args.file else "")
    


if __name__ == "__main__":
    wc()