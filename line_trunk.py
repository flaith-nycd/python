txt = '""""Fibonacci sequences using generators....This program is part of "Dive Into Python", a free Python book for..experienced programmers.  Visit http://diveintopython.org/ for the..latest version..."""....__author__ = "Mark Pilgrim (mark@diveintopython.org)"..__version__ = "$Revision: 1.2 $"..__date__ = "$Date: 2004/05/05 21:57:19 $"..__copyright__ = "Copyright (c) 2004 Mark Pilgrim"..__license__ = "Python"......def fibonacci(max):..    a, b = 0, 1..    while a < max:..        yield a..        a, b = b, a + b......for n in fibonacci(1000):..    print(n, )..'
hex = '80AAA28080A0000480A000348085D400'


def chunkstring(string, length):
    return (string[0 + i:length + i] for i in range(0, len(string), length))

def chunkhexa(string, sep=" "):
    return sep.join(a+b for a,b in zip(string[::2], string[1::2]))

for chunk in chunkstring(txt, 16):
    print(chunk)

print(chunkhexa(hex))
# chunks, chunk_size = len(txt), 16
# print([txt[i:i + chunk_size] for i in range(0, chunks, chunk_size)])
