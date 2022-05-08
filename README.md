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
