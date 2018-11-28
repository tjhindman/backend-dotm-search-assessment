#!/usr/bin/env python
"""
Given a directory path, this searches all files in the path for a given text string 
within the 'word/document.xml' section of a MSWord .dotm file.
"""

# Your awesome code begins here!

import os
import sys
import argparse
import zipfile

def dir_search(*cmd_args):
    directory, text = cmd_args

    items = os.listdir(directory)

    for f in items:
        file = directory + "/" + f

        if f.endswith(".dotm"):
            with zipfile.ZipFile(file) as myzip:
                if 'word/document.xml' in myzip.namelist():
                    with myzip.open('word/document.xml') as doc_text:
                        for line in doc_text:
                            if text in line:
                                a = line.index(text)
                                print "Match found in file " + file + "\n" + line[a - 40: a] + line[a: a + 40]


# def dotm_search(text):
#     items = os.listdir(os.getcwd())

#     for d in items:
#         for f in os.listdir(d):
#             print f
        # file = './' + f

        # if f.endswith(".dotm"):
        #     with zipfile.ZipFile(file) as myzip:
        #         if 'word/document.xml' in myzip.namelist():
        #             with myzip.open('word/document.xml') as doc_text:
        #                 for line in doc_text:
        #                     if text in line:
        #                         a = line.index(text)
        #                         print "Match found in file " + file + "\n" + line[a - 40: a] + line[a: a + 40]



def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('text')
    parser.add_argument('--dir')

    parsed_args = parser.parse_args(args)

    if parsed_args.dir:
        dir_search(parsed_args.dir, parsed_args.text)
    elif not parsed_args.dir:
        dotm_search(parsed_args.text)
    else:
        print "Unknown command."


if __name__ == '__main__':
    main(sys.argv[1:])