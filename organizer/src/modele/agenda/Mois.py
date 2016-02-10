#!/usr/bin/python
# -*-coding:utf-8 -*

import Jour, Semaine, Modifier
from Semaine import *
from FabriqueCreneau import CreneauxPossible as CP


###############################################################################
# Liste des valeurs légales pour un nom de mois.
# On peut les utiliser dans nos code pour simplifier les traitements
JANVIER = "janvier"
FEVRIER = "fevrier"
MARS = "mars"
AVRIL = "avril"
MAI = "mai"
JUIN = "juin"
JUILLET = "juillet"
AOUT = "aout"
SEPTEMBRE = "septembre"
OCTOBRE = "octobre"
NOVEMBRE = "novembre"
DECEMBRE = "decembre"

MOIS_LEGAUX = [JANVIER, FEVRIER, MARS, AVRIL, MAI, JUIN, JUILLET, AOUT, SEPTEMBRE, OCTOBRE, NOVEMBRE, DECEMBRE]
###############################################################################


class Mois(Modifier.Modifier):
	"""
	La classe qui représente un mois dans une année.
	Cela va servir à stocker les L{Semaine}, dans l'ordre d'arrivée.
	@ivar _nom : Le nom du mois parmi ceux présents plus hauts.
	@ivar _semaines : la liste des semaines de ce mois.
	@ivar _nbJours : le nombre de jours dans ce mois.
	@ivar _jourApres : Le 1er jour du mois suivant.
	@author : Laurent Bardoux p1108365
	@version : 1.0
	"""
	
	def __init__(self, nom, jourDebut, nbJours):
		"""
		Le constructeur de cette classe.
		Il permet de générer les semaines en se basant sur jourDebut et nbJours.
		@param self : L'argument implicite.
		@type nom : str.
		@param nom : le nom de ce mois, parmi ceux se trouvant en haut.
		@type jourDebut : str.
		@param jourDebut : le nom du jour par lequel commence la premiere semaine de ce mois.
		@type nbJours : int.
		@param nbJours : le nombre de jours que contient ce mois :(30, 31, 28, 29).
		"""
		super(Mois, self).__init__()
		self._nom = nom
		self._nbJours = nbJours
		self._semaines = list()
		self._jourApres = self._genererSemaines(jourDebut)
	#__init__
	
	
	def _genererSemaines(self, jourDebut):
		"""
		Permet de générer les semaines de ce mois en se basant sur jourDebut.
		@param self : L'argument implicite.
		@type jourDebut : str.
		@param jourDebut : le nom du jour par lequel commence la premiere semaine de ce mois.
		@rtype : str.
		@return : le jour suivant de la fin du mois
		"""
		joursRestants = self._nbJours
		compteurSemaine = 1
		numDebutSemaine = 1
		numFinSemaine = 1
		_liste = Jour.JOURS_LEGAUX
		tailleListe = len(_liste)
		i = _liste.index(jourDebut)
		apres = _liste[0]
		
		while joursRestants > 0:
			if (tailleListe - i) < joursRestants:
				numFinSemaine = numDebutSemaine + tailleListe - i - 1
				#print("du " + _liste[i] + " " + str(numDebutSemaine) + " au " + _liste[tailleListe-1] + " " + str(numFinSemaine))
				temp = Semaine(compteurSemaine, construireArgument(_liste[i], numDebutSemaine, _liste[tailleListe-1], numFinSemaine))
				joursRestants -= tailleListe-i
				i = 0
				numDebutSemaine = numFinSemaine + 1
				compteurSemaine += 1
				self._semaines.append(temp)
				apres = _liste[0]
			else:
				#print("du " + _liste[i] + " " + str(numDebutSemaine) + " au " + _liste[joursRestants-1] + " " + str(numFinSemaine + joursRestants))
				temp = Semaine(compteurSemaine, construireArgument(_liste[i], numDebutSemaine, _liste[joursRestants-1], numFinSemaine + joursRestants))
				self._semaines.append(temp)
				apres = _liste[joursRestants%tailleListe]
				joursRestants = 0
			#if
		#while
		return apres
	#_genererSemaines
	
	
	@property
	def nbJours(self):
		"""
		L'accesseur pour le nombre de jour de ce mois.
		@param self : l'argument implicite.
		@rtype : int.
		@return : le nombre de jour du mois.
		"""
		return self._nbJours
	#nbJours
	
	
	@property
	def semaines(self):
		"""L'accesseur pour les semaines que contient ce mois"""
		return self._semaines
	#semaines
	
	
	@property
	def nom(self):
		"""
		L'accesseur pour le nom de ce mois.
		@param self : l'argument implicite.
		@rtype : str.
		@return : le nom du mois.
		"""
		return self._nom
	#nom
	
	
	@property
	def jourApres(self):
		"""
		L'accesseur pour le jour après la fin du mois.
		@param self : l'argument implicite.
		@rtype : str.
		@return : le nom du jour suivant la fin du mois.
		"""
		return self._jourApres
	#nom
	
	
	@property
	def numero(self):
		"""Renvoie le numéro du mois"""
		for i,elt in enumerate(MOIS_LEGAUX):
			if elt == self._nom:
				return i+1
			#if
		#for
		return 0
	#numero
	
	
	def recupererSemaineParNumJour(self, numJour):
		"""
		Permet la récupération d'une semaine complète par un numéro de jour.
		Ainsi, demander le 25 renverra la L{Semaine} contenant le 25.
		@param self : l'argument implicite
		@type numJour : int
		@param numJour : le numéro du jour dont on cherche la semaine.
		@rtype : L{Semaine}
		@return : la Semaine concernée ou None si elle n'existe pas.
		"""
		for sem in self._semaines:
			for jour in sem.jours.values():
				if jour.numero == numJour:
					return sem
				#if
			#for
		#for
		return None
	#recupererSemaineParNumJour
	
	
	def ajouterCreneau(self, jour, debut, fin, typeCreneau=CP.CRENEAU):
		"""
		Etape 3 de la descente dans l'architecture.
		Ceci va "ajouter" un L{Creneau} dans le M{jour}, entre
		M{debut} et M{fin}.
		@param self : L'argument implicite
		@type jour : int
		@param jour : le numéro du jour dans lequel insérer ce créneau.
		@type debut : int [1, 48]
		@param debut : l'heure de début du créneau
		@type fin : int [1, 48]
		@param fin : l'heure de fin du créneau
		@type typeCreneau : enum
		@param typeCreneau : une valeur enumérée pour la fabrique de creneau
		@precondition : debut < fin, jour/debut/fin doivent etre compris dans leurs intervalles respectifs
		@raise ArgumentInvalide : SI jamais un des arguments ne permet pas la création d'un Creneau.
		@rtype : Creneau
		@return : un Creneau 
		"""
		semaine = self.recupererSemaineParNumJour(jour)
		if semaine is not None:
			resultat = None
			try:
				resultat = semaine.ajouterCreneau(jour, debut, fin, typeCreneau)
			except ValueError:
				raise
			else:
				self.ajoutDeCreneau()
				return resultat
			#try
		else:
			raise ValueError("Ce jour " + str(jour) + " n'existe pas dans ce mois !")
		#if
	#ajouterCreneau
	
	
	def supprimerCreneau(self, jour, idCreneau):
		"""
		Lance la suppression d'un L{Creneau} si il existe.
		@param self : L'argument implicite
		@type jour : int
		@param jour : le numéro du jour où le créneau se situe.
		@type idCreneau : ...
		@param idCreneau : l'identifiant unique du créneau que l'on veut supprimer.
		@raise CreneauInexistant : En cas d'erreur sur les arguments.
		"""
		semaineCible = self.recupererSemaineParNumJour(jour)
		if semaineCible is None:
			raise ValueError("Le jour numéro " + jour + " n'est pas dans ce mois !")
		#if
		try:
			semaineCible.supprimerCreneau(jour, idCreneau)
		except ValueError:
			raise
		else:
			self.retraitDeCreneau()
		#try
	#supprimerCreneau
	
#Mois
