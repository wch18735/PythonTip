# Difference between class variables and instance variable
class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        # self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Won', "CH", 45000)
emp_2 = Employee('Kim', "JH", 45000)
print(Employee.num_of_emps)

# Possible to access class variable
# If there are not class variable, they find it from inherited class next
print(emp_1.__dict__) # Doesn't have an raise_amount
print(Employee.__dict__) # Does have raise_amount

# so if emp_1.raise_amount change the value, other classes are not applied this value
# Sub-class can override a new number
