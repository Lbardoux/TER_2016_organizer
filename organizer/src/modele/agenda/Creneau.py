#!/usr/bin/python3
# -*-coding:utf-8 -*

from Horaire import transformeHoraire, traiteChiffre
from observateur.Observable import *

class Creneau(Observable):
	"""
	La classe centrale d'un agenda.
	Le créneau est un emplacement que l'on alloue sur l'agenda.
	Il contient donc parfois de l'information supplémentaire.
	@ivar _identifiant: l'identifiant unique d'un créneau, sous la forme d'un entier naturel non nul.
	@ivar _horaire: Une référence sur un Horaire.
	@ivar _informations: un dictionnaire contenant des informations additionnelles sous la forme str -> valeur
	@ivar _typeCreneau: Le type de créneau
	@ivar _dateExacte: La date au format chaine.
	@author: Laurent Bardoux p1108365
	@version: 1.0
	"""
	
	def __init__(self, identifiant, horaire):
		"""
		Le constructeur de cette classe.
		@precondition: identifiant doit etre unique dans une annee , M{horaire is not None}.
		@param self: l'argument implicite
		@param identifiant: l'id unique associé à ce créneau.
		@type identifiant: entier naturel non nul.
		@param horaire: une instance de Horaire, qui définira le placement sur l'agenda
		@type horaire: L{Horaire}
		Globalement, on peut mettre ce que l'on veut comme identifiant, comme un
		UID, ou un simple entier.
		"""
		super(Creneau, self).__init__()
		self._identifiant = identifiant
		self._horaire = horaire
		self._informations = dict()
		self._typeCreneau = 0
		self._dateExacte = ()
	#__init__
	
	
	@property
	def identifiant(self):
		"""Un accesseur pour l'identifiant unique."""
		return self._identifiant
	#identifiant
	
	
	@identifiant.setter
	def identifiant(self, valeur):
		"""Un mutateur pour l'identifiant unique."""
		self._identifiant = valeur
	#identifiant
	
	
	@property
	def horaire(self):
		"""Un accesseur pour l'L{Horaire} contenu dans le Creneau."""
		return self._horaire
	#horaire
	
	
	@property
	def typeCreneau(self):
		"""Un accesseur pour _typeCreneau"""
		return self._typeCreneau
	#typeCreneau
	
	
	@typeCreneau.setter
	def typeCreneau(self, valeur):
		"""Un mutateur pour le type de Creneau"""
		self._typeCreneau = valeur
	#typeCreneau
	
	
	@horaire.setter
	@notifier
	def horaire(self, nouvelHoraire):
		"""
		Un setter pour l'Horaire.
		@precondition: type(nouvelHoraire) is Horaire
		"""
		self._horaire = nouvelHoraire
	#horaire
	
	
	@property
	def informations(self):
		"""Un accesseur pour les informations contenues dans ce Creneau."""
		return self._informations
	#informations
	
	
	def existe(self, clef):
		"""
		Test si la clef existe déjà dans le dictionnaire.
		@param self: l'argument implicite.
		@param clef: la clef a testé
		@type clef: str
		@return: True si la clef existe, False sinon
		"""
		if type(clef) is str:
			return clef in self._informations.keys()
		#if
	#existe
	
	
	@notifier
	def ajouterInformation(self, clef, info):
		"""
		Permet d'ajouter une information dans le dictionnaire, sous la forme clef -> info.
		Vous pouvez vérifier l'unicité d'une clef grâce à la méthode self.existe.
		Si la clef existe déjà, rien ne se passera (pas d'écrasement).
		@param self: l'argument implicite.
		@type clef: str
		@param clef: la clef pour identifier l'information dans le dictionnaire.
		@type info: object
		@param info: Ce que l'on veut stocker dans le dictionnaire.
		@precondition: type(clef) is str
		"""
		if not self.existe(clef):
			self._informations[clef] = info
		#if
	#fin ajouterInformation
	
	
	@notifier
	def enleverInformation(self, clef):
		"""
		Permet de supprimer, si elle existe, l'information associée à M{clef}.
		@param self: L'argument implicite.
		@type clef: str
		@param clef: la clef dont on veut supprimer l'information.
		"""
		if self.existe(clef):
			del self._informations[clef]
		#if
	#enleverInformation
	
	
	@property
	def dateExacte(self):
		"""Renvoie la date exacte au format chaine"""
		return self._dateExacte
	#dateExacte
	
	
	@dateExacte.setter
	def dateExacte(self, valeur):
		"""Permet de modifier la date exacte de ce Creneau"""
		self._dateExacte = valeur
	#dateExacte
	
	
	def __le__(self, autre):
		"""
		Permet de comparer des Creneaux via <=.
		@param self: l'argument implicite.
		@type autre: Creneau
		@param autre: le second Creneau avec lequel comparer.
		@rtype: bool
		@return: True si self <= autre, False sinon.
		"""
		return self.horaire.debut <= autre.horaire.debut
	#__le__
	
	
	def versChaine(self):
		"""
		Retourne sous forme de chaine une description du Creneau.
		Elle doit etre surchargé par les classes dérivées.
		@param self: L'argument implicite
		@rtype: str
		@return: une chaine descriptive
		"""
		return "il y a un créneau reservé entre " + self._horaire.debutstr + " à " + self._horaire.finstr
	#versChaine
	
	
	def __eq__(self, autre):
		"""
		Il faut trouver un moyen de comparer des creneaux, et pour cela,
		la tache revient aux classes filles (hélas)
		@param self: L'argument implicite.
		@type autre: Creneau
		@param autre: Le second Creneau avec lequel comparer
		@rtype: bool
		@return: True si ils sont identiques, False sinon
		"""
		return self._typeCreneau == autre._typeCreneau
	#__eq__
	
#fin Creneau
