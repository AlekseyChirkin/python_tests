# Дан список студентов. Элемент списка содержит фамилию, имя, отчество, год рождения, курс, номер группы,
# оценки по пяти предметам. Упорядочите студентов по курсу, причем чтобы студенты одного курса располагались в
# алфавитном порядке. Найдите средний балл каждой группы по каждому предмету. Определите самого старшего студента и
# самого младшего студента. Для каждой группы найдите лучшего с точки зрения успеваемости студента.

import sys
import Student


def sort_students(students_list_for_sort):
    # сортируем студентов по курсу и внутри курса по алфавиту
    sorted_students = []
    for i in range(1, 6):

        students_this_year = []
        for st in students_list_for_sort:
            if st.year == i:
                students_this_year.append(st)

        students_this_year = sorted(students_this_year, key=lambda stu: stu.name)
        for j in students_this_year:
            sorted_students.append(j)
    return sorted_students


def print_average_grade_by_group(students):
    for ye in range(1, 6):
        for gr in range(1, 11):
            count_of_students_in_group = 0
            average_grade_in_group = 0
            for s in students:
                if s.year == ye and s.group == gr:
                    average_grade_in_group += (s.grade1 + s.grade2 + s.grade3 + s.grade4 + s.grade5) / 5
                    count_of_students_in_group += 1
            if count_of_students_in_group != 0:
                average_grade_in_group = average_grade_in_group / count_of_students_in_group
                print(f'Средняя оценка в группе номер {gr}, {ye} курса, составила {average_grade_in_group} баллов')

    pass


file_name = 'txt/students20.txt'
students_list = []

# читаем из файла
try:
    with open(file_name, encoding='utf8') as file:
        lines = file.readlines()
except FileNotFoundError:
    print('Ошибка: файл не найден')
    sys.exit()

# создаем список объектов класса Student с данными из файла
for line in lines:
    data_of_student = line.split()
    student = Student.Student(
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

sorted_students_list = sort_students(students_list)

# Выводим список студентов с именами, курсом, группой и годом рождения
for st in sorted_students_list:
    print(f'{st.name}, {st.year_of_birth} года рождения, {st.year} курс, {st.group} группа')

print_average_grade_by_group(students_list)



