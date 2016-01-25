#!/usr/bin/python
# -*-coding:utf-8 -*


class Precedence(Contrainte):
	"""
	La classe qui définit une contrainte de précédence (ie un element
	du cursus doit avoir lieu avant un autre, par exemple un CM doit
	avoir lieu avant le TP associé.
	
	@ivar _id_avant: l'identifiant de l'element qui passe en premier
	@ivar _id_ensuite: l'identifiant de l'element qui passe en premier
	
	@author: Laurent Bardoux p1108365
	@version: 1.0
	"""
	
	def __init__(self, id_avant, id_ensuite):
		"""
		Le constructeur de cette contrainte
		@param self: L'argument implicite
		@param id_avant: l'identifiant de l'élément qui doit avoir lieu
			en premier
		@param id_ensuite: l'identifiant de l'élément qui doit avoir 
			lieu après le 1er.
		"""
		super(Precedence, self).__init__(self)
		self._id_avant = id_avant
		self._id_ensuite = id_ensuite
		
	#fin __init__


	def contrainte(self):
		"""
		
		"""
		return ""
	#fin contrainte
	
#fin Precedence
