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
#TEST MENU PRINCIPAL


fenetre = Tk()

#########Menu#########
def final():
    fenetre.destroy()

def baffe(): 
    th=Thread(target = lambda : attendre(5))
    th.start()
    return None
 
def attendre(duree):
    bafe = Label(jeu, text="Aie !")
    for i in range(duree):
        bafe.pack()
        time.sleep(1)
    bafe.destroy()
    return None

def changemenu(frame):
    frame.tkraise()

inventaire = Frame(fenetre,borderwidth=2,relief=GROOVE, bg="blue")
jeu = Frame(fenetre,borderwidth=2,relief=GROOVE, bg="green")   
menu = Frame(fenetre,borderwidth=2,relief=GROOVE, bg="red")

for frame in (inventaire, menu, jeu):
    frame.grid(row=0, column=0, sticky='news')

#import la photo 

oui = PhotoImage(file='image/epee.png')
#boutons menu    
tojeu = Button(menu, text="Jouer", command=partial(changemenu, jeu))
tojeu.pack()
quitter = Button(menu, text="Quitter le jeu", command= partial(final))
quitter.pack()

#boutons jeu
todungeon = Button(jeu, text="Partir à l'aventure !", command=partial(changemenu, menu))
todungeon.pack()

toinventory = Button(jeu, text="Voir son inventaire", command=partial(changemenu, inventaire))
toinventory.pack()

baffer = Button(jeu, text="Baffer !", command=partial(baffe))
baffer.pack()

tomenu = Button(jeu, text="Retour au menu principal", command=partial(changemenu, menu))
tomenu.pack()


#boutons inventaire
tojeu1 = Button(inventaire, text="Retour au menu", command=partial(changemenu, jeu))
tojeu1.pack(side=BOTTOM)

for ligne in range(5):
    for colonne in range(5):
        Button(fenetre, text='L%s-C%s' % (ligne, colonne), borderwidth=1).grid(row=ligne, column=colonne)

case1 = Button(inventaire, image = oui , command=partial(changemenu, jeu), relief=RIDGE)
case1.pack(side=TOP, padx=50, pady=50)
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
