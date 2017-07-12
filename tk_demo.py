#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

fenetre = Tk()

# mettez ici tout le code dont vous avez besoin

Label(fenetre, text="Essai fenêtre").pack(pady=20, padx=10)

Button(fenetre, text="Quitter", command=fenetre.destroy).pack(pady=5)

# /!\ n'oubliez pas de finir avec la boucle principale /!\

fenetre.mainloop()
