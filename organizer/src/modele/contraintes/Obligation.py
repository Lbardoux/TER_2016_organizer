#!/usr/bin/python3
# -*-coding:utf-8 -*

import Contrainte

class Obligation(Contrainte.Contrainte):
	"""
	Cette classe définit une contrainte qui impose quelque chose.
	Comme, par exemple, imposer un horaire pour un cours.
	@ivar _valeur: La valeur imposée, tel que M{_valeur >= 0}
	@author: Laurent Bardoux p1108365
	@version: 1.0
	"""
	def __init__(self, valeur):
		"""
		Le constructeur de cette contrainte.
		@param self: L'argument implicite.
		@param valeur: La valeur voulue pour obliger
		@type valeur: entier naturel.
		@precondition: M{valeur >= 0}, et M{self != None}
		@postcondition: self est initialisé correctement.
		"""
		self._valeur = valeur
	#fin __init__
	
	
	def injectionContrainte(self):
		"""
		La fonction qui va injecter une lambda expression imposant une
		valeur à son argument.
		Cette lambda renverra true si cette condition est bien respectée.
		@param self: L'argument implicite.
		@precondition: M{self != None}
		@return: Une lambda expression M{f(x) = (x==valeur) ? true : false}
		"""
		return lambda x : x == self._valeur
	#fin injectionContrainte
	
	
	def valeur(self):
		"""
		L'accesseur pour la valeur de cette contrainte.
		@param self: L'argument implicite.
		@precondition: M{self != None}
		@postcondition: Cette valeur n'est pas modifiée après l'appel.
		"""
		return self._valeur
	#fin valeur
	
#fin Obligation
