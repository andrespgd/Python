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