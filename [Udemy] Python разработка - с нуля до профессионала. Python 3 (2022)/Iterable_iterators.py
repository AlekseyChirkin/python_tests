def my_print_iterator(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(f'[{next(iterator)}]', end='')
        except StopIteration:
            print('\nIteration printed correct')
            break


s = 'Hi, bitches'
iter_s = iter(s)

print('\nPrint by loop:')
for i in range(len(s)):
    print(iter_s.__next__(), end='')

print('\nPrint by function:')
my_print_iterator(s)
my_print_iterator('Ку-ку, ёпта!')
my_print_iterator([range(0, 100, 4)])
my_print_iterator([2, 6, 9, 'd', 1.3, 'c'])
