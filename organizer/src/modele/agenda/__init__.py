#!/usr/bin/python3
# -*-coding:utf-8 -*
"""
API Agenda.

Agenda :
Cette classe est la partie frontale de l'API, c'est vers elle que les
demandes de lectures/écritures doivent se faire.
Pour cela, 3 méthodes peuvent etre employées via une instance de la
classe Agenda :
	1. L{Agenda.Agenda.recupererSemaineParNumJour}
	2. L{Agenda.Agenda.supprimerCreneau}
	3. L{Agenda.Agenda.ajouterCreneau}
	4. L{Agenda.Agenda.recupererJour}

Toutes ces méthodes peuvent lever une exception de type B{ValueError}, alors attention !


Détails
=======
Je vais à présent détailler le fonctionnement de chacune d'elles :

	1. L{Agenda.Agenda.recupererSemaineParNumJour}
		
		Cette fonction va permettre de récupérer une Semaine en fonction de:
			
			- numéro d'année (2015 par exemple)
			- numéro de jour
			- numéro de mois
		
		Le resultat peut etre utilisée de la façon suivante :
		
		>>> semaine = agenda.recupererSemaineParNumJour(2005, 11, 25)
		>>> for nomJour in semaine.listeNomJours:
		... 	jour = semaine.jours[nomJour]
		... 	creneaux = jour.creneaux
		... 	# manipuler la liste creneaux
	
	2. L{Agenda.Agenda.supprimerCreneau}
		
		Cette fonction permet de supprimer un creneau dans l'arborescence, en se basant
		sur son identifiant, et en cherchant en fonction de :
			- numéro d'année (2015 par exemple)
			- numéro de jour
			- numéro de mois
		
		>>> monAgenda.supprimerCreneau(2015, 5, 5, "ADuefy4856")
	
	3. L{Agenda.Agenda.ajouterCreneau}
		
		Cette méthode ajoute un Creneau dans la structure, le type permettant de spécifier
		si l'on veut créer un CM, un TP, un EXAMEN.
		On peut le laisser par défaut pour un Creneau standard
		
		>>> monAgenda.ajouterCreneau(2014, 12, 12, 14, 18)

	4. L{Agenda.Agenda.recupererJour}
		
		Renvoie la liste des créneaux du jours demandé, directement.
		
		>>> monAgenda.recupererJour(2015, 5, 5)

@author: Laurent Bardoux p1108365
@version: 1.0
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/")
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../outils")
