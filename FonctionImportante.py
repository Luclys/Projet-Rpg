#-*- coding: utf-8 -*-
import os.path
from random import *
import pickle
from SauvegardeEtLoad import *
from Classes import *
from Visualisation import * 

def up_stats(perso, item):
    perso.inventaire.pop(item.get_nom())
    perso.force += item.force
    perso.puissance += item.puissance
    perso.vitesse += item.vitesse
    perso.mana += item.mana
    perso.defense += item.defense

def down_stats(perso,item):
    perso.ajout_dans_inventaire(item,1)
    perso.force -= item.force
    perso.puissance -= item.puissance
    perso.vitesse -= item.vitesse
    perso.mana -= item.mana
    perso.defense -= item.defense
    
def ameliore_stats(perso): #Meme probleme que mettre_equipement trouver un moyen de faire perso.nom_de_la_classe pour eviter les if
    if perso.classe == "Mage" :
        perso.pvmax += randint(1, 3)
        perso.puissance += randint(5, 10)
        perso.vitesse += randint(0, 1)
        perso.critique += randint(0, 1)
        perso.precision += randint(0, 1)
        perso.defense += randint(1, 2)
        perso.mana += randint(500, 800)
        perso.prospection += randint(0, 1)
        perso.poidsMax += randint(20, 50)
    elif perso.classe == "Guerrier" :
        perso.pvmax += randint(5, 10)
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
        perso.puissance += randint(1, 5)
        perso.force += randint(1, 5)
        perso.vitesse += randint(1, 2)
        perso.critique += randint(0, 1)
        perso.precision += randint(0, 1)
        perso.defense += randint(1, 5)
        perso.mana += randint(200, 500)
        perso.prospection += randint(0, 1)
        perso.poidsMax += randint(20, 50)
   

####### Groupe Effet
def applique_effet_equip(perso, effet, item): #Applique l'effet d'un equipement 
    if item.effet_sur_joueur:
        perso.effet = item.effet_sur_joueur
        perso.tour_effet = effet.tour

def applique_effet_de_mob(perso, effet, monstre): #Applique l'effet quand un mob tape sur le perso
    if monstre.effet and perso.effet == "":
        perso.effet = monstre.effet.nom
        perso.tour_effet = effet.tour

def applique_dommage_effet(perso, effet): #Appliqueur de dommage 
    if perso.tour_effet == 0:
        perso.effet = ""
    elif perso.effet == "Purge":
        perso.effet = ""
    else :
        perso.pv -= effet.valeur
        perso.tour_effet -= 1
#VRAIMENT A REVOIR L'APPLIQUE DOMMAGE QUAND ON AURA LE SYSTEME DE TOUR PAR TOUR OPERATIONNEL



        
