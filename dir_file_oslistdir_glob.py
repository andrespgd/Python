import os
import random
import glob
# 1 - create a directory
dir_path = r'c:\tmp100'

if not os.path.exists(dir_path):
    os.mkdir(dir_path)


# 2 - create bunch of random files
list = []
for i in range(100):
    fname = 'file_data_' + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + '.txt'
    list.append(fname)

os.chdir(dir_path)
for i in range(len(list)):
    open(list[i], 'a').close()
    
    
# 3A - search for a list of files using LISTDIR - just the filenames
files1 = os.listdir(dir_path)
files2 = [i for i in files1 if (i.endswith('.txt') and '3' in i)]


# 3B - search for a list of files using GLOB - the whole path and filename
files3 = glob.glob(dir_path + '\*3*.txt')
