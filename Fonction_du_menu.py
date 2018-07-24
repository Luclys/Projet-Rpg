#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 20:42:11 2017

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

def menu():
    while menu:
        print("Que voulez-vous faire?\n - Inventaire\n - Statistiques\n - Baffer\n - Partir au combat !\n - Quitter")
        choice = input()
        if choice == "Inventaire" or choice == "inventaire":
            d.show_inventory()
            d.show_equipement()
            retour = False
            while retour == False:
                print("Taper A pour retourner au menu principal")
                retour = input()
                if retour == "A" or retour == "a":
                    retour = True
        elif choice == "Baffer" or choice == "baffer":
            print("Aie !")
            return MenuDeMaltraitance()
            retour = False
            while retour == False:
                print("Taper A pour retourner au menu principal")
                retour = input()
                if retour == "A" or retour == "a":
                    retour = True
        elif choice == "Statistiques" or choice == "statistiques" or choice =="stats" or choice == "Stats":
            d.show()
            retour = False
            while retour == False:
                print("Taper A pour retourner au menu principal")
                retour = input()
                if retour == "A" or retour == "a":
                    retour = True
        elif choice =="Quitter" or choice == "quitter":
            break
        else :
            print("Cette commande n'est pas disponible")
            retour = False
            while retour == False:
                print("Taper A pour retourner au menu principal")
                retour = input()
                if retour == "A" or retour == "a":
                   retour = True

def MenuDeMaltraitance():
    choice = input("Que voulez vous faire de votre personnage ? \n Appuyez sur A pour retourner au menu : ") #là on s'enjaille sur le cosmétique / sadisme : baffer, fouetter (Ref à Dungeon keeper :)), éléctrocuter, empoisonner etc...
    if choice == "A" or choice == "a":
        return menu()
