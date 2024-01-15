import pathlib


print('\n\nCREATE PATHS - Can be paths or files')
print('--------------------------------------')

p0 = pathlib.Path.cwd()

p1 = pathlib.Path(r'C:\Users\a1\file.txt')

p2 = pathlib.Path.home() / 'python' / 'scripts' / 'test.py'

p3 = pathlib.Path.home().joinpath('python', 'scripts', 'test.py')

print(p0)
print(p1)
print(p2)
print(p3)
print()
print(p1.is_file())
print(p1.is_dir())
print(p1.exists())



print('\n\nREADING FILES')
print('-------------')

path = pathlib.Path.cwd() / 'pathlib1_test.txt'
path.read_text()
# OR
pathlib.Path('pathlib1_test.txt').read_text()
print(pathlib.Path('pathlib1_test.txt').is_file())
print()

for one_line in path.open():
    print(one_line, end='')

print('\n')
print(path.stat().st_size, 'size in bytes')



print('\n\nCONFIRM PATH')
print('-------------')

path = pathlib.Path('pathlib1_test.txt')

print(path.resolve())

path.resolve().parent == pathlib.Path.cwd()

print(path.resolve().parent == pathlib.Path.cwd())



print('\n\nPATH COMPONENTS')
print('-------------')

path = pathlib.Path('pathlib1_test.txt')
print(path)
print(path.name)
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
print(path.parent.parent)
print(path.anchor)



print('\n\nDISPLAY DIRECTORY TREE')
print('-------------')

def print_tree(dir):
    print(f'+ {dir}')
    for path in sorted(dir.rglob('*')):
        depth = len(path.relative_to(dir).parts)
        spacer = '    ' * depth
        print(f'{spacer}+ {path.name}')
        
print_tree(pathlib.Path.cwd())



print('\n\nPATH COMPONENTS')
print('-------------')

p = pathlib.Path('.')
p.iterdir()

import glob
glob.glob('*.py')
#
glob.glob('**/*.py')
#
Path.cwd().rglob('MyCamelCase.exe').resolve()

p.glob('*.py')
for one_item in p.glob('*.py'):
    print(f"{one_item}: {type(one_item)}")

    
    

print('\n\nFIND ALL FILES OF a KIND')
print('-------------')

top_level_csv_files = Path.cwd().glob('*.txt')
all_csv_files = Path.cwd().rglob('*.txt')

for i in all_csv_files:
    print(i)



full_text = path.read_text()

full_text_lines = full_text.splitlines()


path.exists() 
path.is_dir()
path.is_file()



