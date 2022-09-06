# Пользователь вводит три числа. Найти сумму тех чисел, которые делятся на 5. Если таких чисел нет, то вывести error

firstNum = input("Введите первое число: ")
secondNum = input("Введите второе число: ")
thirdNum = input("Введите третье число: ")

summa = 0
if (int(firstNum) % 5) == 0:
    summa += int(firstNum)

if (int(secondNum) % 5) == 0:
    summa += int(secondNum)

if (int(thirdNum) % 5) == 0:
    summa += int(thirdNum)

if summa != 0:
    print("Сумма чисел, делящихся нацело на 5, равна: ", summa)
else:
    print("error!")
