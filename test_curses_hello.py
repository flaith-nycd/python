# from os import system
import curses

myscreen = curses.initscr()

myscreen.border(0)
myscreen.addstr(5, 5, "HELLO WORLD")
input = myscreen.getstr(12, 20, 50)
# system("cat /proc/iomem")
myscreen.refresh()
myscreen.getch()

curses.endwin()
