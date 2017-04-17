'''
Decorator example:

see: https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Decorators

'''

## E.g.

def decorate(func):
    def wrapper(*args, **kwargs): #signature generic so it can decorate anything
        print('you have been decorater')
        func(*args, **kwargs)
    return wrapper

def print_the_following(x,k=3):
    for i in range(k):
        print('i = ',i,x)
print_the_following = decorate(print_the_following)
print_the_following('brando',k=3)

@decorate
def print_the_following(x,k=3):
    for i in range(k):
        print('i = ',i,x)
print_the_following('brando',k=3)

## E.g.

def debug(func):
    '''
    goal: decorate func with useful debugging print statements.

    returns a function that can be called the same way as the original func
    but with the wrapper according to debug.
    '''
    def wrapper(*args, **kwargs):
        print("Before call")
        result = func(*args, **kwargs)
        print("After call")
        return result
    return wrapper

# without decorator
debugged_hello = debug(hello)
debugged_hello('brando')


# with decorator
@debug
def hello(x):
    print('hello', x)
debugged_hello('brando')

### E.g.

def viking_chorus(func_to_decorate):
    '''
    decorates func_to_decorate with a viking chorus.
    '''
    def viking_chorus_wrapper(*args, **kwargs):
        '''
        wrapper for the original function.

        note: *args and **kwargs help it receive any type of input arguments,
        wether they are keyed or not.
        '''
        print('VIKING CHORUS!!') # decoration
        func_to_decorate(*args, **kwargs) # calls original function
    return viking_chorus_wrapper # returns the decorated original function

def menu_item():
    print("spam")
menu_item = viking_chorus(menu_item) # this is what decoration does
menu_item()

@viking_chorus
def menu_item():
    print("spam")
menu_item()
