

with open('readline_vs_readlines.txt') as file:
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline() 
    lines = file.read()
    
with open('readline_vs_readlines.txt') as file:  
    lines2 = file.readlines()

with open('readline_vs_readlines.txt') as file:  
    lines3 = file.read()

import pathlib
p = 'readline_vs_readlines.txt'
p.read_text(encoding='UTF-8' )
