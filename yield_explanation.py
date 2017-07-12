"""
http://khmel.org/?p=1151
https://www.quora.com/What-does-the-%E2%80%9Cyield%E2%80%9D-keyword-do-in-Python
https://docs.python.org/3.6/library/itertools.html
"""

"""
Short explanation: Yield can pause a function and return current result.

So yield works almost as return in the function. How to get value and resume function? First way to get current value 
and resume function by for loop:
"""

print('--- Example #1')


def characters():
    yield 'a'  # pause the function and return result
    yield 'b'  # pause the function and return result
    yield 'c'  # pause the function and return result
    yield 'd'  # pause the function and return result
    yield 'e'  # pause the function and return result


for item in characters():  # get current value and resume function
    print(item)

"""
Second example how to continue paused function by next() method. next() method returns value as well:
"""

print('--- Example #2')


def characters():
    abc = ['a', 'b', 'c', 'd', 'e']
    for x in abc:
        yield x  # pause the function and return result


generator = characters()  # assign generator

print(next(generator))  # get current value and resume function
print(next(generator))  # get current value and resume function
print(next(generator))  # get current value and resume function

"""
Each next(generator) returns value and resume function until next yield.

Can you do the same without yield?
  Yes

Why I need yield?
* Another way to write simple and efficient code (no extra objects).
* Getting data from infinite loops.

Understanding of Iterators (https://wiki.python.org/moin/Iterator) and 
Generators (https://wiki.python.org/moin/Generators) is needed to understand how yield working.
"""

print('--- Example #3')

def f(val):
    return "Hi"


x = [1, 2, 3]
yield_list = list(f((yield a)) for a in x)
print(yield_list)  # [1, 'Hi', 2, 'Hi', 3, 'Hi']
