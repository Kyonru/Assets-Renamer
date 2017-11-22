# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import os

path = sys.argv[1] # /some/path/to/file/
filename = sys.argv[2] # foo
size = {
        'drawable-mdpi': filename + '.',
        'drawable-hdpi': filename + '@1.5x.',
        'drawable-xhdpi': filename + '@2x.',
        'drawable-xxhdpi': filename + '@3x.',
        'drawable-xxxhdpi': filename + '@4x.'
        }

print(path)
for directory in os.listdir(path):
    if directory[0] == '.':
	continue
    print (directory)    # Current directory
    print(size[directory])
    for file in os.listdir(path+directory):
        name = file.split('.')
        os.rename(path+directory+'/'+file, path+size[directory]+name[1])
#for filename in glob.glob(os.path.join(path, '*.txt')):
            
