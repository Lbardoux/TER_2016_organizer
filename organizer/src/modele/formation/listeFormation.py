#!/usr/bin/python
# -*-coding:utf-8 -*
from Formation import Formation
class ListeFormation(object):
	"""
	La classe qui contient une liste de formations
	@ivar _liste: La liste de formations
	@author: Zhuying LIU
	@version: 1.0
	"""
	def __init__(self):
		"""
		Le constructeur de la liste de formations
		Par défaut la liste et vide
		@param self : L'argument implicite
		"""
		self._liste = []
	#fin __init__
	
	@property
	def taille(self):
		"""
		La taille de cette liste
		"""
		return len(self._liste)
	#fin taille
	
	@property
	def liste(self):
		"""
		La liste complete
		"""
		return self._liste
	#fin liste
	
	def ajouterFormation(self, nouvelle):
		"""
		La fonction qui ajoute une formation dans cette liste
		@param self: L'argument implicite
		@param uneFormation: la formation à ajouter
		@type uneFormation: une formation 
		"""
		if type(nouvelle) is Formation: 
			self._liste.append(nouvelle)
	#fin ajouterFormation
	
	def supprimerFormation(self, uneFormation):
		"""
		La fonction qui supprime une formation dans cette liste
		@param self: L'argument implicite
		@param uneFormation: la formation à supprimer
		@type uneFormation: une formation dans cette liste
		"""
		if type(uneFormation) is Formation: 
			for i in self._liste:
				if(i.idFormation == uneFormation.idFormation):
					self._liste.remove(i)
					break
				#fin if
			#fin for
		#fin if
	#fin supprimerFormation
	
#fin ListeFormation
