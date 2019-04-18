#-*- coding: utf-8 -*-
import pickle

from SauvegardeEtLoad import *
from Classes import *
from Visualisation import * 
from FonctionImportante import *
from tkinter import *
from functools import *
from Initialisation import *
import time
from threading import Thread

fenetre = Tk()
l = list()
l
def test():
    nom_obj = entry_1.get()
    try:
        not Button(fenetre,image=eval(nom_obj))
        print("il n'y a pas de bouton, creation encours...")
        button_2 = Button(fenetre, image=key)
        button_2.grid(row=1, column=2)
    except NameError:
        print("il y a déjà un bouton !")

key = PhotoImage(file='image/Casque_WazukiIV.png')
button_3 = Button(fenetre, image=key)
button_3.grid(row=4, column=4)
entry_1 = Entry(fenetre)
button_1 = Button(fenetre, text="valider", borderwidth=1, command=partial(test)).grid(row=3, column=2)
entry_1.grid(row=2, column=2)
fenetre.mainloop()
