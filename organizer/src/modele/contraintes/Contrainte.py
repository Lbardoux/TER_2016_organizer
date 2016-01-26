#!/usr/bin/python
# -*-coding:utf-8 -*

class Contrainte:
	"""
	La classe abstraite qui va permettre le polymorphisme pour une
	contrainte.
	Elle ne devra pas etre instanciée telle qu'elle.
	
	@author: Laurent Bardoux p1108365
	@version: 1.0
	"""
	
	def __init__(self):
		"""
		Le constructeur de cette classe, qui sera utilisé dans les 
		classes dérivées.
		@param self: Le paramètre implicite lors de l'appel.
		@precondition: M{self != None}
		@postcondition: l'objet est initialisé et pret à l'emploi.
		"""
	
	#fin __init__
	
	
	def injection_contrainte(self):
		"""
		Cette fonction doit renvoyer une lambda expression pour appliquer
		la contrainte qu'elle spécifie.
		
		@param self: L'argument implicite de la classe
		
		@return : une lambda expression
		
		"""
		
		
	#fin injection_contrainte
	
#fin Contrainte

