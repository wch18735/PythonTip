# First-Class Function
# A programming language is said to have first-class functions if it treats functions as first-class citizens.

# First-Class Citizen:
# a first-class citizen (also type, object, entity, or value) in a given programming language is an entity which supports all the operations generally available to other entities.

# So, functions are able to be treated as a normal variables
def square(x):
    return x * x

# assign function to a variable
f = square(5)

print(square)   # <function square at 0x000001E0DE577160>
print(f)        # 25

# parentheses "()" mean just that execute function
# example of function treated as function
f = square
print(f(5))

# Higher order function
# - functions that take functions as a arguments
# - functions that return functions as a results
# great example is a map

def my_map(func, arg_list):
    result = []
    for i in  arg_list:
        result.append(func(i))
    return result

# square is passed to my_map as a argument
squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)

# example of return a function: logger
# exactly act just like logger
def logger(msg):
    def log_message():
        print("Log:", msg)

    return log_message

log_hi = logger("HI!")
log_hi() # parenthese mean executing function

# using this property, function is able to be just reusable
def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    return wrap_text

print_h1 = html_tag('h1')
print_h1('headline one')
print_p = html_tag('p')
print_p('paragraph')