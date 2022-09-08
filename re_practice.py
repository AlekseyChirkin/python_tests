import  re

file_name = 'Tasks/txt/textForTask_5.txt'

with open(file_name, 'r', encoding='utf8') as in_file:
    line = in_file.read()

    r = re.compile(r'пис')
    print(re.search(r, str))
