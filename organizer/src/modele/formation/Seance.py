#!/usr/bin/python
# -*-coding:utf-8 -*



class Seance(object):
	"""
	La classe mere pour tout element d'une formation.
	ELle contient donc toutes les informations communes aux différents
	composant d'une formation:
	@ivar _idSeance : l'identifiant de la Seance
	@ivar _idGroupe : l'identifiant du groupe lié a cette Seance
	@ivar _duree : la duree de la seance
	@ivar _idEnseignant : l'identifiant de l'ensignant qui se charge de cette seance (facultative)
	@ivar _description : une courte chaine decrivant la seance (facultative)
	@version : 1.0
	@author : Liu Zhuying
	"""
	
	def __init__(self, idSeance, idGroupe, duree, idEnseignant = 0, description = ""):
		"""
		Le constructeur de la classe "abstraite" Seance.
		@param self : L'argument implicite
		@param idSeance : l'identifiant de cette Seance
		@type idSeance : entier naturel non nul
		@param idGroupe : l'identifiant du groupe qui aura cette Seance
		@type idGroupe : entier naturel non nul
		@param duree : la duree qui aura cette Seance
		@type duree : entier naturel non nul
		@param idEnseignant : l'identifiant de l'ensignant de cette Seance
		@type idEnseignant : entier naturel
		@param description : Une courte description de la seance.
		@type description : str
		"""
		if idSeance > 0:
			self._idSeance = idSeance
		else:
			self._idSeance = 1
		#fin if
		
		if idGroupe > 0:
			self._idGroupe = idGroupe
		else:
			self._idGroupe = 1
		#fin if
		
		if duree > 0:
			self._duree = duree
		else:
			self._duree = 1
		#fin if
		
		if idEnseignant >= 0:
			self._idEnseignant = idEnseignant
		else:
			self._idEnseignant = 0
		#fin if
		
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
	def duree(self):
		"""
		L'accesseur pour la duree de cette seance
		@param self : L'argument implicite
		@return : la duree
		"""
		return self._duree
	#fin duree
	
	
	@duree.setter
	def duree(self, nouvelleDuree):
		"""
		Le mutateur pour la duree de cette seance
		@param self : L'argument implicite
		@param nouvelleDuree : la nouvelle duree voulue
		@type nouvelleDuree : entier naturel non nul
		"""
		if nouvelleDuree > 0:
			self._duree = nouvelleDuree
	#fin duree
	
	@property
	def idEnseignant(self):
		"""
		L'accesseur pour l'identifiant de l'enseignant
		@param self : L'argument implicite
		@return : l'identifiant du groupe
		"""
		return self._idEnseignant
	#fin idEnseignant
	
	
	@idEnseignant.setter
	def idEnseignant(self, nouvelId):
		"""
		Le mutateur pour l'identifiant de l'enseignant
		@param self : L'argument implicite
		@param nouvelId : le nouvel identifiant voulu
		@type nouvelid : entier naturel non nul
		"""
		if nouvelId > 0:
			self._idEnseignant = nouvelId
	#fin idEnseignant
	
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
	
#fin Seance
