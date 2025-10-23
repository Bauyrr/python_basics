
import os

path = '/Users/bauyrzanbakytzan/Desktop/python_basics /lab6'
os.chdir(path)

print("Directories:", [item for item in os.listdir() if os.path.isdir(item)])
print("Files:", [item for item in os.listdir() if os.path.isfile(item)])
print("All dir and files:", os.listdir())



