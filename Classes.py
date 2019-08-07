#-*- coding: utf-8 -*-
from random import *
##################################  GROUPE PERSONNAGES/MONSTRES/BOSS
class Personnage:
    #Effet appliqué directement
    effet = ''
    tour_effet = 0
    #Tour pour combat
    tour = 0
    #Emplacements des equipements
    ############
    argent = 0
    exp = 0
     #Choisie aleatoirement l'exp pour atteindre le niveau 2 pour le fun x) 
    niveau = 1
    def __init__(self, nom, pv, pvmax, force, puissance, defense, classe, prospection, critique, precision, vitesse, mana, poidsMax, sort_utilisable, inventaire): 
        self.pv = pv
        self.pvmax = pvmax
        self.force = force
        self.puissance = puissance #Les mages utilisent de la magie donc pas de force mais une stat de puissance pour eux
        self.vitesse = vitesse
        self.critique = critique
        self.precision = precision
        self.defense = defense
        self.mana = mana
        self.prospection = prospection
        self.classe = classe
        self.nom = nom
        self.poidsMax = poidsMax
        self.sort_utilisable = sort_utilisable #Voir les sorts dispo nécéssaires pour les trier etc (dans une liste)
        self.inventaire = inventaire
        self.expmax = randint(150, 200)
        self.empla = {'tete' : 0,
             'dos' :0,
            'bras1' : 0,
            'bras2' : 0,
            'pieds' : 0,
            'main' : 0}
    #METHODES DE MODIFICATION
    
    def ajout_dans_inventaire(self,item,nb_exemplaire):
        if item.nom in self.inventaire :
            self.inventaire[item.get_nom()] += nb_exemplaire
        else :
            self.inventaire[item.get_nom()] = nb_exemplaire
    
    def supprimer_de_inventaire(self,item,nb_exemplaire):
        if self.inventaire[item.get_nom()] > 0:
            self.inventaire[item.get_nom()] -= nb_exemplaire
        if self.inventaire[item.get_nom()] <= 0 :
            self.inventaire.pop(item.get_nom())

    def utiliser_consommables(self, consommable):
        if self.pv == self.pvmax :
            print("Vous avez toute votre vie")
        else :
            supprimer_de_inventaire(self,consommable,1)
            if (self.pv + consommable.valeur) > self.pvmax :
                self.pv = self.pvmax
            else :
                self.pv += consommable.valeur
                
    def mettre_equipement(self, item): 
        if self.empla[item.get_emplacement()] == False and item.nom in self.inventaire:
            self.empla[item.get_emplacement()] = item.nom
            self._up_stats(item)
        else:
            print('Il y a déjà un objet ici !')

    def enlever_equipement(self, item):
        if self.empla[item.get_emplacement()]:
            self.empla[item.get_emplacement()] = 0
            self._down_stats(item)
        else:
            print("Il n'y a pas d'objet ici...")

    def acheter_objet(self, pnj, item): #Pour acheter des objets aux marchands
        if self.argent >= item.get_cout() and item.get_nom() in pnj.objet:
            self.ajout_dans_inventaire(item, 1)
            self.argent -= item.get_cout()
        else :
            print("T'es pauvre ou l'objet n'est pas disponible")

    def vendre_objet(self, item): #Pour vendre des objets aux marchands
        if item.get_nom() in self.inventaire:
            self.supprimer_de_inventaire(item, 1)
            perso.argent += item.get_cout() * 0.5

    def donne_exp(self, monstre): #donne de l'exp au perso voir comment on la calcule
        self.exp += (12 + monstre.get_niveau())
        print('Tu as gagné ' + str((12 + monstre.get_niveau())) + " d'exp")
        if self.exp >= self.expmax:
            self.niveau += 1
            print("TU PASSES AU NIVEAU " + str(self.niveau) + " !!!")
            self.exp = abs(self.expmax - self.exp)
            self.expmax *= uniform(1.20, 1.5)
            self._ameliore_stats()
            self.get_caracteristique()
        self.niveau_sup()
    def donne_argent(self, monstre): #donne de l'argent au perso voir comment on la calcule
        self.argent += (10 + monstre.get_niveau())
        print('Tu as gagné ' + str((10 + monstre.get_niveau())) + " pièces d'or")
    def lootRarete(self,monstre):
        prospectionTotale = self.prospection + randint(0, 101)
        Lootable = list()
        listeDeLoot = list()
        nombreDeLoot = randint(1, 11)
        for i in monstre.get_loot() :
            if prospectionTotale >= i.get_rarete():
                Lootable.append(i)
        for i in range(nombreDeLoot) :
            obj_obtenu = choice(Lootable)
            if Lootable and obj_obtenu not in listeDeLoot:
                listeDeLoot.append(obj_obtenu)
            else :
                break
        for i in listeDeLoot :
            self.ajout_dans_inventaire(i,randint(1,3))
            print('Vous avez récupéré ' + i.nom + ' durant le combat !')

    def donne_sort(self, classe, sort):#Permet d'apprendre un sort (doit etre link au systeme de lvl car la le sort ne s'apprend pas tout seul à la montée de niveau requis
        if sort.get_nom() in classe.get_sort() and self.niveau >= sort.get_niveau_requis() and sort.get_nom() not in self.sort_utilisable:
            self.sort_utilisable.append(sort.get_nom())
        else :
            print("Vous ne pouvez pas apprendre ce sort !")

    def _ameliore_stats(self): #Meme probleme que mettre_equipement trouver un moyen de faire perso.nom_de_la_classe pour eviter les if
        if self.classe == "Mage" :
            self.pvmax += randint(1, 3)
            self.puissance += randint(5, 10)
            self.vitesse += randint(0, 1)
            self.defense += randint(1, 2)
            self.mana += randint(500, 800)
        elif self.classe == "Guerrier" :
            self.pvmax += randint(5, 10)
            self.force += randint(5, 10)
            self.vitesse += randint(1, 3)
            self.defense += randint(1, 5)
            self.mana += randint(0, 150)
        elif self.classe == "Paladin" :
            self.pvmax += randint(5, 15)
            self.puissance += randint(1, 5)
            self.force += randint(1, 5)
            self.vitesse += randint(1, 2)
            self.defense += randint(1, 5)
            self.mana += randint(200, 500)
        self.critique += randint(0, 1)
        self.precision += randint(0, 1)
        self.prospection += randint(0, 1)
        self.poidsMax += randint(20, 50)

    def _up_stats(self, item):
        self.inventaire.pop(item.get_nom())
        self.force += item.force
        self.puissance += item.puissance
        self.vitesse += item.vitesse
        self.mana += item.mana
        self.defense += item.defense

    def _down_stats(self,item):
        self.ajout_dans_inventaire(item,1)
        self.force -= item.force
        self.puissance -= item.puissance
        self.vitesse -= item.vitesse
        self.mana -= item.mana
        self.defense -= item.defense
    
    def set_effet(self, effet):
        self.effet = effet

    def set_tour_effet(self, tour):
        self.tour_effet = tour
        
    #METHODES D'AFFICHAGE
    def get_caracteristique(self):
        print('*******************\n***' + self.nom + '***\n***'\
              + self.classe + '***\nPV : '\
              + str(self.pv) + '/' + str(self.pvmax) + '\nForce : '\
              + str(self.force) + '\nPuissance : '\
              + str(self.puissance) + '\nVitesse : '\
              + str(self.vitesse) + '\nCritique : '\
              + str(self.critique) + '\nPrecision : '\
              + str(self.precision) + '\nDefense : '\
              + str(self.defense) + '\nMana : '\
              + str(self.mana) + '\nProspection : '\
              + str(self.prospection) + '\nPoids max : '\
              + str(self.poidsMax) + '\n*******************\n')
        
    def niveau_sup(self):
        print("Il vous faut ", str(self.expmax - self.exp)\
              , " points d'expérience pour atteindre le prochain niveau !")
        
    def get_argent(self):
        print('Vous avez ' + str(self.argent) + ' PO actuellement')
        
    def get_inventaire(self):
        print(str(self.inventaire))
        
    def get_prospection(self): #necessaire pour calculer le drop
        return self.prospection

    def get_tour_effet(self):
        return self.tour_effet

    def get_effet(self):
        return self.effet

     
