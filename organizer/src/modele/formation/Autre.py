#!/usr/bin/python
# -*-coding:utf-8 -*
import Seance
class Autre(Seance.Seance):
	"""
	La classe Autre qui hérite la classe seance
	@ivar _numeroType
	@version : 1.0
	@author : Liu Zhuying
	"""
	def __init__(self, idAutre, idGroupe, description=""):
		"""
		Le constructeur de la classe Autre.
		@param self : L'argument implicite
		@param idAutre : l'identifiant du groupe qui aura cet Autre
		@type idAutre : entier naturel non nul
		@param idGroupe : l'identifiant du groupe qui aura cet Autre
		@type idGroupe : entier naturel non nul
		@param description : Une courte description du Autre.
		@type description : str
		"""
		super(Autre, self).__init__(self, idAutre, idGroupe, description)
	#fin __init__
	
	@property
	def idAutre(self):
		"""
		L'accesseur pour l'id de cet Autre
		@param self : L'argument implicite
		@return : son id
		"""
		return super(Autre, self).idSeance()
	#fin idAutre
	
	@idAutre.setter
	def idCm(self, nouvelId):
		"""
		Le mutateur pour l'identifiant de l'Autre
		@param self : L'argument implicite
		@param nouvelId : le nouvel identifiant voulu
		@type nouvelid : entier naturel non nul
		"""
		super(Autre, self).idSeance(nouvelId)
	#fin idAutre
	
	@property
	def idGroupe(self):
		"""
		L'accesseur pour l'idgroupe de cet Autre
		@param self : L'argument implicite
		@return : son idgroupe
		"""
		return super(Autre, self).idGroupe()
	#fin idGroupe
	
	@idGroupe.setter
	def idGroupe(self, nouvelId):
		"""
		Le mutateur pour l'idgroupe de l'Autre
		@param self : L'argument implicite
		@param nouvelId : le nouvel idGroupe voulu
		@type nouvelid : entier naturel non nul
		"""
		super(Autre, self).idGroupe(nouvelId)
	#fin idGroupe
	
	
	@property
	def description(self):
		"""
		L'accesseur pour la decription de l'Autre
		@param self : L'argument implicite
		@return : sa description
		"""
		return super(Autre, self).description()
	#fin description
	
	
	@description.setter
	def description(self, nouvelleDescription):
		"""
		Le mutateur pour la description de l'Autre
		@param self : L'argument implicite
		@param nouvelleDescription : le nouvel identifiant voulu
		@type nouvelleDescription : str
		"""
		super(Autre, self).description(nouvelleDescription)
	#fin description
	
#fin Autre
