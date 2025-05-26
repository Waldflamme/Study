class PatientList:
    def __init__(self, first_name, last_name, diagnosis, admission_date, discharge_date, procedures, medications):
        self.first_name = first_name
        self.last_name = last_name
        self.diagnosis = diagnosis
        self.admission_date = admission_date  # строка или datetime
        self.discharge_date = discharge_date  # строка или datetime
        self.procedures = procedures          # список строк
        self.medications = medications        # список строк

        self.prev = None
        self.next = None

class PatientLs:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_patient(self, first_name, last_name, diagnosis, admission_date, discharge_date, procedures, medications):
        new_node = PatientList(first_name, last_name, diagnosis, admission_date, discharge_date, procedures, medications)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display_patients(self):
        current = self.head
        while current:
            print(f"Пациент: {current.first_name} {current.last_name}")
            print(f"Диагноз: {current.diagnosis}")
            print(f"Поступление: {current.admission_date}, Выписка: {current.discharge_date}")
            print(f"Процедуры: {', '.join(current.procedures)}")
            print(f"Лекарства: {', '.join(current.medications)}")
            print("-" * 40)
            current = current.next

patients = PatientLs()
patients.add_patient(
    "Иван", "Петров", "Пневмония", "2025-05-10", "2025-05-20",
    ["рентген", "анализ крови", "ИВЛ"],
    ["Азитромицин", "Парацетамол"]
)

patients.add_patient(
    "Мария", "Иванова", "Мигрень", "2025-05-15", "2025-05-17",
    ["МРТ головы"],
    ["Ибупрофен", "Суматриптан"]
)

patients.display_patients()