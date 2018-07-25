#-*- coding: utf-8 -*-
import os.path
from random import *
import pickle

from SauvegardeEtLoad import *
from Classes import *
from Visualisation import * 


######## Groupe gestion d'inventaire 
def ajout_dans_inventaire(item,perso,nb_exemplaire):
    if item.nom in perso.inventaire :
        perso.inventaire[item.nom] += nb_exemplaire
    else :
        perso.inventaire[item.nom] = nb_exemplaire
    

def supprimer_de_inventaire(item,perso, nb_exemplaire):
    if perso.inventaire[item.nom] > 0:
        perso.inventaire[item.nom] -= nb_exemplaire
    if perso.inventaire[item.nom] <= 0 :
        perso.inventaire.pop(item.nom)

######### Groupe looting/xp
#On appelera cette fonction une fois le(s) monstre(s) vaincu

def lootRarete(monstre, perso,):
    prospectionTotale = perso.prospection + randint(0, 101)
    Lootable = list()
    listeDeLoot = list()
    nombreDeLoot = randint(1, 11)
    for i in monstre.loot :
        if prospectionTotale >= i.rarete:
            Lootable.append(i)
    for i in range(nombreDeLoot) :
        if Lootable :
            listeDeLoot.append(choice(Lootable))
        else :
            break
    for i in listeDeLoot :
        ajout_dans_inventaire(i,perso,1)
#Le nombre d'exemplaire est géré par un nombre aléatoire
#Le drop est géré
