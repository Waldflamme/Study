class Person():
    def __init__(self,name,gender,age=20):
        self.name = name
        self.gender = gender
        self.age = age
person1 = Person('Ivan','male',23)
person2 = Person('Peter','male')
print(person1.name,person1.gender,person1.age)
print(person2.name,person2.gender,person2.age)