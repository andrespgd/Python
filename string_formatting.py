fname = 'Bob'
lname = 'Smith'

# “Old Style” String Formatting
print()
s1a = 'Hello, %s !' % fname
print(s1a)
s1b = 'Hello, %s %s !' % (fname, lname)
print(s1b)


# “New Style” String Formatting
print()
s2a = 'Hello, {} !'.format(fname)
print(s2a)
s2b = 'Hello, {} {} !'.format(fname, lname)
print(s2b)


# f-Strings (Python 3.6+)
print()
s3a = f'Hello, {fname} !'
print(s3a)
s3b = f'Hello, {fname} {lname} !'
print(s3b)
