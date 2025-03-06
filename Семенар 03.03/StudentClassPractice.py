class Student(object):

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def info(self):
        pass

    def student_age_check(self):
        if self.age <= 20:
            return 'This is bachelor'
        else:
            return 'This is master or graduate student'

class Bachelor(Student):

    def __init__(self, name, surname, age, course):
        super().__init__(name, surname, age)
        self.course = course

    def info(self):
        return (f'Name: {self.name} Surname: {self.surname}'
                f' Age: {self.age} Course: {self.course}')

    def student_search_name(self, name):
        if self.name == name:
            print(f'Info on student: {self.info()}')
        else:
            pass

    def student_search_age(self, age):
        if self.age == age:
            print(f'Info on student: {self.info()}')
        else:
            pass

class Master(Student):

    def __init__(self, name, surname, age, spec):
        super().__init__(name, surname, age)
        self.spec = spec

    def info(self):
        return (f'Name: {self.name} Surname: {self.surname} '
                f'Age: {self.age} Specialization: {self.spec}')

    def student_search_name(self, name):
        if self.name == name:
            print(f'Info on student: {self.info()}')
        else:
            pass

    def student_search_age(self, age):
        if self.age == age:
            print(f'Info on student: {self.info()}')
        else:
            pass


class GraduateStudent(Student):

    def __init__(self, name, surname, age, dis_theme):
        super().__init__(name, surname, age)
        self.dis_theme = dis_theme

    def info(self):
        return (f'Name: {self.name} surname: {self.surname}'
                f' Age: {self.age} Dissertation theme: {self.dis_theme}')


    def student_search_name(self, name):
        if self.name == name:
            print(f'Info on student: {self.info()}')
        else:
            pass

    def student_search_age(self, age):
        if self.age == age:
            print(f'Info on student: {self.info()}')
        else:
            pass

prod1 = Bachelor('John', 'Whitkowich', 19, 2)
prod2 = Master('Mary', 'Bell', 24, 'Arts')
prod3 = GraduateStudent('Bill', 'Harris', 27, 'Society in AI epoch')

Student_list = [prod1, prod2, prod3]

def base_output(lst):
    for i in lst:
        print(i.info(), i.student_age_check())

def student_list_search_name(lst):
    name = input('Enter student name: ')
    for i in lst:
        i.student_search_name(name)

def student_list_search_age(lst):
    age = int(input('Enter student age: '))
    for i in lst:
        i.student_search_age(age)

base_output(Student_list)
student_list_search_name(Student_list)
student_list_search_age(Student_list)