#-*- coding: utf-8 -*-
import pickle

from SauvegardeEtLoad import *
from Classes import *
from Visualisation import * 
from FonctionImportante import *

#Ici on met les persos + les items pour test les fonctions et les classes
Poudre_magique = Item("Poudre de perlinpainpain",50,20, 10, "C'est une poudre magiiiiique !")
Ronce_demoniaque = Item("Ronce démoniaque",50,90, 10, "Elle pousse dans le cote cache de la lune.")
gluant = Monstre("Gluant", 5, 5, 5, [Poudre_magique, Ronce_demoniaque], "Brulure")
Epee_maudite = Arme("Epee maudite", 1,1,1,"Oui", 5, 0, 2, 0, 0 ,"","","main")
Casque_WazukiIV = Equipement("Casque du roi Wazuki IV", 1,1,1, 0, 10, 0, 200, 2,"Oui","","","tete")
Potion_soin = Consommable("Potion de soin",1,1,1,"Potion qui soigne 2 pv", 2, 12)
Brulure = Effet("Brûlure", 2 , 2, "Au secours ça brule !")
Poison = Effet("Poison", 2 , 2, "J'ai mal")
Purge = Effet("Purge", 2 , 1, "Je suis guérie !")
Boule_de_feu = Sort("Boule de feu", 50, "C'est une boule de feu", 10, 0, Brulure, 1)
Glace = Sort("Glace", 50, "Non ce n'est pas celle que tu manges l'été", 10, 0, Purge, 2)
Mage = Classe("Mage",[Boule_de_feu.nom, Glace.nom])
Guerrier = Classe("Guerrier",[])
Paladin = Classe("Paladin",[])
Arthur = Personnage("Arthur",8,10,0,0,0,"Mage",0,0,0,0,0,0,[Boule_de_feu.nom, Glace.nom], dict())
Jean = Personnage("Jean",3,10,0,0,0,"Paladin",0,0,0,0,0,0,[], dict())
Michel = Personnage("Michel",3,10,0,0,0,"Guerrier",0,0,0,0,0,0,[], dict())
