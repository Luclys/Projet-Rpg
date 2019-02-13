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
#fenetre.attributes('-fullscreen', 1)
fenetre.geometry("700x700")
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
        bafe.grid()
        time.sleep(1)
    bafe.destroy()
    return None

def changemenu(frame):
    frame.tkraise()

#Prend tout l'écran



inventaire = Frame(fenetre,borderwidth=2,relief=GROOVE, bg="blue")
inventaire.grid_propagate(0) #Permet de pas redimensionner le frame par rapport aux widgets
jeu = Frame(fenetre,borderwidth=2,relief=GROOVE, bg="green")
jeu.grid_propagate(0)
menu = Frame(fenetre,borderwidth=2,relief=GROOVE, bg="red", height= 700, width = 700)
menu.grid_propagate(0)

for frame in (inventaire, menu, jeu):
    frame.grid(row=0, column=0, sticky='news')
    
#import la photo
epee = PhotoImage(file='image/epee.png')
jouer = PhotoImage(file='image/oui.png')
#boutons menu    
tojeu = Button(menu, image=jouer, command=partial(changemenu, jeu))
tojeu.place(x=165, y=100) #permet de placer directement l'element (dans le frame car grid est deja use par le frame lui meme)


quitter = Button(menu, text="Quitter le jeu", command= partial(final))
quitter.place(x=325, y=325)

#boutons jeu
todungeon = Button(jeu, text="Partir à l'aventure !", command=partial(changemenu, menu))
todungeon.grid()

toinventory = Button(jeu, text="Voir son inventaire", command=partial(changemenu, inventaire))
toinventory.grid()

baffer = Button(jeu, text="Baffer !", command=partial(baffe))
baffer.grid()

tomenu = Button(jeu, text="Retour au menu principal", command=partial(changemenu, menu))
tomenu.grid()


#boutons inventaire
tojeu1 = Button(inventaire, text="Retour au menu", command=partial(changemenu, jeu))
tojeu1.grid()


case1 = Button(inventaire, image = epee , command=partial(changemenu, jeu), relief=RIDGE)
case1.grid()
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
