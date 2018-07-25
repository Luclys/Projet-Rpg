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

def utiliser_consommables(perso, consommable):
    if perso.pv == perso.pvmax :
        print("Vous avez toute votre vie")
    else :
        supprimer_de_inventaire(consommable,perso,1)
        if (perso.pv + consommable.valeur) > perso.pvmax :
            perso.pv = perso.pvmax
        else :
            perso.pv += consommable.valeur


def equiper_arme(perso, item):
    if perso.emplacements["Mains"] <= 0 and item.nom in perso.inventaire:
        print("impossible de s'équiper de l'arme votre main sont déjà prises")
    else :
        perso.equipement.append(item.nom)
        perso.inventaire.pop(item.nom)
        perso.emplacements["Mains"] -= 1

def desequiper_arme(perso, item):
    if perso.equipement :
        perso.equipement.remove(item.nom)
        ajout_dans_inventaire(item,perso,1)
        perso.emplacements["Mains"] += 1
    else :
        print("Vous êtes équipé d'aucune arme")


######### Groupe looting/xp
#On appelera cette fonction une fois le(s) monstre(s) vaincu
def rareteToStr(item):
    if item.rarete >= 90 :
        print("Rarete = Légendaire !")
    elif item.rarete >= 70 :
        print("Rarete = Epique")
    elif item.rarete >= 50 :
        print("Rarete = Rare")
    else :
        print("Rarete = Commun")
    
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
