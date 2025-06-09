class Student:
    def __init__(self, fullname, grades):
        self.fullname = fullname
        self.grades = grades
        self.average = sum(grades) / len(grades)

    def __str__(self):
        return f"{self.fullname} | Средний балл: {self.average:.2f}"

def read_students_from_file(filename):
    students = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or 'Оценки' in line:
                continue
            try:
                parts = line.split(';')
                name = parts[0]
                grades = list(map(int, parts[1].split(',')))
                students.append(Student(name, grades))
            except (IndexError, ValueError) as e:
                print(f"Строка пропущена из-за ошибки: {line} — {e}")
    return students

def selection_sort(students):
    n = len(students)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if students[j].average < students[min_index].average:
                min_index = j
        students[i], students[min_index] = students[min_index], students[i]
    return students

def bubble_sort(students):
    n = len(students)
    for i in range(n):
        for j in range(0, n - i - 1):
            if students[j].average > students[j + 1].average:
                students[j], students[j + 1] = students[j + 1], students[j]
    return students

def print_students(students):
    for student in students:
        print(student)

if __name__ == "__main__":
    students = read_students_from_file("students.txt")

    print("Сортировка выбором:")
    sorted_by_selection = selection_sort(students.copy())
    print_students(sorted_by_selection)

    print("\nСортировка пузырьком:")
    sorted_by_bubble = bubble_sort(students.copy())
    print_students(sorted_by_bubble)