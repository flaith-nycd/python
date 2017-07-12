from tkinter import Tk, Frame, Label, IntVar
from tkinter.ttk import Button
from functools import partial
from random import randint


# Onager Ornery Clicker v0.9
# 2016 Mickey Kocic
# Released for testing and review only. All rights reserved.

class Game:
    def __init__(self):
        self.window = Tk()
        self.window.title("Onager Ornery Clicker")
        self.createwidgets()

    def createframes(self):
        self.frame1 = Frame(self.window)
        self.frame2 = Frame(self.window)
        self.frame1.configure(bg='silver',
                              relief='raised', border='15')
        self.frame2.configure(bg='silver',
                              relief='raised', border='15')
        self.frame1.rowconfigure(6)
        self.frame1.columnconfigure(5)
        self.frame2.rowconfigure(15)
        self.frame2.columnconfigure(5)
        self.frame1.grid(row=0, column=0, rowspan=6,
                         columnspan=5)
        self.frame2.grid(row=6, column=0, rowspan=15,
                         columnspan=5)

    def createtitle(self):
        self.title = Label(self.frame1)
        self.title.configure(bg='silver', fg='SlateBlue4',
                             font='serif 30', justify='center',
                             padx='10', pady='10',
                             text='Onager Ornery Clicker')
        self.title.grid(row=0, column=0, rowspan=1,
                        columnspan=5)

    def createinstr(self):
        text1 = "Clicking on 'Click Me!' scores a point.\n"
        text2 = "Clicking on 'Don't Click Me!' costs a point.\n"
        text3 = "'Start' button starts timer, 'Stop' stops/clears it.\n"
        text4 = 'See how quickly you can get the high score\n'
        text5 = 'or how high a score you get in a set time.'
        textstr = text1 + text2 + text3 + text4 + text5

        self.instr = Label(self.frame1)
        self.instr.configure(bg='Silver', fg='SlateBlue4',
                             font='serif 12', justify='center',
                             text=textstr, pady='10',
                             padx='17')
        self.instr.grid(row=1, column=0, rowspan=5,
                        columnspan=1)

    def createstart(self):
        self.start = Button(self.frame1)
        self.start['text'] = 'Start'
        self.start['command'] = partial(self.start_game)
        self.start.grid(row=1, column=2, rowspan=1,
                        columnspan=1)

    def createstop(self):
        self.stop = Button(self.frame1)
        self.stop['text'] = 'Stop.'
        self.stop['command'] = partial(self.stop_game)
        self.stop.grid(row=1, column=3, rowspan=1,
                       columnspan=1)

    def createscore(self):
        self.score_label = Label(self.frame1)
        self.score_label.configure(fg='black',
                                   font='serif 10')
        self.score_label['text'] = 'Score:'
        self.score_label.grid(row=3, column=2, rowspan=1,
                              columnspan=1)
        self.score = Label(self.frame1)
        self.score.configure(bg='black', fg='white',
                             font='serif 16')
        self.score.grid(row=5, column=2, rowspan=1,
                        columnspan=1)

    def createtime(self):
        self.time_label = Label(self.frame1)
        self.time_label.configure(fg='black',
                                  font='serif 10')
        self.time_label['text'] = 'Time:'
        self.time_label.grid(row=3, column=3, rowspan=1,
                             columnspan=1)
        self.time = Label(self.frame1)
        self.time.configure(bg='black', fg='white',
                            font='seriv 16')
        self.time.grid(row=5, column=3, rowspan=1,
                       columnspan=1)

    def createbuttons(self):
        self.buttons = []
        for item in range(75):
            button = Button(self.frame2,
                            width=len("Don't Click Me!"))
            rownum, colnum = divmod(item, 5)
            button.grid(row=rownum, column=colnum,
                        rowspan=1, columnspan=1)
            button['command'] = partial(self.clicked, button)
            self.buttons.append(button)
        self.shuffle()

    def createwidgets(self):
        self.createframes()
        self.createtitle()
        self.createinstr()
        self.createstart()
        self.createstop()
        self.createscore()
        self.createtime()
        self.createbuttons()


class Play(Game):
    def __init__(self):
        Game.__init__(self)
        self.scorevar = IntVar()
        self.timevar = IntVar()
        self.score['textvariable'] = str(self.scorevar)
        self.time['textvariable'] = str(self.timevar)

    def clicked(self, button):
        if button['text'] == 'Click Me!':
            self.scorevar.set(self.scorevar.get() + 1)
        else:
            self.scorevar.set(self.scorevar.get() - 1)
        self.shuffle()

    def shuffle(self):
        for i, button in enumerate(self.buttons, 1):
            button['text'] = "Don't Click Me!!"
        index = randint(0, len(self.buttons))
        self.buttons[index]['text'] = 'Click Me!'

    def start_game(self):
        self.game_running = True
        self.update_time()

    def stop_game(self):
        if self.game_running == False:
            self.timevar.set(0)
            self.scorevar.set(0)
        self.game_running = False

    def update_time(self):
        if self.game_running:
            self.timevar.set(self.timevar.get() + 1)
            self.window.after(1000, self.update_time)


def main():
    onager = Play()
    onager.window.mainloop()


if __name__ == '__main__':
    main()
