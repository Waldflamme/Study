from functools import reduce

students = [
    {"name": "Александр", "age": 22, "grades": [4, 5, 3, 4]},
    {"name": "Дмитрий", "age": 19, "grades": [3, 3, 2, 4]},
    {"name": "Евгения", "age": 21, "grades": [5, 5, 5, 5]},
    {"name": "Александр", "age": 22, "grades": [4, 5, 3, 4]},
    {"name": "Ольга", "age": 22, "grades": [5, 3, 5, 3]}
]

names_upper = list(map(lambda x: x["name"].upper(), students))
print(names_upper)


older_than_20 = list(filter(lambda x: x["age"] > 20, students))
print(older_than_20)

all_grades = reduce(lambda ls, x: ls + x["grades"], students, [])
av_grade = sum(all_grades) / len(all_grades)
print(round(av_grade, 2))