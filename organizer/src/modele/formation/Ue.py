#!/usr/bin/python
# -*-coding:utf-8 -*

class Ue(object):
	"""
	La classe qui représente une unité d'enseignement.
	@ivar _code : le code UE, par exemple : MIF18, LIF15
	@ivar _nom : le nom de UE, par exemple : Base de données avancée
	@ivar _idEnseignant : l'identifiant du responsable de l'Ue
	@ivar _nombreInscrit : le nombre d'etudiants inscrits dans cette Ue
	@ivar _nombreGroupe : le nombre de groupes de cette Ue 
	@ivar _nombreCm : Le nombre de Cms que contient cette Ue
	@ivar _nombreTd : Le nombre de Tds que contient cette Ue
	@ivar _nombreTp : Le nombre de Tps que contient cette Ue
	@ivar _nombreExamen : Le nombre de Examens que contient cette Ue
	@ivar _nombreAutre : Le nombre de séances autre que CM TD TP Examen
	@ivar _listeSeance : La liste des seances que cette Ue contient
	@version : 1.0
	@author : Liu Zhuying
	"""
	def __init__(self, code, nom, id_enseignant):
		"""
		Le constructeur de la classe Enseignant.
		@param self : L'argument implicite
		@param code : l'identifiant que cet enseignant aura
		@type code : str
		@param nom : le nom que cet enseignant aura
		@type nom : str
		@param id_enseignant : le prenom que cet enseignant aura
		@type id_enseignant : entier naturel non nul
		"""
		self._code = code
		self._nom = nom
		
		if id_enseignant > 0:
			self._idEnseignant = id_enseignant
		else:
			self._idEnseignant = 1
		#fin if
		self._nombreInscrit = 1
		self._nombreGroupe = 1
		self._nombreCm = 0
		self._nombreTd = 0
		self._nombreTp = 0
		self._nombreExamen = 0
		self._nombreAutre = 0
		self._listeSeance = []
	#fin __init__
	
	"""
	def setNombreCm(self, nombre):
		"""
		"""
		self._nombreCm = nombre	
	#fin setNombreCm
	
	
	def setNombreTd(self, nombre):
		"""
		"""
		self._nombreTd = nombre	
	#fin setNombreTd
	
	
	def setNombreTp(self, nombre):
		"""
		"""
		self._nombreTp = nombre	
	#fin setNombreTp
	
	
	def setNombreExamen(self, nombre):
		"""
		"""
		self._nombreExamen = nombre	
	#fin setNombreExamen
	
	
	def setNombreAutre(self, nombre):
		"""
		"""
		self._nombreAutre = nombre	
	#fin setNombreAutre
	
	def ajouterSeance(self, Seance):
		"""
		"""
		#if type(element) is Element:
		#	self._listeElement.insert(element)
		#fin if
		
	#fin ajouterSeance
	"""	
#fin Ue
	
