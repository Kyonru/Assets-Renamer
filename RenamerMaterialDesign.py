# -*- coding: utf-8 -*-
"""
RenamerMaterialDesign.py - Renaming your Android assets the easy way.

usage: python RenamerMaterialDesign.py [-h] -p PATH -f FILENAME
"""
import argparse
import os
import sys

if __name__ == '__main__':
    print "RenamerMaterialDesign.py - Rename your Android assets the easy way."

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="The Assets path.", required=True,
                        dest="path")
    parser.add_argument("-f", "--filename", help="Asset new filename pattern.",
                        required=True, dest="filename")
    args = parser.parse_args()

    if args.path and args.filename:
        if not os.path.isdir(args.path):
            print "ERROR: Can't find path: " + args.path
            sys.exit(-1)

        if not os.access('/path/to/folder', os.W_OK):
            print "ERROR: " + args.path + " is not writable."
            sys.exit(-1)

        size = {
            'drawable-mdpi': args.filename + '.',
            'drawable-hdpi': args.filename + '@1.5x.',
            'drawable-xhdpi': args.filename + '@2x.',
            'drawable-xxhdpi': args.filename + '@3x.',
            'drawable-xxxhdpi': args.filename + '@4x.'
        }

        print args.path  # Selected path

        for directory in os.listdir(args.path):
            if directory[0] == '.':
                continue
            print directory  # Current directory
            print size[directory]
            for asset in os.listdir(args.path + directory):
                name = asset.split('.')
                os.rename(args.path + directory + '/' + asset,
                          args.path + size[directory] + name[1])
        sys.exit(0)  # Everything run OK
