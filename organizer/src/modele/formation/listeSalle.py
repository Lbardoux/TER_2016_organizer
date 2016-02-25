#!/usr/bin/python
# -*-coding:utf-8 -*
import Salle
class ListeSalle(object):
	"""
	La classe qui contient une liste de salles
	@ivar _liste: La liste de salles
	@author: Zhuying LIU
	@version: 1.0
	"""
	def __init__(self):
		"""
		Le constructeur de la liste de salles
		Par défaut la liste et vide
		@param self : L'argument implicite
		"""
		self._liste = []
	#__init__
	
	@property
	def taille(self):
		"""
		La taille de cette liste
		"""
		return len(self._liste)
	#taille
	
	@property
	def liste(self):
		"""
		La liste complete
		"""
		return self._liste
	#liste
	
	def ajouterSalle(self, nouvelle):
		"""
		La fonction qui ajoute une salle dans cette liste
		@param self: L'argument implicite
		@param nouvelle: la salle à ajouter
		@type nouvelle: une salle 
		"""
		if type(nouvelle) is Salle: 
			self._liste.append(nouvelle)
	#ajouterSalle
	
	def supprimerSalle(self, uneSalle):
		"""
		La fonction qui supprime une salle dans cette liste
		@param self: L'argument implicite
		@param uneSalle: la salle à supprimer
		@type uneSalle: une salle dans cette liste
		"""
		if type(uneSalle) is Salle: 
			for i in self._liste:
				if(i.idSalle == uneSalle.idSalle):
					self._liste.remove(i)
					break
				#if
			#for
		#if
	#supprimerSalle
	
#ListeSalle
