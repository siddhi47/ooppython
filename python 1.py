class Employee:
    num_of_emp = 0
    raise_amount = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emp +=1

    def fullname(self):
        return '{} {}'.format(self.first,self.last) 

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)
    
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount
    ''''''
    @classmethod
    def from_string(cls,emp_str):
        '''
        alternate constructor from the string!
        '''
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)
    @staticmethod
    def is_workday(day):
        if day.weekday()==6 or day.weekday()==5:
            return False
        return True

emp1 = Employee('siddi','bajracharya',15000)

print(emp1.fullname(),emp1.pay)
emp1.apply_raise()
print(emp1.fullname(),emp1.pay)
#print(Employee.fullname(emp1))

new_emp_str = 'siddhi-kiran-1995'
new_emp =Employee.from_string(new_emp_str)
print(new_emp.fullname(),new_emp.pay)

import datetime
my_date = datetime.date(2016,7,16)
print(Employee.is_workday(my_date))