class Classe:
    def __init__(self, nom, tout_sort):
        self.nom = nom
        self.tout_sort = tout_sort #Tout les sorts de la classe en question (dans une liste)

    def get_sort(self):
        return self.tout_sort

    
class PNJ:
    def __init__(self, nom, objet):
        self.nom = nom
        self.objet = objet #Objet qu'il vend (dans une liste)
    def get_objet(self):
        return self.objet


    
class Monstre:
    def __init__(self, nom, vitesse, pv, pvmax, force, loot, effet, niveau):
        self.nom = nom
        self.vitesse = vitesse
        self.pv = pv
        self.pvmax= pvmax
        self.force = force
        self.loot = loot #une liste qui contient LES NOMS des objets lootables par le monstre
        self.effet = effet
        self.niveau = niveau #Le niveau des mobs pourquoi pas faire un randomizateur et si tu tombes contre un mob lvl 3 il a + de degat que un lvl 2 (et donne + d'exp)

    def get_loot(self):
        return self.loot

    def get_nom(self):
        return self.nom

    def get_niveau(self):
        return self.niveau


    
class Boss(Monstre):
    def __init__(self,nom, vitesse, pv, pvmax, force, loot, effet, niveau,defense,armure,sorts,mana):
        self.nom = nom
        self.vitesse = vitesse
        self.pv = pv
        self.pvmax= pvmax
        self.force = force
        self.loot = loot #une liste qui contient LES NOMS des objets lootables par le monstre
        self.effet = effet
        self.niveau = niveau
        self.defense = defense #les boss, contrairement aux sous monstres, ont une stat de défense, et peuvent donc être plus ou moins tanky
        self.armure = armure #Les boss peuvent eux aussi avoir de l'armure
        self.sorts = sorts #liste qui contient tous les sorts que possède le monstre
        self.mana = mana #Pour lancer ses sorts il lui faut du mana
    #Note : les monstres élites sont des miniboss, ils auront donc des stats réduites : peu/pas de sorts ou de faibles stats à côté



