#!/usr/bin/python
# -*-coding:utf-8 -*

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../agenda")
from Creneau import Creneau

class Seance(Creneau):
	"""
	La classe mere pour tout element d'une formation.
	ELle contient donc toutes les informations communes aux différents
	composant d'une formation.
	Elle fait également le lien avec la modélisation d'un agenda, et
	définit en conséquence les éléments utilisables.
	@ivar _nom: Le nom de cette séance
	@ivar _enseignant: Le nom de l'enseignant de cette séance
	@ivar _salle: Le nom de la salle de cette séance
	@version: 3.0
	@author: Liu Zhuying
	"""
	
	def __init__(self, idSeance, horaire):
		"""
		Le constructeur de la classe "abstraite" Seance.
		@param self : L'argument implicite
		@param idSeance : l'identifiant de cette Seance
		@type idSeance : entier naturel non nul
		@type horaire : Horaire.
		@param horaire : L'horaire voulu
		"""
		super(Seance, self).__init__(idSeance, horaire)
		self._nom = ""
		self._enseignant = ""
		self._salle = ""
	#fin __init__
	
	@property
	def nom(self):
		"""
		Récuperation du nom de cette séance
		"""
		return self._nom
	#fin nom
	
	@property
	def enseignant(self):
		"""
		Récuperation de l'enseignant de cette séance
		"""
		return self._enseignant
	#fin enseignant
	
	@property
	def salle(self):
		"""
		Récuperation de la salle de cette séance
		"""
		return self._salle
	#fin salle
	
	@nom.setter
	def nom(self, nouveauNom):
		"""
		Le mutateur pour le nom
		@precondition: type(nouveauNom) est une chaine de caractères
		"""
		self._nom = nouveauNom
	#fin nom
	
	@enseignant.setter
	def enseignant(self, nouvelEnseignant):
		"""
		Le mutateur pour l'enseignant
		@precondition: type(nouvelEnseignant) est une chaine de caractères
		"""
		self._enseignant = nouvelEnseignant
	#fin enseignant
	
	@salle.setter
	def salle(self, nouvelleSalle):
		"""
		Le mutateur pour la salle
		@precondition: type(nouvelleSalle) est une chaine de caractères
		"""
		self._salle = nouvelleSalle
	#fin salle
	
#fin Seance
