def count_down(from_num):
    from_num = from_num
    while from_num >= 0:
        yield from_num
        from_num -= 1


print([x for x in count_down(10)])

c = count_down(99)
print(c.__next__())
print(next(c))
print(c.__next__())
print(next(c))

week = {
    1: 'monday',
    2: 'tuesday',
    3: 'wednesday',
    4: 'thursday',
    5: 'friday',
    6: 'saturday',
    7: 'sunday'
}


def day_of_week():
    day = 1
    while day < 8:
        yield week[day]
        day += 1


ddd = day_of_week()
print(ddd.__next__())
print(next(ddd))
for d in ddd:
    print(d, end=' ')