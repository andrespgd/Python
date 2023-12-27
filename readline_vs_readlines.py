

with open('readline_vs_readlines.txt') as file:
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline() 
    lines = file.read()
    
with open('readline_vs_readlines.txt') as file:  
    lines5 = file.readlines()

with open('readline_vs_readlines.txt') as file:  
    lines6 = file.read()

import pathlib
p = pathlib.Path('readline_vs_readlines.txt')
lines7 = p.read_text(encoding='UTF-8' )
lines7separated = lines7.splitlines()
