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
#On appelera ses fonctions une fois le(s) monstre(s) vaincu

def loot(monstre): #Sous fonction : permet de choisir un item aléatoire dans la liste de drop du monstre.
    return monstre.loot[randint(0,len(monstre.loot) - 1)]

def lootComplet(monstre,perso): 
    listeDeLoot = list()
    for i in range(0,perso.prospection): #on loot des item x fois, avec x = prospection du personnage : 1 fois au début et plus après
        listeDeLoot.append(loot(monstre))
    for i in listeDeLoot :
        ajout_dans_inventaire(i,perso,nb_exemplaire):   #Le nombre d'exemplaire n'est pas géré on retravaillera ça
# !!!!!!!!!!    le i correspond à objet.nom, ça sert à faire le pont avec la "base de donnée" et c'est beaucoup plus facile à traiter
# (une simple STR) qui est un nom, donc on sait à quoi on a affaire.


#pour l'instant les chances de drop sont équivalentes, mais on pourra envisager de les affiner : un item legendaire aurait 5% de chance de drop et un commun
#en aurait 80 par exemple. à envisager plus tard
