#!/usr/bin/python
# -*-coding:utf-8 -*
import Seance
class Examen(Seance.Seance):
	"""
	La classe Examen qui hérite la classe seance
	@ivar _numeroType
	@version : 1.0
	@author : Liu Zhuying
	"""
	def __init__(self, idExamen, idGroupe, description=""):
		"""
		Le constructeur de la classe Examen.
		@param self : L'argument implicite
		@param idExamen : l'identifiant du groupe qui aura cet Examen
		@type idExamen : entier naturel non nul
		@param idGroupe : l'identifiant du groupe qui aura cet Examen
		@type idGroupe : entier naturel non nul
		@param description : Une courte description de l'Examen.
		@type description : str
		"""
		super(Examen, self).__init__(self, idExamen, idGroupe, description)
	#fin __init__
	
	@property
	def idExamen(self):
		"""
		L'accesseur pour l'id de cet Examen
		@param self : L'argument implicite
		@return : son id
		"""
		return super(Examen, self).idSeance()
	#fin idExamen
	
	@idExamen.setter
	def idExamen(self, nouvelId):
		"""
		Le mutateur pour l'identifiant de l'Examen
		@param self : L'argument implicite
		@param nouvelId : le nouvel identifiant voulu
		@type nouvelid : entier naturel non nul
		"""
		super(Examen, self).idSeance(nouvelId)
	#fin idExamen
	
	@property
	def idGroupe(self):
		"""
		L'accesseur pour l'idgroupe de cet Examen
		@param self : L'argument implicite
		@return : son idgroupe
		"""
		return super(Examen, self).idGroupe()
	#fin idGroupe
	
	@idGroupe.setter
	def idGroupe(self, nouvelId):
		"""
		Le mutateur pour l'idgroupe de l'Examen
		@param self : L'argument implicite
		@param nouvelId : le nouvel idGroupe voulu
		@type nouvelid : entier naturel non nul
		"""
		super(Examen, self).idGroupe(nouvelId)
	#fin idGroupe
	
	
	@property
	def description(self):
		"""
		L'accesseur pour la decription de l'Examen
		@param self : L'argument implicite
		@return : sa description
		"""
		return super(Examen, self).description()
	#fin description
	
	
	@description.setter
	def description(self, nouvelleDescription):
		"""
		Le mutateur pour la description de l'Examen
		@param self : L'argument implicite
		@param nouvelleDescription : le nouvel identifiant voulu
		@type nouvelleDescription : str
		"""
		super(Examen, self).description(nouvelleDescription)
	#fin description
	
#fin Examen
