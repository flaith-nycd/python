# -*- coding:utf-8 -*-
class Application:
    def __init__(self):
        self.root = Tk()
        self.root.title('Tirage de dés')
        self.root.geometry("600x400")
        self.c = Canvas(self.root)
        self.c.pack(fill=BOTH, expand=YES)
        self.unite = 8  # unite servant à dimensionner les dés
        self.trait = 1  # épaisseur en pixels du bord du dé
        self.dessiner(10, 10, 6)
        self.dessiner(10 + 13 * self.unite, 10, 5)
        self.dessiner(10 + 26 * self.unite, 10, 4)
        self.dessiner(10, 10 + 13 * self.unite, 3)
        self.dessiner(10 + 13 * self.unite, 10 + 13 * self.unite, 2)
        self.dessiner(10 + 26 * self.unite, 10 + 13 * self.unite, 1)
        self.root.mainloop()

    def dessiner(self, x, y, num):
        # on trace d'abord le carré de la face du dé
        self.c.create_rectangle(x, y, x + (10 * self.unite),
                                y + (10 * self.unite), fill='white', width=self.trait)
        # voici les coordonnées en "unités" des différents points de chaque face de dé
        cdpn = (
            ((4, 4),),
            ((1, 1), (7, 7)),
            ((1, 7), (4, 4), (7, 1)),
            ((1, 1), (7, 1), (1, 7), (7, 7)),
            ((1, 1), (7, 1), (1, 7), (7, 7), (4, 4)),
            ((2, 1), (6, 1), (2, 4), (6, 4), (2, 7), (6, 7))
        )
        for p in cdpn[num - 1]:
            self.c.create_oval(x + (p[0] * self.unite),
                               y + (p[1] * self.unite),
                               x + ((p[0] + 2) * self.unite),
                               y + ((p[1] + 2) * self.unite), fill='black')


# départ du programme principal :
from tkinter import *

f = Application()
