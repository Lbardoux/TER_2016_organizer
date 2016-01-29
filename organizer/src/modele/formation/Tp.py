#!/usr/bin/python
# -*-coding:utf-8 -*
import Seance
class Tp(Seance.Seance):
	"""
	La classe tp qui hérite la classe seance
	@ivar _numeroType
	@version : 1.0
	@author : Liu Zhuying
	"""
	def __init__(self, idTp, idGroupe, description=""):
		"""
		Le constructeur de la classe tp.
		@param self : L'argument implicite
		@param idTp : l'identifiant du groupe qui aura ce tp
		@type idTp : entier naturel non nul
		@param idGroupe : l'identifiant du groupe qui aura ce tp
		@type idGroupe : entier naturel non nul
		@param description : Une courte description du tp.
		@type description : str
		"""
		super(Tp, self).__init__(self, idTp, idGroupe, description)
	#fin __init__
	
	@property
	def idTp(self):
		"""
		L'accesseur pour l'id de ce Tp
		@param self : L'argument implicite
		@return : son id
		"""
		return super(Tp, self).idSeance()
	#fin idTp
	
	@idTp.setter
	def idTp(self, nouvelId):
		"""
		Le mutateur pour l'identifiant du tp
		@param self : L'argument implicite
		@param nouvelId : le nouvel identifiant voulu
		@type nouvelid : entier naturel non nul
		"""
		super(Tp, self).idSeance(nouvelId)
	#fin idTp
	
	@property
	def idGroupe(self):
		"""
		L'accesseur pour l'idgroupe de ce Tp
		@param self : L'argument implicite
		@return : son idgroupe
		"""
		return super(Tp, self).idGroupe()
	#fin idGroupe
	
	@idGroupe.setter
	def idGroupe(self, nouvelId):
		"""
		Le mutateur pour l'idgroupe du tp
		@param self : L'argument implicite
		@param nouvelId : le nouvel idGroupe voulu
		@type nouvelid : entier naturel non nul
		"""
		super(Tp, self).idGroupe(nouvelId)
	#fin idGroupe
	
	
	@property
	def description(self):
		"""
		L'accesseur pour la decription du tp
		@param self : L'argument implicite
		@return : sa description
		"""
		return super(Tp, self).description()
	#fin description
	
	
	@description.setter
	def description(self, nouvelleDescription):
		"""
		Le mutateur pour la description du cm
		@param self : L'argument implicite
		@param nouvelleDescription : le nouvel identifiant voulu
		@type nouvelleDescription : str
		"""
		super(Tp, self).description(nouvelleDescription)
	#fin description
	
#fin Tp
