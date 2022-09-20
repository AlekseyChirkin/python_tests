s = 'kuku, yopta, blyat'

print(s)

k = [n for n in s]
print(k)

n = [*s]
print(n)

number_list = [num * 2 for num in range(10)]
print(number_list)

number_list = [num * num for num in range(10)]
print(number_list)

number_list = [-(num * 2) * (num - 1) for num in range(1, 10)]
print(number_list)

number_list = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, -4, -12, -24, -40, -60, -84, -112, -144]
print(number_list)

new_list2 = ['+' if n > 0 else '-' for n in number_list]
print(new_list2)

new_list_with_if = [n * 2 for n in number_list if 10 > n // 2 > -10]
print(new_list_with_if)

# 021

number_dict = {
    'first': 1,
    'second': 2,
    'third': 3,
    'forth': 4,
    'fifth': 5
}

print(number_dict)
new_number_dict = {k: value * 2 for k, value in number_dict.items()}
print(new_number_dict)

dict_from_list = {n: 'positive' if n > 0 else 'negative' if n < 0 else 'zero' for n in new_list_with_if}
print(dict_from_list)
