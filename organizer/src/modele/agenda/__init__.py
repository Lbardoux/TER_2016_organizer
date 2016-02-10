#!/usr/bin/python
# -*-coding:utf-8 -*
"""
#### USAGE DE L'API Agenda ####

Agenda :
Cette classe est la partie frontale de l'API, c'est vers elle que les
demandes de lectures/écritures doivent se faire.
Pour cela, 3 méthodes peuvent etre employées via une instance de la
classe Agenda :
--> recupererSemaineParNumJour(self, annee, mois, jour)                         (1)
--> supprimerCreneau(self, annee, mois, jour, idCreneau)                        (2)
--> ajouterCreneau(self, annee, mois, jour, debut, fin, typeCreneau=CP.CRENEAU) (3)
--> recupererJour(self, annee, mois, jour)                                      (4)
Toutes ces méthodes peuvent levé une exception de type ValueError, alors attention !

Je vais à présent détailler le fonctionnement de chacune d'elles :
--1. recupererSemaineParNumJour
Cette fonction va permettre de récupérer une Semaine en fonction de:
-- numéro d'année (2015 par exemple)
-- numéro de jour
-- numéro de mois
Le resultat peut etre utilisée de la façon suivante :
semaine = agenda.recupererSemaineParNumJour(2005, 11, 25)
for nomJour in semaine.listeNomJours:
...jour = semaine.jours[nomJour]
...creneaux = jour.creneaux
...# manipuler la liste creneaux

--2. supprimerCreneau
Cette fonction permet de supprimer un creneau dans l'arborescence, en se basant
sur son identifiant, et en cherchant en fonction de :
-- numéro d'année (2015 par exemple)
-- numéro de jour
-- numéro de mois

--3. ajouterCreneau
Cette méthode ajoute un Creneau dans la structure, le type permettant de spécifier
si l'on veut créer un CM, un TP, un EXAMEN.
On peut le laisser par défaut pour un Creneau standard

--4. recupererJour
Renvoie la liste des créneaux du jours demandé, directement.
"""
