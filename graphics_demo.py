from graphics import *


def main():
    win = GraphWin("My Circle", 400, 100)
    c = Circle(Point(50, 50), 10)
    c.draw(win)
    win.plot(11, 10)
    win.plot(10, 11)
    win.plot(10, 12)
    win.plot(10, 13)
    win.plot(10, 14)
    win.getMouse()  # pause for click in window
    win.close()


main()
