
import shutil, os

def SaveStorage(folder):

    for foldername, subfolders, filenames in os.walk(folder):
        if (os.path.getsize(foldername)/1000000) > 100:
            print('Deleting...'+ os.path.abspath(foldername))
        for subfolder in subfolders:
            if (os.path.getsize(os.path.join(foldername, subfolder))/1000000) > 100:
                print('Deleting...'+ os.path.abspath(subfolder))
            for filename in filenames:
                if (os.path.getsize(os.path.join(foldername, filename))/1000000) > 100:
                    print('Deleting...'+ os.path.abspath(filename))

SaveStorage('C:\\Riot Games')