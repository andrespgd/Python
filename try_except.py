# USES of TRY/EXCEPT

param = 10.0
try:
    param2 = param1 * 2
except NameError:
    param2 = 10.0
    print('no param1 was found, param2 set to default of 10.0 \n')
    
    
filename = 'test.csv'
try:
    file1 = open(filename, 'r')
    lines = file1.readlines()
    file1.close()
except FileNotFoundError:
    lines = []
    print('no file was found \n')
    