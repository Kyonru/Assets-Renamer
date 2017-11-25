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
    parser.add_argument("-d", "--destination", help="Asset new path", required=False,
                        dest="destination")
    args = parser.parse_args()

    if args.path and args.filename:

        path = os.path.abspath(args.path) + '/'

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
            destinationPath = os.path.abspath(args.destination) + '/'
        else:
            destinationPath = os.getcwd() + '/'
        size = {
            'drawable-mdpi': args.filename + '.',
            'drawable-hdpi': args.filename + '@1.5x.',
            'drawable-xhdpi': args.filename + '@2x.',
            'drawable-xxhdpi': args.filename + '@3x.',
            'drawable-xxxhdpi': args.filename + '@4x.'
        }

        print 'We are looking the directory from: ' + path  # Selected path
        print 'We are gonna put the files in this location: ' + destinationPath  # Selected destination

        for directory in os.listdir(path):
            if directory[0] == '.' or "drawable" not in directory:
                continue
            print directory  # Current directory
            print size[directory]
            for asset in os.listdir(path + directory):
                name = asset.split('.')
                os.rename(path + directory + '/' + asset,
                          destinationPath + size[directory] + name[1])
        sys.exit(0)  # Everything run OK
