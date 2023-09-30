class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id

    def __repr__(self) -> str:
        return f"Student name: {self.name}, Student class: {self.current_class}, Student id: {self.id}"


class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f"Teacher: {self.name}, Subject: {self.subject}, Id: {self.id}"


class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            return f"Not sufficiant amount"
        else:
            id = len(self.students) + 1
            student = Student(name, 9, id)
            self.students.append(student)
        return f"{name} with id: {id} is enrolled successfully"

    def __repr__(self) -> str:
        print("Welcome to", self.name)
        print("----------Out Teachers----------")
        for teacher in self.teachers:
            print(teacher)
        print("----------Out Students----------")
        for student in self.students:
            print(student)
        return f"This is the representation of {self.name}"


# alia = Student("Alia Torkari", 9, 2)
# print(alia)
# jafor = Teacher("SHAR", "Biggan", 69)
# print(jafor)

phitron = School("Phitron")
phitron.enroll("Alia", 6500)
phitron.enroll("Aisharia", 7000)
phitron.enroll("Ranbeeer", 8300)
phitron.enroll("Sallu", 9000)

phitron.add_teacher("Tom Cruise", "ALGO")
phitron.add_teacher("Decap", "DS")
phitron.add_teacher("AJ", "DB")

print(phitron)
