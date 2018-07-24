#-*- coding: utf-8 -*-
import os.path
from random import *
import pickle

from SauvegardeEtLoad import *
from Classes import *
from Visualisation import * 



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

