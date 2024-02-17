

# “Old Style” String Formatting

fname = 'Bob'
lname = 'Smith'
print()
s1a = 'Hello, %s !' % fname
print(s1a)
s1b = 'Hello, %s %s !' % (fname, lname)
print(s1b)

#######################################################

# “New Style” String Formatting

fname = 'Bob'
lname = 'Smith'
print()
s2a = 'Hello, {} !'.format(fname)
print(s2a)
s2b = 'Hello, {} {} !'.format(fname, lname)
print(s2b)

#######################################################

# f-Strings (Python 3.6+)
print()
s3a = f'Hello, {fname} !'
print(s3a)
s3b = f'Hello, {fname} {lname} !'
print(s3b)

# f-strings for numbers

n = 12345.6789
print(f'{n:.1f}') #12345.7
print(f'{n:.0f}') #12346
print(f'{n:,.0f}') #12,346

# f-string keep expresion
a=5
b=7
print(f'{a+b=}') # a+b=12
print(f'{a+b}')  # 12
#
today_is_monday = False
print(f'{bool(today_is_monday) = }')  #bool(today_is_monday) = False

# f-string separators
n = 100000000000
print(f'{n:_}') #100_000_000_000
print(f'{n:,}') #100,000,000,000
#
n = 100000000000.312341234
print(f'{n:_}') #100_000_000_000.31235

# f-string spaces
my_str = 'var'
print(f'{my_str:>20}')  #                 var
# fill element _
print(f'{my_str:_>20}') #_________________var

#f-strings datetime
import datetime
now = datetime.datetime.now()
print(f'{now:%d.%m.%y}') # 17.02.24
print(f'{now:%Y-%m-%d}') # 2024-02-17
print(f'{now:%c}')       # Sat Feb 17 15:44:38 2024
