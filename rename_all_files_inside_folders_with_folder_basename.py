import os

path = r'C:\udacity_data_analyst_nd\udacity_data_analyst_nd_LESSONS'

os.chdir(path)

# list of folders
folders = next(os.walk('.'))[1]

# renames files inside folder with same name as folder plus a number

for folder in folders:
    print(folder)
    print('--------------------')
    os.chdir(folder)
    files = os.listdir()
    for i, file in enumerate(files):
        print(file)
        print(folder+str(i).zfill(3)+'.PNG')
        os.rename(file, folder+str(i).zfill(3)+'.PNG')
    os.chdir('..')
    print('--------------------')
