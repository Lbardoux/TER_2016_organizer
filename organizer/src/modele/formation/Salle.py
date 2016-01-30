#!/usr/bin/python
# -*-coding:utf-8 -*
class Salle(object):
	"""
	La classe qui représente une salle.
	@ivar _idSalle : l'identifiant de la salle
	@ivar _taille : le nombre de personnes que cette salle peut contenir 
	@ivar _typeSalle : le type de cette salle(salle TP, salle TD, labo) pour les futures fonctionnalités 
	@version : 1.0
	@author : Liu Zhuying
	"""
	def __init__(self, id_salle, taille, typeSalle = 0):
		"""
		Le constructeur de la classe salle.
		@param self : L'argument implicite
		@param id_salle : l'identifiant que cette salle aura
		@type id_salle : entier naturel non nul
		@param taille : la taille que cette salle aura
		@type taille : entier naturel non nul
		@param typeSalle : le type de cette salle.(falcultatif)
		@type typeSalle : entier naturel
		"""
		if id_salle > 0:
			self._idSalle = id_salle
		else:
			self.idSalle = 1
		#fin if
		if taille > 0:
			self._taille = taille
		else:
			self._taille = 1
		#fin if
		self._typeSalle = typeSalle	
	#fin __init__
	
	@property
	def idSalle(self):
		"""
		L'accesseur pour l'id de cette salle
		@param self : L'argument implicite
		@return : son id
		"""
		return self._idSalle
	#fin idSalle
	
	@idSalle.setter
	def idSalle(self, nouvelId):
		"""
		Le mutateur pour l'identifiant de la salle
		@param self : L'argument implicite
		@param nouvelId : le nouvel identifiant voulu
		@type nouvelid : entier naturel non nul
		"""
		if nouvelId > 0:
			self._idSalle = nouvelId
	#fin idSalle
	
	@property
	def taille(self):
		"""
		L'accesseur pour la taille de cette salle
		@param self : L'argument implicite
		@return : sa taille
		"""
		return self._taille
	#fin taille
	
	@taille.setter
	def taille(self, nouvelleTaille):
		"""
		Le mutateur pour la taille de la salle
		@param self : L'argument implicite
		@param nouvelleTaille : la nouvelle taille voulue
		@type nouvelleTaille : entier naturel non nul
		"""
		if nouvelleTaille > 0:
			self._taille = nouvelleTaille
	#fin taille
	
	@property
	def typeSalle(self):
		"""
		L'accesseur pour le type de cette salle
		@param self : L'argument implicite
		@return : son type
		"""
		return self._typeSalle
	#fin typeSalle
	
	@typeSalle.setter
	def typeSalle(self, nouveauType):
		"""
		Le mutateur pour le type de la salle
		@param self : L'argument implicite
		@param nouveauType : le nouveau type voulu
		@type nouveauType : entier naturel
		"""
		self._typeSalle = nouveauType
	#fin typeSalle
	
#fin Salle
