import pathlib

print('\nCREATE PATHS - Can be paths or files')
print('--------------------------------------')

p0 = pathlib.Path.cwd()

p1 = pathlib.Path(r'C:\Users\a1\file.txt')

p2 = pathlib.Path.home() / 'python' / 'scripts' / 'test.py'

p3 = pathlib.Path.home().joinpath('python', 'scripts', 'test.py')

print(p0)
print(p1)
print(p2)
print(p3)


print('\nREADING FILES')
print('-------------')

path = pathlib.Path.cwd() / 'pathlib1_test.txt'
path.read_text()

# OR

pathlib.Path('pathlib1_test.txt').read_text()


print('\nCONFIRM PATH')
print('-------------')

path = pathlib.Path('pathlib1_test.txt')

print(path.resolve())

path.resolve().parent == pathlib.Path.cwd()

print(path.resolve().parent == pathlib.Path.cwd())


print('\nPATH COMPONENTS')
print('-------------')

path = pathlib.Path('pathlib1_test.txt')
print(path)
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
print(path.parent.parent)
print(path.anchor)

print('\nDISPLAY DIRECTORY TREE')
print('-------------')

def print_tree(dir):
    print(f'+ {dir}')
    for path in sorted(dir.rglob('*')):
        depth = len(path.relative_to(dir).parts)
        spacer = '    ' * depth
        print(f'{spacer}+ {path.name}')
        
print_tree(pathlib.Path.cwd())