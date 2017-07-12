from time import time, ctime

print('Python: Today is', ctime(time()))


def func(arg):
    return [ctime(time()), arg / 2, arg, arg * 2]


result = func(42)

print(result)