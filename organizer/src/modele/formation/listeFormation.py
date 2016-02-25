#!/usr/bin/python3
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
		@param self: L'argument implicite
		"""
		self._liste = []
	#__init__
	
	@property
	def taille(self):
		"""La taille de cette liste"""
		return len(self._liste)
	#taille
	
	@property
	def liste(self):
		"""La liste complete"""
		return self._liste
	#liste
	
	def ajouterFormation(self, nouvelle):
		"""
		La fonction qui ajoute une formation dans cette liste
		@param self: L'argument implicite
		@param nouvelle: la formation à ajouter
		@type nouvelle: une formation 
		"""
		if type(nouvelle) is Formation: 
			self._liste.append(nouvelle)
	#ajouterFormation
	
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
				#if
			#for
		#if
	#supprimerFormation
	
#ListeFormation
