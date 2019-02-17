#-*- coding: utf-8 -*-
import pickle

from SauvegardeEtLoad import *
from Classes import *
from Visualisation import * 
from FonctionImportante import *
from tkinter import *
from functools import *

#Ici on met les persos + les items pour test les fonctions et les classes
Poudre_magique = Item("Poudre de perlinpainpain",50,20, 10, "C'est une poudre magiiiiique !")
Ronce_demoniaque = Item("Ronce démoniaque",50,90, 10, "Elle pousse dans le cote cache de la lune.")
Epee_maudite = Arme("Epee maudite", 1,90,1,"Ceci est l'épée maudite !", 5, 0, 2, 0, 0 ,"","","main")
Casque_WazukiIV = Equipement("Casque du roi Wazuki IV", 1,1,1, 0, 10, 0, 200, 2,"Vieux casque dégueulasse","","","tete")
Potion_soin = Consommable("Potion de soin",1,1,1,"Potion qui soigne 2 pv", 2, 12)
Brulure = Effet("Brûlure", 2 , 2, "Au secours ça brule !")
Poison = Effet("Poison", 2 , 2, "J'ai mal")
Purge = Effet("Purge", 2 , 1, "Je suis guérie !")
Gluant = Monstre("Gluant", 5, 13, 20, 1, [Poudre_magique, Ronce_demoniaque], Brulure, 1)
Multi_Gluant = Monstre("Multi Gluant", 5, 13, 20, 1, [Epee_maudite], Poison, 2)

Boule_de_feu = Sort("Boule de feu", 50, "C'est une boule de feu", 10, 0, Brulure, 1)
Glace = Sort("Glace", 50, "Non ce n'est pas celle que tu manges l'été", 10, 0, Purge, 2)
Mage = Classe("Mage",[Boule_de_feu.nom, Glace.nom])
Guerrier = Classe("Guerrier",[])
Paladin = Classe("Paladin",[])
Arthur = Personnage("Arthur",8,10,0,0,0,"Mage",0,0,0,0,0,0,[Boule_de_feu.nom, Glace.nom], dict())
Jean = Personnage("Jean",3,10,0,0,0,"Paladin",0,0,0,0,0,0,[], dict())
Michel = Personnage("Michel",3,10,0,0,0,"Guerrier",0,0,0,0,0,0,[], dict())
Ish = PNJ("Ish", [Epee_maudite.nom, Casque_WazukiIV.nom])

Plaine = Zone("Plaine", [Gluant, Multi_Gluant], "C'est une plaine")

#TEST MENU PRINCIPAL










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
