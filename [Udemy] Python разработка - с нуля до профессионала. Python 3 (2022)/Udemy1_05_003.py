def ten_percent_of_product(x, y, z):
    return (x * y * z) * 0.1


def ten_percent_of_product_with_args(percent, *args):
    p = 1
    for i1 in args:
        p = p * i1
    return p / 100 * percent


def func_with_kwargs(**kwargs):
    print(kwargs)


print(ten_percent_of_product(10, 20, 3))
print(ten_percent_of_product_with_args(10, 20, 3, 321, 10, 15))

func_with_kwargs(f=10, s=10, t=100, fo=50)


# 004


def sum_of_two(x):
    return x + x


number_list = [x for x in range(1, 11)]
print(number_list)

summ = 0
for i in number_list:
    summ = summ + i
print(summ)

print(list(map(sum_of_two, number_list)))

print('*' * 100)


def is_number_odd(number):
    return number % 2 == 1


print(list(filter(is_number_odd, number_list)))

print('*' * 100)

# Lambda

s = 'lkasdjf;lajsdf;lasdf'
string_bullshit = [*s]

print(list(map(lambda x: x ** 3, number_list)))
print(list(map(lambda x: x * 2, string_bullshit)))

from random import shuffle
from random import randint

shuffle(string_bullshit)
sas = list(map(lambda x: x * randint(1, 5), string_bullshit))
print(list(filter(lambda x: len(x) > 2, sas)))
