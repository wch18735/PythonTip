# Difference between regular method, class method and static method
# regular method in class automatically pass an instance as an first argument, self
# similarly, class method pass an class as an first argument, cls
# static method don't pass anything automatically, anything
# so,
# regular method control variables in class (self.something)
# class method control class variables
# static method act just like regular method with an little connection to class itself

class Employee:
    raise_amt = 1.04
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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        # built in function weekday()
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Won', "CH", 45000)
emp_2 = Employee('Kim', "JH", 45000)

# classmethod experiment
# if classmethod executed, instances by the class are affected
print('before classmethod:', emp_1.raise_amt)
print('before classmethod:', emp_2.raise_amt)
Employee.set_raise_amt(1.05)
print('after classmethod:', emp_1.raise_amt)
print('after classmethod:', emp_2.raise_amt)

# When is the classmethod used in??
# If someone want to use some class constantly using a class variables but
# in specific situation, want to change the class variable, classmethod would be useful
# plus, if classmethod don't use any cls, it doesn't have to be used decorator @classmethod

# Another example
# create and return class in classmethod
emp_str_1 = 'John-Doe-70000'
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
# Realworld example
# datetime!!

# staticmethod example
import datetime
my_date = datetime.date(2020, 11, 21)
print(Employee.is_workday(my_date))