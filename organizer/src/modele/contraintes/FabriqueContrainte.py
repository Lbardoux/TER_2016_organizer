#!/usr/bin/python
# -*-coding:utf-8 -*

import Contrainte, Blocage, Ressource, Precedence, Obligation, DateLimite
import sys
sys.path.insert(0, "../../")
from src.outils import enum


# Création de l'enum pour la fabrique
Contraintes = enum.enum('BLOCAGE', 'PRECEDENCE', 'OBLIGATION', 'DATE_LIMITE', 'RESSOURCE')


class FabriqueContrainte:
	"""
	Voici la classe qui va se charger de la création des contraintes.
	Via un "enum", il suffira de demander ce que l'on veut
	Et la fabrique nous le fournira directement, si tant est qu'on lui
	fourni les bons matériaux.
	
	@ivar _choix : les choix possibles pour la création d'une contrainte

	USAGE :
		--> créer une Obligation : il faut un nombre en argument
		--> créer une Blocage : il faut un ou plusieurs nombre(s)  en argument
		--> créer une DateLimite : il faut un nombre en argument
		--> créer une Precedence : il faut 2 arguments
	
	@author : Laurent Bardoux p1108365
	@version : 1.0
	"""
	
	def fabrique(self, enumQuoi, *arguments):
		"""
		La méthode qui fabrique une contrainte pour nous.
		Cette méthode à l'avantage d'épargner des importations dans le code
		appellant.

		@param self : L'argument implicite
		@param enumQuoi : Ce que l'on veut fabriquer
		@type enumQuoi : une valeur de l'enum L{Contraintes}
		@param *arguments : les arguments que l'on veut passer lors de la construction
		@type *arguments : dépend de ce que l'on veut
		@return None si la construction a echoué, une Contrainte sinon
		@precondition : enumQuoi est une valeur connue dans L{Contraintes}
		"""
		resultat = self._choix.get(enumQuoi, None)
		if resultat is not None:
			return resultat(*arguments)
		#fin if
		return None
	#fin fabrique
	
	
	def __init__(self):
		"""
		Construit une fabrique de contrainte simple
		Ceci va initialiser le dictionnaire des valeurs possible
		dans le but de réaliser un "switch"
		@param self : L'argument implicite

		Pour ajouter des choix, il suffit alors de rajouter des lignes
		dans _choix avec une lambda ou une fonction qui doit agir le
		cas echeant
		"""
		self._choix = {
			Contraintes.BLOCAGE : lambda *x : Blocage.Blocage(*x),
			Contraintes.PRECEDENCE : lambda x, y : Precedence.Precedence(x, y),
			Contraintes.OBLIGATION : lambda x : Obligation.Obligation(x),
			Contraintes.DATE_LIMITE : lambda x : DateLimite.DateLimite(x),
			Contraintes.RESSOURCE : lambda : Ressource.Ressource()
		}
		
	#fin __init__

#fin FabriqueContrainte
