import time
from collections import Counter
from functools import wraps


def test_speed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Complite. Duration: {round(end_time - start_time, 2)} sec")
        return result
    return wrapper


@test_speed
def long_loop_print(loops_count=1000):
    for x in range(loops_count):
        print(x)


@test_speed
def pause(pause_sec=1):
    time.sleep(pause_sec)


@test_speed
def list_sum(list_in):
    return sum(list_in)


# long_loop_print(50000)
# pause(1)
n = 10000000

print(list_sum((x for x in range(n))))
print(list_sum([x for x in range(n)]))

start_time = time.time()
print(f'Sum of {n} (by list) is      {sum([n for n in range(n)])}, time spend: {time.time() - start_time}')

start_time = time.time()
print(f'Sum of {n} (by generator) is {sum(n for n in range(n))}, time spend: {time.time() - start_time}')


print('*' * 60)
nums = [x for x in range(n)]
print(list_sum([v for v, c in Counter(nums).items() if not c-1]))
print(list_sum(v for v, c in Counter(nums).items() if not c-1))

