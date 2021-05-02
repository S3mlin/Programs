#shows content of a specified folder in os.walk()
import os

for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('Subfolder of ' + folderName + ': ' + subfolder)
    
    for filename in filenames:
        print('File inside ' + folderName + ': ' + filename)
    print('')