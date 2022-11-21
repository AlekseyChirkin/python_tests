def decorator_func(orig_func):
    def wrap_my_func():
        print('additional code before')
        orig_func()
        print('additional code after')
    return wrap_my_func

@decorator_func
def my_func():
    print('my function run')


my_func()

