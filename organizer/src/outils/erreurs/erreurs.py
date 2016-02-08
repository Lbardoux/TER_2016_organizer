#!/usr/bin/python
# -*-coding:utf-8 -*

class NosExceptions(Exception):
	"""
	Décrit un pattern général pour nos Exception.
	@ivar info : un court texte descriptif.
	@author : Laurent Bardoux p1108365
	"""
	
	def __init__(self, info):
		"""
		Le constructeur de cette Exception.
		@param self : L'argument implicite.
		@type info : str
		@param info : le texte descriptif qui accompagne l'exception.
		"""
		self.info = info
	#__init__
	
	
	def __str__(self):
		"""
		Transforme cette exception en une chaine lisible.
		@param self : L'argument implicite.
		@rtype : str
		@return : une chaine détaillant cette exception.
		"""
		return str(type(self)) + " : " + self.info
	#__str__
#NosExceptions


class CreneauInexistant(NosExceptions):
	"""
	Décrit une exception lorsqu'un L{Creneau}, quelqu'il soit, n'a pas été
	trouvé lors d'une recherche.
	@author : Laurent Bardoux p1108365
	"""
	
#CreneauInexistant


class ArgumentInvalide(NosExceptions):
	"""
	Décrit une exception qui doit survenir en cas d'erreur sur les arguments.
	@author : Laurent Bardoux p1108365
	"""
	
#ArgumentInvalide
