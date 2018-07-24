#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 23:25:17 2017

@author: Zorino, Flywalker, mornviir
"""
#Importation de gros modules colombiens
from Classes_Monstre_Perso_Item_Armes import *
from Fonction_de_sauvegarde import *
from Fonction_de_chargement import *
from Fonction_du_menu import *
from Fonction_concernant_le_mode_AVENTURE import * 
import os.path
from random import *

#CE MODULE EST INCOMPLET, IL MANQUE LA PARTIE INVENTAIRE VU QUE J'AI PARSÉ COMME UN PORC, IL MANQUE AUSSI UNE FONCTION POUR ENLEVER LA DERNIERE ";" POUR QUE CE SOIT BIEN LISIBLE LORS DU CHARGEMENT
###############################"On lance TOUT le module à partir de loadUser, faut juste taper userino(perso)
def userino(perso):
    choix = input("Voulez vous spécifier la destination [O/n]?: ")
    if choix == 'O':
        desti = input('insérez votre destination : ')
    else:
        desti = "/home/mornviir/Documents/python/Projo RPG/users/"
    name = input("Quel est votre nom jeune aventurier ?: ")
    if os.path.exists(desti + name):
        print("Oh je vous reconnait !!!")
    else: 
        os.makedirs(desti + name,511)
        usr = open(desti + name + '/' + "usr"+name,'w')
        stat = open(desti + name + '/' + "stat"+name,'w')
        invent = open(desti + name + '/' + "invent"+name,'w')
        nbr = open(desti + name + '/' + "nbr"+name,'w')
        usr.close()
        invent.close()
        stat.close()
        nbr.close()
    return saveStats(perso,name,desti)


     
def saveStats(perso,name,desti):       #parse 1 = ;   
    stat = open(desti + name + '/'+ "stat"+ name, 'w')
    stat.write(str(perso.Dstats["Vie"]) +";")
    stat.write(str(perso.Dstats["Force"]) +";")
    stat.write(str(perso.Dstats["Valeur_Armure"]) +";")
    stat.write(str(perso.Dstats["Agilité"]) +";")
    stat.write(str(perso.Dstats["Mana"]))
    stat.close()
    return saveUser(perso,name,desti)

def saveUser(perso,name,desti):        #parse 1  = ;   
    usr = open(desti + name + '/'+ "usr"+ name, 'w')
    usr.write(str(perso.nom_perso) +";")
    usr.write(str(perso.argent) +";")
    usr.write(str(perso.exp) +";")
    usr.write(str(perso.mains_libres) +";")
    usr.write(str(perso.nom_classe))
    usr.close()
    return saveInvent(perso,name,desti)


def saveInvent(perso,name,desti):      #parse 1 = ; ||parse 2 = £
    nbr = open(desti + name + '/'+ "nbr" + name, 'w')
    invent = open(desti +name+"/" + 'invent' + name  , 'w')
    for i in perso.inventaire :
        nbr.write(str(perso.inventaire[i]) + ";")
    for i in perso.inventaire :  #faudra parser 2 fois : séparer les items et séparer le contenu des items
        invent.write(i.spécialshow() + ";")    
    invent.close()
    nbr.close() 
