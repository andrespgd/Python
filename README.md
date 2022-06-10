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


Looping over a dictionary keys and values .Simplest way (inefficient):
```
for k in d:
    print(k, '-->', d[k])
```
If using this way it has to re-hash the dictionary in every iteration:
```
for k, v in d.items():
    print(k, '-->>', v)
```
If  using this form, it stays in memory:
```
for k, v in d.iteritems():
    print(k, '-->', v)
```
<br /><br />


Simultaneous state updates<br />
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
<br /><br />


Functors use in Python:
https://www.geeksforgeeks.org/functors-use-python/




# PANDAS
## Bitwise Operators for Pandas
https://towardsdatascience.com/bitwise-operators-and-chaining-comparisons-in-pandas-d3a559487525
