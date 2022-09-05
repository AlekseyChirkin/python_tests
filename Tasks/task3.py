# Вывести квадрат 7 на 7 из случайных букв
import string
import random

for i in range(0, 7):
    stringLineOfCube = ''

    for j in range(0, 7):
        stringLineOfCube += random.choice(string.ascii_letters)
    print(stringLineOfCube)
