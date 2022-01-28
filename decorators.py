
# A decorator acts as a wrapper for the function that is being decorated
# -takes in a function
# -adds some functionality 
# -and returns it

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi)
print(decorate())

# 'uppercase_decorator' is the name of the decorator
# 'wrapper' is the name of the inner function
#     -which is actually only used in this decorator definition
# 'say_hi' is the function that is being decorated

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())

# Now, everytime we call say_hi()
# -instead of returning 'hello there'
# -will return 'HELLO THERE' every time