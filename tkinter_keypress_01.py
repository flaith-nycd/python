from tkinter import *


def foo(event):
    global m

    key = event.char
    if key.upper() == 'P':
        c.move(a1, 0, 5)
        c.itemconfig(a1, fill='yellow')
    elif key.upper() == 'H':
        c.move(a1, 0, -5)
        c.itemconfig(a1, fill='blue')
    elif key.upper() == 'K':
        c.move(a1, -5, 0)
        c.itemconfig(a1, fill='white')
    elif key.upper() == 'M':
        c.move(a1, 5, 0)
        c.itemconfig(a1, fill='green')
    elif key == '\x1b':
        root.destroy()
    c.after_cancel(m)
    m = c.after(1000, move)


def move():
    c.move(a1, 0, 2)
    m = c.after(1000, move)


root = Tk()
c = Canvas(root, height=900, width=700)
c.pack()
p0 = (450, 450)
p1 = (460, 460)
a1 = c.create_oval(p0, p1, fill='red')
m = root.after(1000, move)
root.bind('<Key>', foo)
root.mainloop()
