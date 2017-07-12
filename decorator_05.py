def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result


a = 5
print(operate(inc, a))
print(operate(dec, a))


def calculate(a, b):
    def get_first(val):
        return val

    def get_second(val):
        return val

    return get_first(a) + get_second(b)


print(calculate(3, 2))


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner


def ordinary():
    print("I am ordinary")


ordinary()
print()

# make_pretty() is a decorator. In the assignment step.
pretty = make_pretty(ordinary)
pretty()
print()

# Generally, we decorate a function and reassign it as,
ordinary = make_pretty(ordinary)
ordinary()
print()


# We can use the @ symbol along with the name of the decorator function and place it above the
# definition of the function to be decorated. For example,
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


# is equivalent to
"""
def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)
"""

ordinary()
print()
