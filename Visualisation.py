#-*- coding: utf-8 -*-
from SauvegardeEtLoad import *

######## Groupe de système de tour  

def combat(perso, monstre): #la fonction s'execute par le biais de entre_dans_combat
    monstre_nom = list()
    for i in monstre:
        monstre_nom.append(i.nom)
    print("Tu es contre ", str(monstre_nom))
    while perso.pv > 0  :
        perso.tour += 1
        print("Tour : ", perso.tour)
        print("Effet actuel : ", perso.get_effet, " pendant encore : ", perso.get_tour_effet)
        if perso.get_effet:
            applique_dommage_effet(perso)
        choix = input("Que voulez-vous faire ?")
        if choix == "Attaque" or choix == "attaque":
            for i in monstre:
                print(i.nom + '\n')
            choix2 = input("\nQui attaquer ? : ")
            for i in monstre:
                if i.nom == choix2:
                    cible = i
            cible.pv -= perso.force
            print("Monstre : ", cible.pv)
        cible.effet.applique_effet_de_mob(perso, cible)
        for i in monstre:
            perso.pv -= i.force
        print("Moi : ", perso.pv)
    if perso.pv <= 0 :
        print("Perdu!")
        cible.pv == cible.pvmax
    else :
        print("Bravo, votre ennemi est mort !")
        lootRarete(monstre, perso)
        donne_exp(perso, monstre)
        donne_argent(perso, monstre)
        cible.pv = cible.pvmax
        perso.effet = ""
        perso.tour_effet = 0
