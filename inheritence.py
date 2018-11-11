class Employee:
    num_of_emp = 0
    raise_amount = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emp +=1

    def fullname(self):
        return  '{} {}'.format(self.first,self.last) 

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)

class Developer(Employee):

    raise_amt = 1.10
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self,first,last,pay,employees = None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname())



dev1 = Employee('gary','Huda',5000)
dev2 = Developer('Sanju','Baba',5500,'Java')

manager1 = Manager('Sue','Smith',9000,[dev1,])

print(dev1.fullname())
print(dev2.fullname())
print('-----------------------------')
manager1.print_emps()
manager1.add_emp(dev2)
manager1.print_emps()
manager1.remove_emp(dev1)
manager1.print_emps()