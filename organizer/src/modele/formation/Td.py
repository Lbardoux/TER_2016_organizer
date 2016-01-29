#!/usr/bin/python
# -*-coding:utf-8 -*
import Seance
class Td(Seance.Seance):
	"""
	La classe Td qui hérite la classe seance
	@ivar _numeroType
	@version : 1.0
	@author : Liu Zhuying
	"""
	def __init__(self, idTd, idGroupe, description=""):
		"""
		Le constructeur de la classe Td.
		@param self : L'argument implicite
		@param idTd : l'identifiant du groupe qui aura ce Td
		@type idTd : entier naturel non nul
		@param idGroupe : l'identifiant du groupe qui aura ce Td
		@type idGroupe : entier naturel non nul
		@param description : Une courte description du Td.
		@type description : str
		"""
		super(Td, self).__init__(self, idTd, idGroupe, description)
	#fin __init__
	
	@property
	def idTd(self):
		"""
		L'accesseur pour l'id de ce Td
		@param self : L'argument implicite
		@return : son id
		"""
		return super(Td, self).idSeance()
	#fin idTd
	
	@idTd.setter
	def idCm(self, nouvelId):
		"""
		Le mutateur pour l'identifiant du Td
		@param self : L'argument implicite
		@param nouvelId : le nouvel identifiant voulu
		@type nouvelid : entier naturel non nul
		"""
		super(Td, self).idSeance(nouvelId)
	#fin idTd
	
	@property
	def idGroupe(self):
		"""
		L'accesseur pour l'idgroupe de ce Td
		@param self : L'argument implicite
		@return : son idgroupe
		"""
		return super(Td, self).idGroupe()
	#fin idGroupe
	
	@idGroupe.setter
	def idGroupe(self, nouvelId):
		"""
		Le mutateur pour l'idgroupe du Td
		@param self : L'argument implicite
		@param nouvelId : le nouvel idGroupe voulu
		@type nouvelid : entier naturel non nul
		"""
		super(Td, self).idGroupe(nouvelId)
	#fin idGroupe
	
	
	@property
	def description(self):
		"""
		L'accesseur pour la decription du Td
		@param self : L'argument implicite
		@return : sa description
		"""
		return super(Td, self).description()
	#fin description
	
	
	@description.setter
	def description(self, nouvelleDescription):
		"""
		Le mutateur pour la description du Td
		@param self : L'argument implicite
		@param nouvelleDescription : le nouvel identifiant voulu
		@type nouvelleDescription : str
		"""
		super(Td, self).description(nouvelleDescription)
	#fin description
	
#fin Td
