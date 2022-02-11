import pdfplumber
import pathlib
import pandas as pd
import re

folder = r'c:\folder1\'
file_out1 = 'out1.txt'
file_out2 = 'out2.csv'

# 1- Read .PDFs ----> .TXT
folder_path = pathlib.Path(folder)
with open(file_out1, 'a') as out_file:
     # find PDFS        
     for file in folder_path.glob('*.pdf'):
            # open PDFs
            with pdfplumber.open(file) as pdf:
                # extract text 
                for page in pdf.pages:
                    text = page.extract_text()
                    out_file.write(text)

# 2- Read .TXT ----> LINES    
with open(file_out1,'r') as f:
    lines_kept = []
    for line in f:
        if line.startswith(('text1','text2')):
            # replace strings
            line_edit1 = line.replace('this text','that text')
            # remove empty lines with 1 comma
            line_edit2 = re.sub(' +', ',', line_edit1)
            lines_kept.append(line_edit2)

# 3- LINES ----> .CSV
with open(file_out2, 'w') as f:
    for item in lines_kept:
        f.write(item)
        
# 4- .CSV ----> DF
df1 = pd.read_csv(file_out2, header=None)
df2 = df1.copy()
df2.drop_duplicates(inplace=True)

