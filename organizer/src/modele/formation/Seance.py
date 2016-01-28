#!/usr/bin/python
# -*-coding:utf-8 -*



class Seance(object):
	"""
	La classe mere pour tout element d'une formation.
	ELle contient donc toutes les informations communes aux différents
	composant d'une formation:
	@ivar _idSeance : l'identifiant de la Seance
	@ivar _idGroupe : l'identifiant du groupe lié a cette Seance
	@ivar _description : une courte chaine decrivant la seance (facultative)
	@version : 1.0
	@author : Liu Zhuying
	"""
	
	def __init__(self, idSeance, idGroupe, description=""):
		"""
		Le constructeur de la classe "abstraite" Seance.
		@param self : L'argument implicite
		@param idGroupe : l'identifiant du groupe qui aura cette Seance
		@type idGroupe : entier naturel non nul
		@param description : Une courte description de la seance.
		@type description : str
		"""
		if idSeance > 0:
			self._idSeance = idSeance
		else:
			self._idSeance = 1
		if idGroupe > 0:
			self._idGroupe = idGroupe
		else:
			self._idGroupe = 1
		self._description = description
	#fin __init__
	
	
	@property
	def idSeance(self):
		"""
		L'accesseur pour l'id de cette Seance
		@param self : L'argument implicite
		@return : son id
		"""
		return self._idSeance
	#fin idSeance
	
	
	@idSeance.setter
	def idSeance(self, nouvelId):
		"""
		Le mutateur pour l'identifiant de la Seance
		@param self : L'argument implicite
		@param nouvelId : le nouvel identifiant voulu
		@type nouvelid : entier naturel non nul
		"""
		if nouvelId > 0:
			self._idSeance = nouvelId
	#fin idSeance
	
	
	@property
	def idGroupe(self):
		"""
		L'accesseur pour l'id du Groupe
		@param self : L'argument implicite
		@return : l'identifiant du groupe
		"""
		return self._idGroupe
	#fin idGroupe
	
	
	@idGroupe.setter
	def idGroupe(self, nouvelId):
		"""
		Le mutateur pour l'identifiant du Groupe
		@param self : L'argument implicite
		@param nouvelId : le nouvel identifiant voulu
		@type nouvelid : entier naturel non nul
		"""
		if nouvelId > 0:
			self._idGroupe = nouvelId
	#fin idGroupe
	
	
	@property
	def description(self):
		"""
		L'accesseur pour la decription de la seance
		@param self : L'argument implicite
		@return : sa description
		"""
		return self._description
	#fin description
	
	
	@description.setter
	def description(self, nouvelleDescription):
		"""
		Le mutateur pour la description de la seance
		@param self : L'argument implicite
		@param nouvelleDescription : le nouvel identifiant voulu
		@type nouvelleDescription : str
		"""
		self._description = nouvelleDescription
	#fin description
	
#fin Element
