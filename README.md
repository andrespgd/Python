Literal Strings: 

-are surrounded by single quotes

-no escaping is performed

-what you see is what you get

-Examples

```
r'C:\tmp\'
```


SORTING
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


Instead of zip instead of izip. Stays in memory ( faster for long lists):
```
izip(list1, list2)
```
<br /><br />


Always clarify functions with keywoard arguments. Kwargs help understanding the code. Instead of:
```
twitter_search('@trump', False, 20, True)
```
Use:
```
twitter_search('@trump', retweets=False, numtweets=20, popular=True)
```
<br /><br />


## Dictionary
Looping over keys and values .Simplest way (inefficient):
```
for k in d:
    print(k, '-->', d[k])
```
Use this for Python3 (same as iteritems in python2.7)
```
for k, v in d.items():
    print(k, '-->>', v)
```
<br /><br />


## Simultaneous state updates
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


Functors use in Python:
https://www.geeksforgeeks.org/functors-use-python/


# ARGs
The elements of argv are strings, they're not parsed like literals in the program.

You should just pass a comma-separated string (without the brackets):
```
python3 test.py 1,2,3,4,5 0
```
and then use split() to convert it to an array.
```
import sys
arr = sys.argv[1].split(',')
print(arr[2])
```

# SHUTIL
copy2() method in Python is used to copy the content of source file to destination file or directory. This method is identical to shutil. copy() method but it also try to preserves the file's metadata

# OS
getcwd()
chdir()

https://levelup.gitconnected.com/10-python-os-module-functions-that-you-should-know-a320aba36c87



# NUMPY
https://www.dataquest.io/blog/numpy-cheat-sheet/

# SKLEARN
sklearn fit and transform - μ and σ
https://datascience.stackexchange.com/questions/12321/difference-between-fit-and-fit-transform-in-scikit-learn-models 

very sklearn's transform's fit() just calculates the parameters (e.g. μμ and σσ in case of StandardScaler) and saves them as an internal objects state.

Afterwards, you can call its transform() method to apply the transformation to a particular set of examples.

fit_transform() joins these two steps and is used for the initial fitting of parameters on the training set xx, but it also returns a transformed x′

x′. Internally, it just calls first fit() and then transform() on the same data.

# MATPLOTLIB
## No block plots
Use:
```
plt.show(block=True)
plt.pause(1.0)
plt.close()
```

# PANDAS
## Bitwise Operators for Pandas
https://towardsdatascience.com/bitwise-operators-and-chaining-comparisons-in-pandas-d3a559487525
## ILOC causes warnings
instead of using df.iloc , use df[df.isin(list_of_rows)]
## Create categorical values
```
df['school_level'] = pd.Categorical(df['school_level'], categories=['elem','middle','high'], ordered=True]
```
# Sort values on the fly
```
df.sort_values(by=['gender','age','height'], inplace=True)
```

# OS.System VS. SUBPROCESS
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

# DATACLASS
Can be used in place of a C++ Struct
```
from dataclasses import dataclass
@dataclass
class Vehicle:
    n_wheels: int
    mass:     float
    brand:    str
```
https://realpython.com/python-data-classes/



# OTHER

SMOP to translate Matlab- > Python

