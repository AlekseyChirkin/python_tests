# В файле содержится совокупность текстовых строк. Изменить первую букву каждого слова на заглавную.
# Заменить все цифры соответствующими словами.

fileName = 'txt/textForTask_5.txt'
numbersAsWords = {
    '0': 'Ноль',
    '1': 'Один',
    '2': 'Два',
    '3': 'Три',
    '4': 'Четыре',
    '5': 'Пять',
    '6': 'Шесть',
    '7': 'Семь',
    '8': 'Восемь',
    '9': 'Девять'
}
contentResult = ''

with open(fileName, encoding='utf8') as file:
    lines = file.readlines()

lines = str(lines).title()

for char in lines:
    if char.isdigit():
        char = ' ' + numbersAsWords[char]
    contentResult += char

contentResult = contentResult.strip().replace('  ', ' ').replace('  ', ' ')
print(contentResult)
