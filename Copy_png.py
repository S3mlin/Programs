#Copy_png.py - Copies all files with a png extention to a new folder

import shutil, os

def CopyPng(folder):

    folder = os.path.abspath(folder)

    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith('.jpg'):
                print('Copying file...'+ filename)
                shutil.copy(os.path.join(foldername, filename), 'C:\\PngCopies')
    print('Done.')
CopyPng('C:\\delicious')        