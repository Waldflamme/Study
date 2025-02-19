class Person():
    name = ''
    age = 20
t1 = Person()
t2 = Person()
t1.name = 'Ivan'
t2.name = 'Peter'
t1.age = 23
print(type(t1),type(t2))
print(t1)
print(t2)
print(t1==t2)
print(t1.name)
print(t2.name)
print(t1.age)
print(t2.age)