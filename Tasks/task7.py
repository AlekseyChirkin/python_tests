# Дан список студентов. Элемент списка содержит фамилию, имя, отчество, год рождения, курс, номер группы,
# оценки по пяти предметам. Упорядочите студентов по курсу, причем чтобы студенты одного курса располагались в
# алфавитном порядке. Найдите средний балл каждой группы по каждому предмету. Определите самого старшего студента и
# самого младшего студента. Для каждой группы найдите лучшего с точки зрения успеваемости студента.

import sys
import Student

content = ''

file_name = 'txt/students.txt'
output_file_name = 'txt/task7_report.txt'
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


def sort_students(students_list_for_sort):
    # сортируем студентов по курсу и внутри курса по алфавиту
    sorted_students = []
    for i in range(1, 6):
        students_this_year = []
        for stu in students_list_for_sort:
            if stu.year == i:
                students_this_year.append(stu)

        students_this_year = sorted(students_this_year, key=lambda stud: stud.name)
        for j in students_this_year:
            sorted_students.append(j)
    return sorted_students


def print_average_grade_by_group(students):
    cont = ''
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
                cont += f'Средняя оценка в группе номер {gr}, {ye} курса, составила {average_grade_in_group} баллов\n'
    return cont


def print_oldest_students(data_students):
    cont = ''

    oldest = data_students[0].year_of_birth
    for stu in data_students:
        if oldest > stu.year_of_birth:
            oldest = stu.year_of_birth
    for stu in data_students:
        if oldest == stu.year_of_birth:
            print(f'Старший студент среди всех: {stu.name}, {stu.year_of_birth} года рождения')
            cont += f'Старший студент среди всех: {stu.name}, {stu.year_of_birth} года рождения\n'
    return cont


def print_young_students(data_students):
    cont = ''

    youngest = data_students[0].year_of_birth
    for stu in data_students:
        if youngest < stu.year_of_birth:
            youngest = stu.year_of_birth
    for stu in data_students:
        if youngest == stu.year_of_birth:
            print(f'Самый младший студент среди всех: {stu.name}, {stu.year_of_birth} года рождения')
            cont += f'Самый младший студент среди всех: {stu.name}, {stu.year_of_birth} года рождения\n'
    return cont


def print_best_student_in_group(data_students):
    cont = ''

    for ye in range(1, 6):
        for gr in range(1, 11):
            best_average_grade_in_group = 0
            for s in data_students:
                if s.year == ye and s.group == gr:
                    average_grade = (s.grade1 + s.grade2 + s.grade3 + s.grade4 + s.grade5) / 5
                    if average_grade > best_average_grade_in_group:
                        best_average_grade_in_group = average_grade
            for s in data_students:
                if s.year == ye and s.group == gr:
                    average_grade = (s.grade1 + s.grade2 + s.grade3 + s.grade4 + s.grade5) / 5
                    if average_grade == best_average_grade_in_group:
                        print(f'Лидер по успеваемости в {s.group} группе,'
                              f'{s.year} курса: {s.name}, средний балл {best_average_grade_in_group}')
                        cont += (f'Лидер по успеваемости в {s.group} группе,'
                                 f'{s.year} курса: {s.name}, средний балл {best_average_grade_in_group}\n')
    return cont


sorted_students_list = sort_students(students_list)

# Выводим список студентов с именами, курсом, группой и годом рождения
for st in sorted_students_list:
    content += f'{st.name}, {st.year_of_birth} года рождения, {st.year} курс, {st.group} группа\n'
    print(f'{st.name}, {st.year_of_birth} года рождения, {st.year} курс, {st.group} группа')

content += print_average_grade_by_group(students_list)

# Выводим старых студентов
content += print_oldest_students(sorted_students_list)

# Выводим самых молодых студентов
content += print_young_students(sorted_students_list)

# Ищем лучшего по успеваемости студента в группе
content += print_best_student_in_group(sorted_students_list)

with open(output_file_name, 'w', encoding='utf8') as output_file:
    output_file.write(content.strip())
