
file_name = r'readline_vs_readlines.txt'

with open(file_name) as file:
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline() 
    lines = file.read()
    
with open(file_name) as file:  
    lines5 = file.readlines()

with open(file_name) as file:  
    lines6 = file.read()

import pathlib
p = pathlib.Path(file_name)
lines7 = p.read_text(encoding='UTF-8' )
lines7separated = lines7.splitlines()
