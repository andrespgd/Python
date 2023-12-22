## Install a package inside environment
python -m pip install

## Raw Strings: 
* use when there is a **space** in a path
* start with r' or r"
* treat backslashes \ as literal characters
* no escaping is performed
* what you see is what you get
```
r'C:\Users\John\My Documents'
r"C:\Program Files (x86)\WinRar\Rar.exe"
```

## Unicode
```
print("here is your checkmark: " + u'\u2713')
```
Will print:
```
$ python test.py
here is your checkmark: ✓
```

## Sorting
* .sort() function  makes changes inplace  AND for case insensitive use: .sort(key=str.lower)
* sorted() function creates a new sequence AND for case insensitive use: sorted_list = sorted(unsorted_list, key=str.casefold)
```
list1 = ['B','a']
print(list1)
list1.sort()
print(list1)
list1.sort(key=str.lower)
print(list1)
```
will return:
```
['B', 'a']
['B', 'a']
['a', 'B']
```


## Function Clarity
use keywoard arguments. Kwargs help understanding the code. Instead of:
```
twitter_search('@trump', False, 20, True)
```
Use:
```
twitter_search('@trump', retweets=False, numtweets=20, popular=True)
```

## Dictionaries
for Python3 (same as iteritems in python2.7)
```
for k, v in d.items():
    print(k, '-->>', v)
```
to get the keys and values as lists:
```
d.keys()
d.values()
```


## Simultaneous State Updates (Just like Excel)
Instead of:
```
tmp_x = x + dx * t
tmp_y = y + dy * t
tmp_dx = influence(m, x, y ,dx, dy, partial='x')
tmp_dy = influence(m, x, y ,dx, dy, partial='y')
x = tmp_x
y = tmp_y
dx = tmp_dx
dy = tmp_dy
```
Use this format (just like you would in Excel):
```
x, y, dx, dy = (x + dx * t,
                y + dy * t,
                influence(m, x, y ,dx, dy, partial='x'),
                influence(m, x, y ,dx, dy, partial='y'))
```


## SYS ARGs
* the elements of argv are strings
* Python expect arguments separated by spaces
* they're not parsed like literals in the program
* sys.argv[0] is the fname of the Python file
* if you want to pass comma separated arguments, you should just pass a comma-separated string (without the brackets)
```
python3 test.py 1,2,3,4,5 0
```
and then use split() to convert it to an array.
```
import sys
arr = sys.argv[1].split(',')
print(argv[2])
```
If there is a space (such as in a path), the argument needs to start/end with double-quotes(")
```
python program.py "D:\Users\John\Desktop\Folder Name" 100
```
The args above will be 3: program.py, the path, AND 100

## SHUTIL
* copy2() method in Python is used to copy the content of source file to destination file or directory
* identical to shutil. copy() method 
* but it also try to preserves the file's metadata

## OS
* getcwd()
* chdir()
https://levelup.gitconnected.com/10-python-os-module-functions-that-you-should-know-a320aba36c87
* OS.System VS. SUBPROCESS
```
command='ls -l'
os.system(command)
```
VS.
```
proc= subprocess.Popen(command, shell=True, std=subprocess.PIPE)
print('the command is', proc.args)
proc.wait()
print(proc.returncode)
```

## SKLEARN
* sklearn fit and transform - μ and σ
https://datascience.stackexchange.com/questions/12321/difference-between-fit-and-fit-transform-in-scikit-learn-models 

* sklearn's transform's fit() just calculates the parameters 
* and saves them as an internal objects state.
* afterwards, you can call its transform() method to apply the transformation to a particular set of examples.
* fit_transform() joins these two steps and is used for the initial fitting of parameters on the training set xx, 
* but it also returns a transformed x′
* internally, it just calls first fit() and then transform() on the same data.

## MATPLOTLIB
For NO block plots use:
```
plt.show(block=True)
plt.pause(1.0)
plt.close()
```

# PANDAS DataFrame
## Bitwise Operators for Pandas
https://towardsdatascience.com/bitwise-operators-and-chaining-comparisons-in-pandas-d3a559487525
## ILOC causes warnings
instead of using df.iloc use: df.index.isin([0,2,3])
## Create categorical values
```
df['school_level'] = pd.Categorical(df['school_level'], categories=['elem','middle','high'], ordered=True]
```
## Column with 0s and 1s as integers: convert to 2 categories
```
df['on_or_off'] = df['on_or_off'].astype('category')
```
# Sort values on the fly
```
df.sort_values(by=['gender','age','height'], inplace=True)
```

## DATACLASS
- similar to C++ Struct
- easily work with classes that act as data containers
    - can do methods, but DON'T use them, keep it simple
- less code to define a class
- support for default values
```
from dataclasses import dataclass
@dataclass
class Vehicle:
    n_wheels: int
    mass:     float
    brand:    str
```
- easy conversion to a tuple or a dictionary
- frozen instances / immutable objects
    - prevent anyone from modifying the values of the attributes once the object is instantiated
```
@dataclass(frozen=True)
class Person:
     first_name: str = "John"
     last_name: str = "Smith"
     age: int = 40
     job: str = "Engineer"
 ```
 - No need to write comparison methods


## MySQL sqlalchemy
```
engine = sqlalchemy.create_engine('mysql+pymysql://username:password@localhost:3306/db_name')

query = '''
SELECT * FROM table_name
'''
df = pd.read_sql_query(query, engine)
print(df)
```
* There is a way to wrap/check query with sqlalchemy function, use:
* You can only do 1 query at a time with this method!!!!
    * for example you CANNOT do: SELECT * blah blah ; SELECT * blah blah.....; etc
