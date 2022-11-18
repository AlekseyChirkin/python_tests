import time
#
#
# def day_of_week_infinite():
#     week = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
#
#     day = 0
#     while True:
#         if day >= len(week):
#             day = 0
#         yield week[day]
#         day += 1
#
#
# ddd = day_of_week_infinite()
# print(ddd.__next__())
# print(next(ddd))
# for d in range(0, 10):
#     print(next(ddd))
#
# xxx = (x for x in range(100))
# for xx in xxx:
#     print(xx)

n = 50_000_000

start_time = time.time()
print(f'Sum of {n} (by list) is      {(sum([n for n in range(n)]))}, time spend: {time.time() - start_time}')

start_time = time.time()
print(f'Sum of {n} (by generator) is {(sum((n for n in range(n))))}, time spend: {time.time() - start_time}')


