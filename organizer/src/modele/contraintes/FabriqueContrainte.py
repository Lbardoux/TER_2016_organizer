#!/usr/bin/python3
# -*-coding:utf-8 -*

import os, sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/")
import Contrainte, Blocage, Ressource, Precedence, Obligation, DateLimite
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../../outils")
import enum, Fabrique


# Création de l'enum pour la fabrique
Contraintes = enum.enum('BLOCAGE', 'PRECEDENCE', 'OBLIGATION', 'DATE_LIMITE', 'RESSOURCE')


class FabriqueContrainte(Fabrique.Fabrique):
	"""
	Voici la classe qui va se charger de la création des contraintes.
	Via un "enum", il suffira de demander ce que l'on veut
	Et la fabrique nous le fournira directement, si tant est qu'on lui
	fourni les bons matériaux.
	USAGE :
	--> créer une Obligation : il faut un nombre en argument
	--> créer une Blocage : il faut un ou plusieurs nombre(s)  en argument
	--> créer une DateLimite : il faut un nombre en argument
	--> créer une Precedence : il faut 2 arguments
	@author: Laurent Bardoux p1108365
	@version: 2.0
	"""
	
	def __init__(self):
		"""
		Construit une fabrique de contrainte simple
		Ceci va initialiser le dictionnaire des valeurs possible
		dans le but de réaliser un "switch"
		@param self: L'argument implicite
		Pour ajouter des choix, il suffit alors de rajouter des lignes
		dans _choix avec une lambda ou une fonction qui doit agir le
		cas echeant
		"""
		dico = {
			Contraintes.BLOCAGE : lambda *x : Blocage.Blocage(*x),
			Contraintes.PRECEDENCE : lambda x, y : Precedence.Precedence(x, y),
			Contraintes.OBLIGATION : lambda x : Obligation.Obligation(x),
			Contraintes.DATE_LIMITE : lambda x : DateLimite.DateLimite(x),
			Contraintes.RESSOURCE : lambda : Ressource.Ressource()
		}
		super(FabriqueContrainte, self).__init__(dico)
	#fin __init__
	
#fin FabriqueContrainte
