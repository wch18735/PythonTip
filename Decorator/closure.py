# A closure is a record storing a function together with an environment. 
# The environment is a mapping associating each free variable of the function 
# (variables that are used locally, but defined in an enclosing scope) with the value 
# or reference to which the name was bound when the closure was created. 
# Unlike a plain function, a closure allows the function to access those captured variables 
# through the closure's copies of their values or references, even when the function is invoked outside their scope.

def outer_func():
    message = "Hi"

    def inner_func():
        print(message)

    return inner_func # without executing 

my_func = outer_func() # my_func is actually same as inner_func
print(my_func.__name__) # inner_func
my_func()

# so in simple terms
# a closure is an inner function that remembers and has access to variables in the local scope in which it was created
# even after the outer function has finished excuting

# example: closure close over a free varable, which is message in this example
def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func # without executing 

hi_func = outer_func('Hi')
hello_func = outer_func('Hello')
hi_func()
hello_func()

# exmample in logging
import logging
logging.basicConfig(filename='./Decorator/example.log', level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

add_logger = logger(add)
sub_logger = logger(sub)
add_logger(3, 3)
sub_logger(4, 5)