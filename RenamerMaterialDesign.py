# -*- coding: utf-8 -*-
"""
RenamerMaterialDesign.py - Renaming your Android assets the easy way.

usage: python RenamerMaterialDesign.py [-h] -p PATH -f FILENAME [-d DESTINATION]
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
    parser.add_argument("-d", "--destination", help="Asset new path", required=False,
                        dest="destination")
    args = parser.parse_args()

    if args.path and args.filename:

        path = os.path.abspath(args.path) + '/'
        destination_path = os.getcwd() + '/'

        if not os.path.isdir(path):
            print "ERROR: Can't find path: " + path
            sys.exit(-1)

        if not os.access(path, os.W_OK):
            print "ERROR: " + path + " is not writable."
            sys.exit(-1)

        if args.destination is not None:
            if not os.path.isdir(args.destination):
                print "ERROR: Can't find destination path: " + path
                sys.exit(-1)

            if not os.access(args.destination, os.W_OK):
                print "ERROR: " + args.destination + " is not writable."
                sys.exit(-1)
            destination_path = os.path.abspath(args.destination) + '/'

        size = {
            'mdpi': args.filename + '.',
            'drawable-mdpi': args.filename + '.',
            'drawable-ldrtl-mdpi': args.filename + '-ldrtl.',
            'hdpi': args.filename + '@1.5x.',
            'drawable-hdpi': args.filename + '@1.5x.',
            'drawable-ldrtl-hdpi': args.filename + '-ldrtl@1.5x.',
            'xhdpi': args.filename + '@2x.',
            'drawable-xhdpi': args.filename + '@2x.',
            'drawable-ldrtl-xhdpi': args.filename + '-ldrtl@2x.',
            'xxhdpi': args.filename + '@3x.',
            'drawable-xxhdpi': args.filename + '@3x.',
            'drawable-ldrtl-xxhdpi': args.filename + '-ldrtl@3x.',
            'xxxhdpi': args.filename + '@4x.',
            'drawable-xxxhdpi': args.filename + '@4x.',
            'drawable-ldrtl-xxxhdpi': args.filename + '-ldrtl@4x.'
        }

        print 'We are looking the directory from: ' + path  # Selected path
        print 'We are gonna put the files in this location: ' + destination_path  # Selected destination

        for directory in os.listdir(path):
            if directory[0] == '.' or directory not in size:
                continue
            print directory  # Current directory
            print size[directory]
            for asset in os.listdir(path + directory):
                name = asset.split('.')
                os.rename(path + directory + '/' + asset,
                          destination_path + size[directory] + name[1])
        sys.exit(0)  # Everything run OK
