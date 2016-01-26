#!/usr/bin/python
# -*-coding:utf-8 -*

import Contrainte

class DateLimite(Contrainte.Contrainte):
	"""
	La classe qui définit une deadline dans l'ordonnancement
	Par exemple, Tel cours doit se finir avant 18h, ou telle UE avant
	telle date.
	
	@ivar _limite : la limite numérique a ne pas atteindre/dépasser
	
	@author : Laurent Bardoux p1108365
	@version : 1.0
	"""
	
	def __init__(self, limite):
		"""
		Le constructeur de cette contrainte.
		@param self : l'argument implicite.
		@type limite : un entier.
		@param limite : la valeur maximale (exclue).
		@postcondition : L'objet est bien initialisé.
		"""
		self._limite = limite
		
	#fin __init__
	
	
	def injectionContrainte(self):
		"""
		La fonction polymorphique qui injecte une lambda expression
		correspondant à cette contrainte.
		@param self: l'argument implicite
		@return une lambda exprimant cette limite M{pour tout x, x < _limite}
		"""
		return lambda x : x < self._limite
	#fin injectionContrainte
	
	
	def limite(self):
		"""
		Un accesseur pour la limite de cette contrainte.
		@param self: l'argument implicite
		@return la valeur entière représentant cette L{deadline}
		"""
		return self._limite
	#fin limite
	
#fin DateLimite
