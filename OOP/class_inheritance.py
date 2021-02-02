# Reuse Employee class to make developer and manager class
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

# inherit by insert class that you want to do between brackets
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # Employee handles first, last, pay just like declared
        # Employee.__init__(self, first, last, pay) is same with that. Not to duplicate same process
        self.prog_lang = prog_lang

dev_1 = Developer('Corey', 'Schafer', 5000, 'Python')
dev_2 = Developer('Test', 'Employee', 6000, 'Java')

print(dev_1.email)
print(dev_2.email)
# If there are not init method in Developer, python automatically check their parent class

print(help(Developer))
# Method resolution order:
#  |      Developer
#  |      Employee
#  |      builtins.object

# raise amount change by subclass
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

# Subclasses with little bit of code are useful to init or some other things.
class Manager(Employee):
    # default None
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

mgr_1 = Manager('Sue', 'Smith', 9000, [dev_1])

# manager email
print(mgr_1.email)
print('-' * 10)

# managed employees
mgr_1.print_emps()
print('-' * 10)

# add
mgr_1.add_emp(dev_2)
mgr_1.print_emps()
print('-' * 10)

# remove
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()
print('-' * 10)

# built in function, isinstance and issubclass
print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Developer, Developer)) # same class show True
# print(issubclass(mgr_1, Employee)) : Error because mgr_1 is instance, not class
print(isinstance(mgr_1, Manager))

# Practical real-world module: Exception library