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
#TEST MENU PRINCIPAL


fenetre = Tk()

#########Menu#########
def final():
    fenetre.destroy()

def baffe(): #COMMENT METTRE DU DELAY SUR UNE ACTION
    
    bafe = Label(jeu, text="Aie !")
    bafe.pack()
    bafe.destroy()
    
def menu2jeu(frame):
    frame.tkraise()

jeu = Frame(fenetre,borderwidth=2,relief=GROOVE, bg="green")   
menu = Frame(fenetre,borderwidth=2,relief=GROOVE, bg="red")
for frame in (menu, jeu):
    frame.grid(row=0, column=0, sticky='news')

#import la photo 

PhotoImage(file='image/fond.png')
#boutons menu    
tojeu = Button(menu, text="Jouer", command=partial(menu2jeu, jeu))
tojeu.pack()
quitter = Button(menu, text="Quitter le jeu", command= partial(final))
quitter.pack()

#boutons jeu
todungeon = Button(jeu, text="Partir à l'aventure !", command=partial(menu2jeu, menu))
todungeon.pack()

toinventory = Button(jeu, text="Voir son inventaire", command=partial(menu2jeu, menu))
toinventory.pack()

baffer = Button(jeu, text="Baffer !", command=partial(baffe))
baffer.pack()

tomenu = Button(jeu, text="Retour au menu principal", command=partial(menu2jeu, menu))
tomenu.pack()
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
