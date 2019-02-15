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
#fenetre.attributes('-fullscreen', 1) permet le fullscreen
fenetre.geometry("700x700")
toto = fenetre.winfo_screenwidth()
toto1 = fenetre.winfo_screenheight()
print(toto)
print(toto1) #La hauteur et la largeur de la fenetre askip
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
img_obj = dict()
key = PhotoImage(file='image/Casque_WazukiIV.png')

jouer = PhotoImage(file='image/oui.png')
quitte = PhotoImage(file='image/non.png')
#boutons menu    
tojeu = Button(menu, image=jouer, command=partial(changemenu, jeu))
tojeu.place(x=150, y=150) #permet de placer directement l'element (dans le frame car grid est deja use par le frame lui meme)


quitter = Button(menu, image=quitte, command= partial(final))
quitter.place(x=150, y=350)

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


#Affichage de la description d'un item
def creer():
    Descr.grid(row=0,column=8)

def detruire():
    Descr.grid_forget()


def ajout_img():
    nom_obj = entry_1.get()
    try:
        immg = PhotoImage(file='image/' + nom_obj +'.png')
        img_obj[nom_obj] = immg
        print("item ajouté !")
    except IOError:
        print("Erreur! Le fichier n'a pas pu être ouvert")
        
    
def ajout_inventaire_et_image(): #Permet d'ajouter l'objet dans l'inventaire et decharger son image (et creer un new button si il n'existe pas) 
    nom_obj = entry_1.get()
    ajout_dans_inventaire(eval(nom_obj),Jean,1)
    ajout_img()

Descr = LabelFrame(inventaire, text="Description", height= 300, width=100)
Descr.grid_forget()
slot2 = Button(inventaire, image=key, borderwidth=1, command=partial(detruire) ).grid(row=1, column=2)


entry_1 = Entry(inventaire)
button_1 = Button(inventaire, text="valider", borderwidth=1, command=partial(ajout_inventaire_et_image) ).grid(row=3, column=2)
entry_1.grid(row=2, column=2)
#description items
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
