from functools import wraps


def deco_with_args(type):
    def inner_deco(func):

        pass

@deco_with_args(str)
def print_five_times(*args, **kwargs):
    for i in range(5):
        print(args)


print_five_times("lskdjf")
