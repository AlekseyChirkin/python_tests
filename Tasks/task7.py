# Дан список студентов. Элемент списка содержит фамилию, имя, отчество, год рождения, курс, номер группы,
# оценки по пяти предметам. Упорядочите студентов по курсу, причем чтобы студенты одного курса располагались в
# алфавитном порядке. Найдите средний балл каждой группы по каждому предмету. Определите самого старшего студента и
# самого младшего студента. Для каждой группы найдите лучшего с точки зрения успеваемости студента.

class Student:

    def __init__(self, name: str, year_of_birth: int, year: int, group: int, grade1: int, grade2: int, grade3: int,
                 grade4: int, grade5: int):
        self.name = name
        self.year_of_birth = year_of_birth
        self.year = year
        self.group = group
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3
        self.grade4 = grade4
        self.grade5 = grade5

    pass


file_name = 'txt/students.txt'
students_list = []

with open(file_name, encoding='utf8') as file:
    lines = file.readlines()

for line in lines:
    data_of_student = line.split()
    student = Student(
        data_of_student[0] + ' ' + data_of_student[1] + ' ' + data_of_student[2],
        int(data_of_student[3]),
        int(data_of_student[4]),
        int(data_of_student[5]),
        int(data_of_student[6]),
        int(data_of_student[7]),
        int(data_of_student[8]),
        int(data_of_student[9]),
        int(data_of_student[10]))
    students_list.append(student)



