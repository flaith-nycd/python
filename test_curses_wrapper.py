"""
A common problem when debugging a curses application is to get your terminal messed up when the application dies 
without restoring the terminal to its previous state. In Python this commonly happens when your code is buggy 
and raises an uncaught exception. 
Keys are no longer echoed to the screen when you type them, for example, which makes using the shell difficult.

In Python you can avoid these complications and make debugging much easier by importing the curses.wrapper() function 
and using it like this:
"""
from curses import wrapper


def main(stdscr):
    # Clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 11):
        v = i - 10
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10 / v))

    stdscr.refresh()
    stdscr.getkey()


wrapper(main)
