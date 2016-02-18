#!/usr/bin/python3
# -*-coding:utf-8 -*

from Seance import Seance
from FabriqueCreneau import CreneauxPossible as CP


class Ue(object):
	"""
	La classe qui représente une unité d'enseignement.
	@ivar _code: le code UE, par exemple : MIF18, LIF15
	@ivar _nom: le nom de UE, par exemple : Base de données avancée
	@ivar _idEnseignant: l'identifiant du responsable de l'Ue
	@ivar _nombreInscrit: le nombre d'etudiants inscrits dans cette Ue
	@ivar _nombreGroupe: le nombre de groupes de cette Ue 
	@ivar _nombreCm: Le nombre de Cms que contient cette Ue
	@ivar _nombreTd: Le nombre de Tds que contient cette Ue
	@ivar _nombreTp: Le nombre de Tps que contient cette Ue
	@ivar _nombreExamen: Le nombre de Examens que contient cette Ue
	@ivar _nombreAutre: Le nombre de séances autre que CM TD TP Examen
	@ivar _listeSeance: La liste des seances que cette Ue contient
	@version: 1.0
	@author: Liu Zhuying
	"""
	
	def __init__(self, code, nom, id_enseignant):
		"""
		Le constructeur de la classe Enseignant.
		@param self: L'argument implicite
		@param code: l'identifiant que cet enseignant aura
		@type code: str
		@param nom: le nom que cet enseignant aura
		@type nom: str
		@param id_enseignant: le prenom que cet enseignant aura
		@type id_enseignant: entier naturel non nul
		"""
		self._code = code if bool(code.strip()) else "Code Null"
		self._nom = nom if bool(nom.strip()) else "Nom Par Defaut"
		self._idEnseignant = id_enseignant if id_enseignant > 0 else 1
		
		self._nombreInscrit = 1
		self._nombreGroupe = 1
		self._nombreCm = 0
		self._nombreTd = 0
		self._nombreTp = 0
		self._nombreExamen = 0
		self._nombreAutre = 0
		self._listeSeance = []
	#__init__
	
	
	@property
	def code(self):
		"""L'accesseur pour le code de cette Ue"""
		return self._code
	#code
	
	
	@code.setter
	def code(self, nouveauCode):
		"""Le mutateur pour le code de cette Ue"""
		if bool(nouveauCode.strip()):
			self._code = nouveauCode
		#if
	#code
	
	
	@property
	def nom(self):
		"""L'accesseur pour le nom de cette Ue"""
		return self._nom
	#nom
	
	
	@nom.setter
	def nom(self, nouveauNom):
		"""Le mutateur pour le nom de cette Ue"""
		if bool(nouveauNom.strip()):
			self._nom = nouveauNom
		#if
	#nom
	
	
	@property
	def idEnseignant(self):
		"""L'accesseur pour l'identifiant de l'enseignant"""
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
	def nombreInscrit(self):
		"""L'accesseur pour le nombre d'inscrits de cette Ue"""
		return self._nombreInscrit
	#nombreInscrit
	
	
	@nombreInscrit.setter
	def nombreInscrit(self, nouveauNombre):
		"""Le mutateur pour le nombre d'inscrits de cette Ue"""
		if nouveauNombre > 0:
			self._nombreInscrit = nouveauNombre
		#if
	#nombreInscrit
	
	
	@property
	def nombreGroupe(self):
		"""L'accesseur pour le nombre de Groupes de cette Ue"""
		return self._nombreGroupe
	#nombreGroupe
	
	
	@nombreGroupe.setter
	def nombreGroupe(self, nouveauNombre):
		"""Le mutateur pour le nombre de groupes de cette Ue"""
		if nouveauNombre > 0 and nouveauNombre <= self._nombreInscrit:
			self._nombreGroupe = nouveauNombre
		#if
	#nombreGroupe
	
	
	@property
	def nombreSeance(self):
		"""L'accesseur pour le nombre de Cms de cette Ue"""
		return len(self._listeSeance)
	#nombreCm
	
	
	@property
	def nombreCm(self):
		"""L'accesseur pour le nombre de Cms de cette Ue"""
		return self._nombreCm
	#nombreCm
	
	
	@property
	def nombreTd(self):
		"""L'accesseur pour le nombre de Tds de cette Ue"""
		return self._nombreTd
	#nombreTd
	
	
	@property
	def nombreTp(self):
		"""L'accesseur pour le nombre de Tps de cette Ue"""
		return self._nombreTp
	#nombreTp
	
	
	@property
	def nombreExamen(self):
		"""L'accesseur pour le nombre d'Examens de cette Ue"""
		return self._nombreExamen
	#nombreExamen
	
	
	@property
	def nombreAutre(self):
		"""L'accesseur pour le nombre d'Autres de cette Ue"""
		return self._nombreAutre
	#nombreAutre
	
	
	@property
	def listeSeance(self):
		"""L'accesseur pour la liste de Seances de cette Ue"""
		return self._listeSeance
	#listeSeance
	
	
	@property
	def listeCm(self):
		"""La fonction qui envoie que les Cms dans la liste de seances"""
		return [seance for seance in self._listeSeance if seance.typeCreneau == CP.CM]
	#listeCm
	
	
	@property
	def listeTd(self):
		"""La fonction qui envoie que les Tds dans la liste de seances"""
		return [seance for seance in self._listeSeance if seance.typeCreneau == CP.TD]
	#listeTd
	
	
	@property
	def listeTp(self):
		"""La fonction qui envoie que les Tps dans la liste de seances"""
		return [seance for seance in self._listeSeance if seance.typeCreneau == CP.TP]
	#listeTp
	
	
	@property
	def listeExamen(self):
		"""La fonction qui envoie que les Examens dans la liste de seances"""
		return [seance for seance in self._listeSeance if seance.typeCreneau == CP.EXAMEN]
	#listeExamen
	
	
	@property
	def listeAutre(self):
		"""La fonction qui envoie que les Autres dans la liste de seances"""
		return [seance for seance in self._listeSeance if seance.typeCreneau == CP.AUTRE]
	#listeAutre
	
	
	def ajouterSeance(self, nouvelleSeance):
		"""
		La méthode qui ajoute une nouvelle seance en fonction de son type dans la liste 
		@param self: L'argument implicite
		@param nouvelleSeance: la nouvelle Seance à ajouter
		@type nouvelleSeance: une seance
		"""
		print("creation !")
		self._listeSeance.append(nouvelleSeance)
		if nouvelleSeance.typeCreneau == CP.CM:
			self._nombreCm += 1
		elif nouvelleSeance.typeCreneau == CP.TD:
			self._nombreTd += 1
		elif nouvelleSeance.typeCreneau == CP.TP:
			self._nombreTp += 1
		elif nouvelleSeance.typeCreneau == CP.EXAMEN:
			self._nombreExamen += 1
		elif nouvelleSeance.typeCreneau == CP.AUTRE:
			self._nombreAutre += 1
		#if
	#ajouterSeance
	
	
	def supprimerSeance(self, uneSeance):
		"""
		La méthode qui supprime une seance en fonction de son type dans la liste 
		@param self: L'argument implicite
		@param uneSeance: la  Seance à supprimer
		@type uneSeance: une seance
		"""
		if uneSeance in self._listeSeance:
			self._listeSeance.remove(uneSeance)
			if nouvelleSeance.typeCreneau == CP.CM:
				self._nombreCm -= 1
			elif nouvelleSeance.typeCreneau == CP.TD:
				self._nombreTd -= 1
			elif nouvelleSeance.typeCreneau == CP.TP:
				self._nombreTp -= 1
			elif nouvelleSeance.typeCreneau == CP.EXAMEN:
				self._nombreExamen -= 1
			elif nouvelleSeance.typeCreneau == CP.AUTRE:
				self._nombreAutre -= 1
			#if
		#if
	#supprimerSeance
	
#Ue
