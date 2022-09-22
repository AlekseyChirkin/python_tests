from random import randint

n = randint(1, 10)
nums = [*range(randint(-20, 0), randint(1, 20), 1)]
res = []

for i in nums:
    num_for_find = n - i
    if num_for_find and num_for_find != i in nums:
        res = [i, num_for_find]
        break

print(f'Для числа n = {n} в последовательности {nums}, результат: {res}')
