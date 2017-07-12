from PIL import Image, ImageTk
import random
import tkinter

CHOICES = [
    'Yes',
    'No',
    'Ask again later',
    'Maybe?',
    'Bees?',
    'OMG CLOWNS!',
    'Eh, 50/50'
]


class App():
    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.pack()

        image = Image.open('crystal_ball.png')
        photo = ImageTk.PhotoImage(image)

        self.answer_text = tkinter.StringVar()
        self.crystal_ball = tkinter.Label(frame, image=photo)
        self.answer = tkinter.Label(frame, font=("Helvetica", 16),
                                    textvariable=self.answer_text)
        self.crystal_ball.image = photo
        self.crystal_ball.pack()
        self.answer.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        self.quit_button = tkinter.Button(frame, text='QUIT',
                                          command=frame.quit)
        self.quit_button.pack(side=tkinter.RIGHT)

        self.ask_button = tkinter.Button(frame, text='ASK',
                                         command=self.get_answer)
        self.ask_button.pack(side=tkinter.LEFT)

    def get_answer(self):
        self.answer_text.set(random.choice(CHOICES))


root = tkinter.Tk()
app = App(root)
root.mainloop()
root.destroy()
