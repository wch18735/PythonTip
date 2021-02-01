# Python Object-Oriented Programming

class Employee:
    # constructor
    def __init__(self, first, last, pay):
        # self is an instance of this class
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@company.com'

    def fullname(self):
        # an method in class automatically pass an instance argument
        # and that is self (instance of class itself)
        return '{} {}'.format(self.first, self.last)

# instance = class()
# instances are unique
emp_1 = Employee('won', 'ch', 500000)
emp_2 = Employee('jeon', 'dh', 5000000)

print(emp_1.email)
print(emp_1.fullname())

# self passed or not
print(emp_1.fullname()) # passed what self is -> emp_1
print(Employee.fullname(emp_1)) # passed nothing so we need to specify what instance is passed