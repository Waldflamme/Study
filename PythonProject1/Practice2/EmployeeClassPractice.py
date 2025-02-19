class Employee():

    def __init__(self, name, surname, job_title, salary):
        self.name = name
        self.surname = surname
        self.job_title = job_title
        self.salary = salary

    def Info(self):
        return f'Name: {self.name} Surname: {self.surname} Job title: {self.job_title} Salary: {self.salary}'

    def MoreThanBase(self):
        return 'More than base' if self.salary>100000 else 'Less than base'

    @property
    def JobExp(self):
        if self.salary<100000:
            return 'Less than a year'
        elif self.salary<20000:
            return '2 years'
        else:
            return 'More than 5 years'

emp1 = Employee('john','Smith', 'CEO', 300000)
emp2 = Employee('Lora','Palmer', 'CFO', 150000)
emp3 = Employee('Jack','Jackson', 'Office Worker', 50000)
print(f'{emp1.Info()} {emp1.MoreThanBase()} {emp1.JobExp}')
print(f'{emp2.Info()} {emp2.MoreThanBase()} {emp2.JobExp}')
print(f'{emp3.Info()} {emp3.MoreThanBase()} {emp3.JobExp}')