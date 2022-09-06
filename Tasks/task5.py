# В файле содержится совокупность текстовых строк. Изменить первую букву каждого слова на заглавную.
# Заменить все цифры соответствующими словами.

fileName = 'txt/textForTask_5.txt'
capitalizedEveryWordText = ''
allNumsAsWordsText = ''

with open(fileName, encoding='utf8') as file:
    lines = file.readlines()

lines = str(lines).split(' ')
for word in lines:
    capitalizedEveryWordText += word.capitalize() + ' '

for char in capitalizedEveryWordText:
    if char == '0':
        char = ' Ноль'
    if char == '1':
        char = 'Один '
    if char == '2':
        char = ' Два'
    if char == '3':
        char = ' Три'
    if char == '4':
        char = ' Четыре'
    if char == '5':
        char = ' Пять'
    if char == '6':
        char = ' Шесть'
    if char == '7':
        char = ' Семь'
    if char == '8':
        char = ' Восемь'
    if char == '9':
        char = ' Девять'

    allNumsAsWordsText += char

for i in range(0, 3):
    allNumsAsWordsText.replace('  ', ' ')

print(allNumsAsWordsText)
