# Генерация файла с данными для задачи №7
import random

fileInputName = 'txt/names.txt'
fileOutputName = 'txt/students.txt'
content = ''

with open(fileInputName, encoding='utf8') as file:
    names = file.readlines()

for name in names:
    content += name.strip() + " "\
        + str(1990 + round(random.random() * 20)) + " "\
        + str(round(random.random() * 4) + 1) + " "\
        + str(round(random.random() * 9) + 1) + " "\
        + str(round(random.random() * 3) + 2) + " "\
        + str(round(random.random() * 3) + 2) + " "\
        + str(round(random.random() * 3) + 2) + " "\
        + str(round(random.random() * 3) + 2) + " "\
        + str(round(random.random() * 3) + 2) + "\n"
content = content.strip()

with open(fileOutputName, 'w', encoding='utf8') as file:
    file.write(content)
    print(f'The file "{file.name}" successfully created!')
