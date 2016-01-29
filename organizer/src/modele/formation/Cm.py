#!/usr/bin/python
# -*-coding:utf-8 -*
import Seance
class Cm(Seance.Seance):
	"""
	La classe Cm qui hérite la classe seance
	@ivar _numeroType
	@version : 1.0
	@author : Liu Zhuying
	"""
	def __init__(self, idCm, idGroupe, description=""):
		"""
		Le constructeur de la classe cm.
		@param self : L'argument implicite
		@param idCm : l'identifiant du groupe qui aura ce cm
		@type idCm : entier naturel non nul
		@param idGroupe : l'identifiant du groupe qui aura ce cm
		@type idGroupe : entier naturel non nul
		@param description : Une courte description du cm.
		@type description : str
		"""
		super(Cm, self).__init__(self, idCm, idGroupe, description)
	#fin __init__
	
	@property
	def idCm(self):
		"""
		L'accesseur pour l'id de ce Cm
		@param self : L'argument implicite
		@return : son id
		"""
		return super(Cm, self).idSeance()
	#fin idCm
	
	@idCm.setter
	def idCm(self, nouvelId):
		"""
		Le mutateur pour l'identifiant du Cm
		@param self : L'argument implicite
		@param nouvelId : le nouvel identifiant voulu
		@type nouvelid : entier naturel non nul
		"""
		super(Cm, self).idSeance(nouvelId)
	#fin idCm
	
	@property
	def idGroupe(self):
		"""
		L'accesseur pour l'idgroupe de ce Cm
		@param self : L'argument implicite
		@return : son idgroupe
		"""
		return super(Cm, self).idGroupe()
	#fin idGroupe
	
	@idGroupe.setter
	def idGroupe(self, nouvelId):
		"""
		Le mutateur pour l'idgroupe du Cm
		@param self : L'argument implicite
		@param nouvelId : le nouvel idGroupe voulu
		@type nouvelid : entier naturel non nul
		"""
		super(Cm, self).idGroupe(nouvelId)
	#fin idGroupe
	
	
	@property
	def description(self):
		"""
		L'accesseur pour la decription du Cm
		@param self : L'argument implicite
		@return : sa description
		"""
		return super(Cm, self).description()
	#fin description
	
	
	@description.setter
	def description(self, nouvelleDescription):
		"""
		Le mutateur pour la description du cm
		@param self : L'argument implicite
		@param nouvelleDescription : le nouvel identifiant voulu
		@type nouvelleDescription : str
		"""
		super(Cm, self).description(nouvelleDescription)
	#fin description
	
#fin Cm
