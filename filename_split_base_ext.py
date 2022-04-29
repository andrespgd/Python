import os
import sys

# this file filename
fname = os.path.basename(sys.argv[0])
print(fname)

# basename
base=os.path.splitext(fname)[0]
print(base)

# extension
ext=os.path.splitext(fname)[1]
print(ext)



import pathlib

file = r'C:\tmp\untitled0.py'
file_pathlib = pathlib.Path(file)

# folder path
folder_names = file_pathlib.parent

# basename
file_without_extension = file_pathlib.stem

# extension
file_extension = file_pathlib.suffix
