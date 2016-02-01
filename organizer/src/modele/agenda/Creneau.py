#!/usr/bin/python
# -*-coding:utf-8 -*

import Horaire

class Creneau(object):
	"""
	La classe centrale d'un agenda.
	Le créneau est un emplacement que l'on alloue sur l'agenda.
	Il contient donc parfois de l'information supplémentaire.
	@ivar _identifiant : l'identifiant unique d'un créneau, sous la forme d'un entier naturel non nul.
	@ivar _horaire : Une référence sur un Horaire.
	@ivar _informations : un dictionnaire contenant des informations additionnelles sous la forme str -> valeur
	@author : Laurent Bardoux p1108365
	@version : 1.0
	"""
	
	def __init__(self, identifiant, horaire):
		"""
		Le constructeur de cette classe.
		@precondition : identifiant doit etre unique dans toute l'application !
		@precondition : M{horaire is not None}
		@param self : l'argument implicite
		@param identifiant : l'id unique associé à ce créneau.
		@type identifiant : entier naturel non nul.
		@param horaire : une instance de Horaire, qui définira le placement sur l'agenda
		@type horaire : Horaire
		@raise AssertionError : Si les arguments ne correspondent pas
		"""
		assert type(horaire) is Horaire, "On ne peut ranger qu'un Horaire ici"
		assert type(identifiant) is int and identifiant > 0, "Il faut un entier > 0 comme id"
		self._identifiant = identifiant
		self._horaire = horaire
		self._informations = dict()
	#fin __init__
	
	
	@property
	def identifiant(self):
		"""
		Un accesseur pour l'identifiant unique.
		@param self : L'argument implicite.
		@return : la valeur entière de l'identifiant
		"""
		return self._identifiant
	#fin identifiant
	
	
	@identifiant.setter
	def identifiant(self, autre):
		"""
		Ne fais rien, on ne doit pas modifier l'identifiant
		"""
	#fin identifiant
	
	
	@property
	def horaire(self):
		"""
		Un accesseur pour l'Horaire contenu dans le Creneau.
		@param self : L'argument implicite
		@return : la référence sur l'Horaire
		"""
		return self._horaire
	#fin horaire
	
	
	@horaire.setter
	def horaire(self, nouvelHoraire):
		"""
		Un setter pour l'Horaire.
		@param self : L'argument implicite
		@param nouvelHoraire : Le nouvel ... Horaire !
		@type nouvelHoraire : Horaire
		@precondition : L{type(nouvelHoraire) is Horaire}
		"""
		if type(nouvelHoraire) is Horaire:
			self._horaire = nouvelHoraire
		#if
	#fin horaire
	
	
	@property
	def informations(self):
		"""
		Un accesseur pour les informations contenues dans ce Creneau.
		@param self : l'argument implicite.
		@return : une référence sur le dictionnaire qui contient ces informations.
		"""
		return self._informations
	#fin informations
	
	
	@identifiant.setter
	def informations(self, autre):
		"""
		Un mutateur pour pouvoir initialiser à la volée les informations.
		@param self : l'argument implicite.
		@param autre : Le dictionnaire que l'on veut mettre à la place.
		@type autre : dict
		"""
		if type(autre) is dict:
			self._informations = autre
		#if
	#fin informations
	
	
	def existe(self, clef):
		"""
		Test si la clef existe déjà dans le dictionnaire.
		@param self : l'argument implicite.
		@param clef : la clef a testé
		@type clef : str
		@return : True si la clef existe, False sinon
		"""
		if type(clef) is str:
			return clef in self._informations.keys()
		#if
	#fin existe
	
	
	def ajouterInformation(self, clef, info):
		"""
		Permet d'ajouter une information dans le dictionnaire, sous la forme clef -> info.
		Vous pouvez vérifier l'unicité d'une clef grâce à la méthode self.existe.
		Si la clef existe déjà, rien ne se passera (pas d'écrasement).
		
		@param self : l'argument implicite.
		@param clef : la clef pour identifier l'information dans le dictionnaire.
		@type clef : str, qui doit etre unique dans le dictionnaire.
		@param info : Ce que l'on veut stocker dans le dictionnaire.
		@type info : Ce que l'on veut
		@precondition : L{type(clef) is str}
		"""
		if not self.existe(clef):
			self._informations[clef] = info
		#if
	#fin ajouterInformation
	
#fin Creneau
