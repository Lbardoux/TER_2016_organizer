#!/usr/bin/python3
# -*-coding:utf-8 -*
class Enseignant(object): 
	"""
	La classe qui représente une salle.
	@ivar _idEnseignant: l'identifiant de l'enseignant
	@ivar _nom: le nom de l'enseignant
	@ivar _prenom: le prenom de l'enseignant 
	@version: 1.0
	@author: Liu Zhuying
	"""
	def __init__(self, id_enseignant, nom, prenom):
		"""
		Le constructeur de la classe Enseignant.
		@param self: L'argument implicite
		@param id_enseignant: l'identifiant que cet enseignant aura
		@type id_enseignant: entier naturel non nul
		@param nom: le nom que cet enseignant aura
		@type nom: str
		@param prenom: le prenom que cet enseignant aura
		@type prenom: str
		"""
		if id_enseignant > 0: 
			self._idEnseignant = id_enseignant
		else:
			self._idEnseignant = 1
		#if
		if bool(nom.strip()):	
			self._nom = nom
		else:
			self._nom = "DEFAUT"
		#if
		if bool(prenom.strip()):	
			self._prenom = prenom
		else:
			self._prenom = "DEFAUT"
		#if	
		
	#__init__
	
	@property
	def idEnseignant(self):
		"""L'accesseur pour l'id de cet Enseignant"""
		return self._idEnseignant
	#idEnseignant
	
	@idEnseignant.setter
	def idEnseignant(self, nouvelId):
		"""Le mutateur pour l'identifiant de l'enseignant"""
		if nouvelId > 0:
			self._idEnseignant = nouvelId
		#if
	#idEnseignant
	
	@property
	def nom(self):
		"""L'accesseur pour le nom de cet Enseignant"""
		return self._nom
	#nom
	
	@nom.setter
	def nom(self, nouveauNom):
		"""Le mutateur pour le nom de l'enseignant"""
		if nouveauNom.strip():
			self._nom = nouveauNom
	#nom
	
	@property
	def prenom(self):
		"""L'accesseur pour le prenom de cet Enseignant"""
		return self._prenom
	#prenom
	
	@prenom.setter
	def prenom(self, nouveauPrenom):
		"""Le mutateur pour le prenom de l'enseignant"""
		if nouveauPrenom.strip():
			self._prenom = nouveauPrenom
	#prenom
	
#Enseignant
