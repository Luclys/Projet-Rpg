#-*- coding: utf-8 -*-
import pickle

from SauvegardeEtLoad import *
from Classes import *
from Visualisation import * 
from FonctionImportante import *
from tkinter import *
from functools import *
from Initialisation import *

#TEST MENU PRINCIPAL


fenetre = Tk()

#########Menu#########
def menu2jeu(frame):
    frame.tkraise()

    
menu = Frame(fenetre,borderwidth=2,relief=GROOVE, bg="red")
jeu = Frame(fenetre,borderwidth=2,relief=GROOVE, bg="green")
oui = Frame(fenetre,borderwidth=2,relief=GROOVE, bg="blue")
for frame in (menu, jeu, oui):
    frame.grid(row=0, column=0, sticky='news')

#boutons menu    
tojeu = Button(menu, text="Jouer", command=partial(menu2jeu, jeu))
tojeu.grid(column=1, row =2, padx=480, pady=300)

tooui = Button(menu, text="test", command=partial(menu2jeu, oui))
tooui.grid(column=2, row =3)

#boutons jeu
tomenu = Button(jeu, text="Retour au menu", command=partial(menu2jeu, menu))
tomenu.grid(column=1, row =2, padx=480, pady=300)

tooui = Button(jeu, text="test", command=partial(menu2jeu, oui))
tooui.grid(column=2, row =3)

#boutons oui 
tomenu = Button(oui, text="Retour au menu", command=partial(menu2jeu, menu))
tomenu.grid(column=1, row =2, padx=480, pady=300)

tojeu = Button(oui, text="Jouer", command=partial(menu2jeu, jeu))
tojeu.grid(column=3, row =5)
#########Menu#########

fenetre.mainloop()

###TEST BETA D'INTERFACE 
##fenetre = Tk()
##def complet(item, perso, nb):
##    ajout_dans_inventaire(item, perso, nb)
##    label.config(text=perso.inventaire)
##    
##label = Label(fenetre, text=Arthur.inventaire, width=200)
##label.grid(column=1, row= 0)
##
##ajout_soin = Button(fenetre, text="Ajoute une potion de soin", command=partial(complet, Potion_soin, Arthur, 1))
##ajout_soin.grid(column=0, row= 1)
##
##ajout_casque = Button(fenetre, text="Ajoute le casque de Wazuki IV", command=partial(complet, Casque_WazukiIV, Arthur, 1))
##ajout_casque.grid(column=3, row= 1)
##
##fenetre.mainloop()
