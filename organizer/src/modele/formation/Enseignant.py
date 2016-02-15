#!/usr/bin/python3
# -*-coding:utf-8 -*
class Enseignant(object): 
	"""
	La classe qui représente une salle.
	@ivar _idEnseignant : l'identifiant de l'enseignant
	@ivar _nom : le nom de l'enseignant
	@ivar _prenom : le prenom de l'enseignant 
	@version : 1.0
	@author : Liu Zhuying
	"""
	def __init__(self, id_enseignant, nom, prenom):
		"""
		Le constructeur de la classe Enseignant.
		@param self : L'argument implicite
		@param id_enseignant : l'identifiant que cet enseignant aura
		@type id_enseignant : entier naturel non nul
		@param nom : le nom que cet enseignant aura
		@type nom : str
		@param prenom : le prenom que cet enseignant aura
		@type prenom : str
		"""
		if id_enseignant > 0: 
			self._idEnseignant = id_enseignant
		else:
			self._idEnseignant = 1
		#fin if
		if bool(nom.strip()):	
			self._nom = nom
		else:
			self._nom = "DEFAUTE"
		#fin if
		if bool(prenom.strip()):	
			self._prenom = prenom
		else:
			self._prenom = "DEFAUTE"
		#fin if	
		
	#fin __init__
	
	@property
	def idEnseignant(self):
		"""
		L'accesseur pour l'id de cet Enseignant
		@param self : L'argument implicite
		@return : son id
		"""
		return self._idEnseignant
	#fin idEnseignant
	
	@idEnseignant.setter
	def idEnseignant(self, nouvelId):
		"""
		Le mutateur pour l'identifiant de l'enseignant
		@param self : L'argument implicite
		@param nouvelId : le nouvel identifiant voulu
		@type nouvelId : entier naturel non nul
		"""
		if nouvelId > 0:
			self._idEnseignant = nouvelId
		#fin if
	#fin idEnseignant
	
	@property
	def nom(self):
		"""
		L'accesseur pour le nom de cet Enseignant
		@param self : L'argument implicite
		@return : son nom
		"""
		return self._nom
	#fin nom
	
	@nom.setter
	def nom(self, nouveauNom):
		"""
		Le mutateur pour le nom de l'enseignant
		@param self : L'argument implicite
		@param nouveauNom : le nouveau nom voulu
		@type nouveauNom : str
		"""
		if nouveauNom.strip():
			self._nom = nouveauNom
	#fin nom
	
	@property
	def prenom(self):
		"""
		L'accesseur pour le prenom de cet Enseignant
		@param self : L'argument implicite
		@return : son prenom
		"""
		return self._prenom
	#fin prenom
	
	@prenom.setter
	def prenom(self, nouveauPrenom):
		"""
		Le mutateur pour le prenom de l'enseignant
		@param self : L'argument implicite
		@param nouveauPrenom : le nouveau prenom voulu
		@type nouveauPrenom : str
		"""
		if nouveauPrenom.strip():
			self._prenom = nouveauPrenom
	#fin prenom
	
#fin Enseignant
