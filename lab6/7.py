import os
import shutil

def copy(f1, f2):
    if os.path.isfile(f1):
        shutil.copyfile(f1, f2)
        print('copied')
    else:
        print('file doesnt exists')
    
f1 = '/Users/bauyrzanbakytzan/Desktop/python_basics /lab6/copy.txt'
f2 = '/Users/bauyrzanbakytzan/Desktop/python_basics /lab6/copy2.txt '
copy(f1, f2)