############################    GROUPE EFFET/SORT
class Sort:
    def __init__(self, nom, coutMana, description, degat, soin, effet, niveau_requis):
        self.nom = nom
        self.coutMana = coutMana
        self.description = description
        self.degat = degat #si le sort fait des degats
        self.soin = soin #si le sort heal
        self.effet = effet
        self.niveau_requis = niveau_requis #niveau requis pour apprendre le sort

    def get_nom(self):
        return self.nom

    def get_niveau_requis(self):
        return self.niveau_requis


    
class Effet:    
    def __init__(self, nom,valeur,duree, description): #la valeur c'est ce que ça fait: ce que ça modifie comme stat,  ou les dégats que ça inflige
        self.nom = nom
        self.description = description
        self.valeur = valeur
        self.duree = duree
        
    def set_tour(self,duree):
        self.duree
        
    def set_valeur(self,valeur):
        self.valeur
        
    def applique_effet_equip(self,perso, equipement): #Applique l'effet d'un equipement 
        if equipement.get_effet_sur_joueur():
            perso.set_effet(equipement.get_effet_sur_joueur)
            perso.tour_effet(self.tour)

    def applique_effet_de_mob(self,perso, monstre): #Applique l'effet quand un mob tape sur le perso
        if monstre.effet and perso.get_effet() == "":
            perso.set_effet(monstre.effet.nom)
            perso.set_tour_effet(self.duree)
            print("Outch tu possèdes désormais l'effet de " + perso.get_effet() + "...")

    def applique_dommage_effet(self,perso): #Appliqueur de dommage 
        if perso.get_tour_effet() == 0:
            perso.set_effet("")
        elif perso.get_effet() == "Purge":
            perso.set_effet("")
        else :
            perso.pv -= self.valeur
            perso.set_tour_effet(perso.get_tour_effet() - 1)


###########################     GROUPE ITEM/CONSO/STUFF/ARME
class Item:
    def __init__(self, nom, cout, rarete, poids, description):
        self.nom = nom
        self.cout = cout 
        self.rarete = rarete
        self.poids = poids
        self.description = description

    #METHODES D'AFFICHAGE    
    def rareteToStr(self):
        if self.rarete >= 90 :
            print("Rarete : Légendaire !")
        elif self.rarete >= 70 :
            print("Rarete : Epique")
        elif self.rarete >= 50 :
            print("Rarete : Rare")
        else :
            print("Rarete : Commun")

    def get_nom(self):
        return self.nom

    def get_cout(self):
        return self.cout

    def get_rarete(self):
        return self.rarete
    
    def get_poids(self):
        return self.poids
    
class Consommable(Item):
    def __init__(self,nom, cout, rarete, poids, description, effet, valeur): 
        self.nom = nom
        self.cout = cout 
        self.rarete = rarete
        self.poids = poids
        self.description = description
        self.effet = effet
        self.valeur = valeur

    def get_effet(self):
        return self.effet

    def get_valeur(self):
        return self.valeur
    
class Equipement(Item):
    def __init__(self, nom, cout, rarete, poids, force, puissance, vitesse, mana, defense, description, effet_sur_joueur, effet_sur_mob, emplacement):
        self.nom = nom
        self.cout = cout 
        self.rarete = rarete
        self.poids = poids
        self.force = force
        self.puissance = puissance
        self.vitesse = vitesse
        self.mana = mana
        self.defense = defense
        self.description = description
        self.effet_sur_joueur = effet_sur_joueur
        self.effet_sur_mob = effet_sur_mob
        self.emplacement = emplacement #indique l'emplacement de l'item (c'est un str)

    def get_effet_sur_joueur(self):
        return self.effet_sur_joueur

    def get_effet_sur_mob(self):
        return self.effet_sur_mob

    def get_emplacement(self):
        return self.emplacement

    def get_caracteristique(self):
        print("Nom : ",self.nom)
        print("Cout : ",self.cout)
        self.rareteToStr() #Rareté de l'item
        print("Cet équipement donne ", self.force, " de force")
        print("Cet équipement donne ", self.puissance, " de puissance")
        print("Cet équipement donne ", self.vitesse, " d'accéleration")
        print("Cet équipement donne ", self.mana, " de mana")
        print("Cet équipement donne ", self.defense, " d'armure !")
        print("Description : ",self.description)
        print("Poids : ",self.poids )
        print('\n')
        
class Zone(): #Systeme de zone avec des monstres specifiques a chaque zone 
    def __init__(self, nom, monstre, description):
        self.nom = nom
        self.monstre = monstre #les monstres de la zone (en liste)
        self.description = description
        
    def get_nom(self):
        return self.nom
    
    def get_description(self):
        return self.description
