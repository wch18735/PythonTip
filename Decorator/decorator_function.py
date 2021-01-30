# closure example
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)
    return inner_function

# function depends on msg passed in (closure)
hi_func = outer_function('Hi')
bye_func = outer_function('Bye')
hi_func()
bye_func()

# Decorators
# Function that takes another function as an argument and some kind of functionality and then return a function
# All of this without altering the source code of the original function passed in
# Why?
# We are easily able to add some functionality
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__)) # add printing functionality
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print('display function ran')

# @decorator_function
# def display():
#     print('display function ran')
# means just display = decorator_function(display)
# yes!! just wrapping @ means "wrap function declared below and assign to the same name variable"
display()

@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25)
# If developer want to apply decorator to both: *args, **kwargs (arguments and keyword arguments)