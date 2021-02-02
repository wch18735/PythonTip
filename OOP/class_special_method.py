# special method: allows us to emulate some built-in behavior within Python and
# it's also how we implement operator overloading
# surrounded with double underscores -> Dunder

class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    def __repr__(self):
        return "Employtee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        # how we want to add this Employee
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 5000)
emp_2 = Employee('Test', 'Employee', 6000)

print(emp_1.__repr__()) # print(repr(emp1))
print(emp_1.__str__()) # print(str(emp1))

# similarly, add operator act like that
print(1 + 1)
print(int.__add__(1, 1))

# __add__ in Employee
print(emp_1 + emp_2)

# __len__ method
print(len(emp_1))

# discriminating line
print("=" * 50)
# What is difference between str() and repr()?
# The goal of __repr__ is to be unambiguous: representation is helpful for developer to catch what type or value are
# The goal of __str__ is to be readable: User-friendly version of that
a = [1, 2, 3, 4]
b = 'sample string'

print(str(a))
print(repr(a))
print(str(b))
print(repr(b))