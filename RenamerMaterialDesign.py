# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
#path = '/some/path/to/file'
path = str(input('Escriba el path de la carpeta del icono'))
size = {
        'drawable-mdpi': '.',
        'drawable-hdpi': '@1.5x.',
        'drawable-xhdpi': '@2x.',
        'drawable-xxhdpi': '@3x.',
        'drawable-xxxhdpi': '@4x.'
        }

path = path.split("'")
path = ''.join(path)
path += '/'
for directory in os.listdir(path):
    print (directory)    # do your stuff
    print(size[directory])
    for file in os.listdir(path+directory):
        name = file.split('.')
        os.rename(path+directory+'/'+file, path+name[0][:-11]+size[directory]+name[1])
#for filename in glob.glob(os.path.join(path, '*.txt')):
            
