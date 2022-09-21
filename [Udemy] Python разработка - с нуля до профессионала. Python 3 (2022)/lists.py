number_list = [332, 656, 84, 848.5]
print(number_list)

some_list = [1000, 999.99, 'hi', [1, 2]]
print(f'list: {some_list}, length = {len(some_list)}, second element: {some_list[1]}')
print(f'slice list from start to 2: {some_list[:2]}')

new_list = some_list + number_list
print(new_list)

new_list.append('new item')
print(new_list)

new_list.insert(3, 'inserted element')
print(new_list)

new_list.pop()
print(new_list)

removed_elem = new_list.pop(-3)
print(new_list)
print(removed_elem)

new_list.remove(999.99)
print(new_list)

abc_list = ['a', 'lskajf', 'alsk', 'dkfj']

print(abc_list)
print(number_list)
abc_list.sort()
number_list.sort()
print(abc_list)
print(number_list)

print()
phrase1 = 'А Роза упала на лапу Азора'
letter_list_from_phrase1 = list(phrase1.lower())
for lett in letter_list_from_phrase1:
    if lett == ' ':
        letter_list_from_phrase1.remove(lett)
print(letter_list_from_phrase1)

letter_list_from_phrase1.reverse()
print(letter_list_from_phrase1)
