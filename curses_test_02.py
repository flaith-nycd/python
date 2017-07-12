#!/usr/bin/env python

import curses
import curses.textpad

stdscr = curses.initscr()

curses.noecho()
# curses.echo()

begin_x = 20
begin_y = 7
height = 5
width = 40
win = curses.newwin(height, width, begin_y, begin_x)
tb = curses.textpad.Textbox(win)
text = tb.edit()
win.addstr(4, 1, text.encode('utf_8'))
