#-*- coding: utf-8 -*-
import os.path
from random import *
import pickle
from SauvegardeEtLoad import *
from Classes import *
from Visualisation import * 


######## Groupe gestion d'inventaire et equipements
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

def mettre_equipement(perso, item):
    perso.tag = item.emplacement
    if perso.tag == "tete" :
        if perso.tete and item.nom in perso.inventaire:
             print("Vous avez déjà un objet sur cet emplacement")
        else :
            perso.tete = item.nom
            perso.inventaire.pop(item.nom)
    elif perso.tag == "dos" :
        if perso.dos and item.nom in perso.inventaire:
             print("Vous avez déjà un objet sur cet emplacement")
        else :
            perso.dos = item.nom
            perso.inventaire.pop(item.nom)
    elif perso.tag == "bras1" :
        if perso.bras1 and item.nom in perso.inventaire:
             print("Vous avez déjà un objet sur cet emplacement")
        else :
            perso.bras1 = item.nom
            perso.inventaire.pop(item.nom)
    elif perso.tag == "bras2" :
        if perso.bras2 and item.nom in perso.inventaire:
             print("Vous avez déjà un objet sur cet emplacement")
        else :
            perso.bras2 = item.nom
            perso.inventaire.pop(item.nom)
    elif perso.tag == "pieds" :
        if perso.pieds and item.nom in perso.inventaire:
             print("Vous avez déjà un objet sur cet emplacement")
        else :
            perso.pieds = item.nom
            perso.inventaire.pop(item.nom)
    elif perso.tag == "main" :
        if perso.main and item.nom in perso.inventaire:
             print("Vous avez déjà une arme dans vos mains !")
        else :
            perso.main = item.nom
            perso.inventaire.pop(item.nom)

def enlever_equipement(perso, item):
    perso.tag = item.emplacement
    if perso.tag == "tete" :
        if perso.tete :
            perso.tete = ""
            ajout_dans_inventaire(item,perso,1)
        else :
            print("Vous êtes équipé d'aucune pièce d'équipement")
    elif perso.tag == "dos" :
        if perso.dos :
            perso.dos = ""
            ajout_dans_inventaire(item,perso,1)
        else :
            print("Vous êtes équipé d'aucune pièce d'équipement")
    elif perso.tag == "bras1" :
        if perso.bras1 :
            perso.bras1 = ""
            ajout_dans_inventaire(item,perso,1)
        else :
            print("Vous êtes équipé d'aucune pièce d'équipement")
    elif perso.tag == "bras2" :
        if perso.bras2 :
            perso.bras2 = ""
            ajout_dans_inventaire(item,perso,1)
        else :
            print("Vous êtes équipé d'aucune pièce d'équipement")
    elif perso.tag == "pieds" :
        if perso.pieds :
            perso.pieds = ""
            ajout_dans_inventaire(item,perso,1)
        else :
            print("Vous êtes équipé d'aucune pièce d'équipement")
    elif perso.tag == "main" :
        if perso.main :
            perso.main = ""
            ajout_dans_inventaire(item,perso,1)
        else :
            print("Vous êtes équipé d'aucune pièce d'équipement")


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

######### Groupe experience et monter de lvl

def donne_exp(perso, nb_exp):
    perso.exp += nb_exp
    if perso.exp >= perso.expmax:
        perso.niveau += 1
        perso.exp = 0
        perso.expmax *= uniform(1.20, 1.5)
        ameliore_stats(perso)

def ameliore_stats(perso):
    if perso.classe == "Mage" :
        perso.pvmax += randint(1, 3)
        perso.armure += randint(0, 1)
        perso.vitesse += randint(0, 1)
        perso.critique += randint(0, 1)
        perso.precision += randint(0, 1)
        perso.defense += randint(1, 2)
        perso.mana += randint(500, 800)
        perso.prospection += randint(0, 1)
        perso.poidsMax += randint(20, 50)
    elif perso.classe == "Guerrier" :
        perso.pvmax += randint(5, 10)
        perso.armure += randint(3, 6)
        perso.force += randint(5, 10)
        perso.vitesse += randint(1, 3)
        perso.critique += randint(0, 1)
        perso.precision += randint(0, 1)
        perso.defense += randint(1, 5)
        perso.mana += randint(0, 150)
        perso.prospection += randint(0, 1)
        perso.poidsMax += randint(20, 50)
    elif perso.classe == "Paladin" :
        perso.pvmax += randint(5, 15)
        perso.armure += randint(3, 6)
        perso.force += randint(1, 5)
        perso.vitesse += randint(1, 2)
        perso.critique += randint(0, 1)
        perso.precision += randint(0, 1)
        perso.defense += randint(1, 5)
        perso.mana += randint(200, 500)
        perso.prospection += randint(0, 1)
        perso.poidsMax += randint(20, 50)
   

def donne_sort(perso, classe, sort):
    if sort.nom in classe.tout_sort and perso.niveau >= sort.niveau_requis:
        perso.sort_utilisable.append(sort.nom)
    else :
        print("Vous ne pouvez pas apprendre ce sort !")


    
