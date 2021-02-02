# If we want to reflect one change of variable in class to other variables, we use setter, getter and deleter
class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    # To reflect change of variable (self.first and self.last)
    # define variables depending on these variable and use @property to declare it is property, not function
    # and @property is called getter
    @property
    def email(self):
        return '{}{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # To set property, use property name and dot setter
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # To use 'del' keyword, define deleter
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee('Jhon', 'Smith', 5000)
# emp_1.first = 'Jim'
# emp_1.fullname = 'Corey Schafer' : Error before setter doesn't exist
emp_1.fullname = 'Corey Schafer'

print(emp_1.first)  # Changed
print(emp_1.email)  # Changed
print(emp_1.fullname) # Chagned

# deleter works!!
del emp_1.fullname