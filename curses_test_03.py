# https://docs.python.org/3.6/library/curses.html
import curses

stdscr = curses.initscr()

# Clear and refresh the screen for a blank canvas
stdscr.clear()
stdscr.refresh()

curses.flash()
curses.delay_output(250)
curses.flash()
curses.delay_output(250)

print('curses.baudrates() =', curses.baudrate())

print('curses.can_change_color() ?', curses.can_change_color())
print('curses.has_color() ?', curses.has_colors())
if curses.can_change_color() and curses.has_colors():
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # print('2 Flashes happened')
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(10, 20, '2 Flashes happened')
    stdscr.attroff(curses.color_pair(1))
    # Refresh the screen
    stdscr.refresh()
    print()
    print()
    print('curses.color_content(1) =', curses.color_content(1))
    print('curses.color_pair(1) =', curses.color_pair(1))

# Set the virtual screen cursor to y, x. If y and x are both -1, then leaveok is set.
curses.setsyx(-1, -1)
# Return the current coordinates of the virtual screen cursor in y and x.
# If leaveok is currently true, then -1,-1 is returned.
print('curses.getsyx() =', curses.getsyx())

# curses.endwin()
