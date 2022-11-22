import time


def test_speed(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        print("Complite. Duration: " + str(round(time.time() - start_time, 2)) + " sec")

    return wrapper


@test_speed
def long_loop_print(loops_count=1000):
    for x in range(loops_count):
        print(x)


@test_speed
def pause(pause_sec=1):
    print("Pausing for " + str(pause_sec) + " seconds")
    time.sleep(pause_sec)


long_loop_print(50000)
pause(3)
