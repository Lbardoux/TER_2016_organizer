#!/usr/bin/python33
# -*-coding:utf-8 -*

import Contrainte

class Precedence(Contrainte.Contrainte):
	"""
	La classe qui définit une contrainte de précédence (ie un element
	du cursus doit avoir lieu avant un autre, par exemple un CM doit
	avoir lieu avant le TP associé.
	@ivar _idAvant: l'identifiant de l'element qui passe en premier
	@ivar _idEnsuite: l'identifiant de l'element qui passe en premier
	@author: Laurent Bardoux p1108365
	@version: 1.0
	"""
	
	def __init__(self, idAvant, idEnsuite):
		"""
		Le constructeur de cette contrainte
		@param self: L'argument implicite
		@param idAvant: l'identifiant de l'élément qui doit avoir lieu en premier
		@param idEnsuite: l'identifiant de l'élément qui doit avoir lieu après le 1er.
		"""
		# ici il faut que la classe de base herite de (object)
		#super(Precedence, self).__init__(self)
		
		#solution alternative
		Contrainte.Contrainte.__init__(self)
		self._idAvant = idAvant
		self._idEnsuite = idEnsuite
		
	#fin __init__
	
	
	def injectionContrainte(self):
		"""
		Renvoi une lambda expression correspondant à une relation
		de précédence entre _idAvant et _idEnsuite
		
		@param self: l'argument implicite
		@return: une lambda expression renvoyant M{avant < ensuite}
		"""
		return lambda x, y : x < y
	#fin injectionContrainte


	def idAvant(self):
		"""
		Un accesseur pour l'identifiant de l'element qui doit avoir
		lieu en premier
		@param self: L'argument implicite
		@postcondition: Aucune modification de l'objet
		@return: l'identifiant de l'élément
		"""
		return self._idAvant
	#fin idAvant
	
	
	def idEnsuite(self):
		"""
		Un accesseur pour l'identifiant de l'element qui doit avoir
		lieu en premier
		@param self: L'argument implicite
		@postcondition: Aucune modification de l'objet
		@return: l'identifiant de l'élément
		"""
		return self._idEnsuite
	#fin idEnsuite
	
#fin Precedence
