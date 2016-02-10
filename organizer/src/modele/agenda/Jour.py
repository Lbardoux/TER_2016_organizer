#!/usr/bin/python
# -*-coding:utf-8 -*

import Horaire, FabriqueCreneau
from FabriqueCreneau import CreneauxPossible as CP

###############################################################################
# Liste des valeurs légales pour un nom de jour.
# On peut les utiliser dans nos code pour simplifier les traitements
LUNDI = "lundi"
MARDI = "mardi"
MERCREDI = "mercredi"
JEUDI = "jeudi"
VENDREDI = "vendredi"
SAMEDI = "samedi"
DIMANCHE = "dimanche"

JOURS_LEGAUX = [LUNDI, MARDI, MERCREDI, JEUDI, VENDREDI, SAMEDI, DIMANCHE]
###############################################################################


class Jour(object):
	"""
	La classe qui représente un jour dans un agenda.
	Cette classe va donc contenir des L{Creneau}, afin que l'on puisse trouver
	chaque créneau en fonction d'un jour en particulier.
	@ivar _numero: Le numéro du jour dans le mois.
	@ivar _nom: le nom du jour parmi ceux connus.
	@ivar _creneaux: la liste de L{Creneau} que contient cette journée.
	@cvar _usine: La fabrique communes aux Jour
	Bien entendu, ces numéros ne sont pas fixés à l'avance, ils vont varier lors
	de la création de chaque journée, selon le calendrier européen.
	@author: Laurent Bardoux p1108365
	@version: 1.0
	"""

	_usine = FabriqueCreneau.FabriqueCreneau()
	
	def __init__(self, numero, nom=LUNDI):
		"""
		Permet de créer un jour en précisant les données temporelles.
		@param self: L'argument implicite.
		@type numero: int [1, 31].
		@param numero: le numéro du jour dans le mois.
		@type nom: str.
		@param nom: le nom du jour (de Lundi à Dimanche), optionnel (lundi par défaut).
		"""
		self._numero = numero
		self._creneaux = list()
		
		if nom in JOURS_LEGAUX:
			self._nom = nom
		else:
			self._nom = LUNDI
		#if
	#__init__
	
	
	@property
	def numero(self):
		"""
		L'accesseur pour le numéro du jour.
		"""
		return self._numero
	#numero
	
	
	@numero.setter
	def numero(self, nouveauNumero):
		"""
		Le mutateur pour changer le numéro.
		Attention, aucune vérification n'est faîtes à ce niveau là !
		@precondition: M{0 < nouveauNumero <= 31}
		"""
		if nouveauNumero>0 and nouveauNumero<=31:
			self._numero = nouveauNumero
		#if
	#numero
	
	
	@property
	def nom(self):
		"""
		L'accesseur pour le nom du jour dans la semaine.
		"""
		return self._nom
	#nom
	
	
	@property
	def creneaux(self):
		"""
		L'accesseur pour la liste triée des L{Creneau}.
		"""
		return self._creneaux
	#creneaux
	
	
	def insererCreneau(self, creneau):
		"""
		Cette fonction permet d'ajouter proprement un L{Creneau} dans la liste.
		Les insertions se font à l'aide tu tri par insertion afin que l'on puisse lire séquentiellement
		les L{Creneau} dans le but d'une conversion au format texte par exemple.
		Attention !
		Les créneaux doivent supporter l'opération < (def __lt__(self, autre))
		@param self: L'argument implicite.
		@type creneau: L{Creneau}.
		@param creneau: le créneau que l'on souhaite ajouter.
		A noter qu'il est tout à fait possible d'ajouter des créneaux aux même horaires (par exemple,
		dans le cas de plusieurs groupes pour un même cours).
		@postcondition: la liste interne est triée après l'insertion.
		"""
		for i, element in enumerate(self._creneaux):
			if creneau <= element:
				self._creneaux.insert(i, creneau)
				return
			#if
		#for
		
		# Cas ou creneau est le plus grand de tous, donc on le met à la fin
		self._creneaux.append(creneau)
	#ajouterCreneau
	
	
	def ajouterCreneau(self, debut, fin, typeCreneau=CP.CRENEAU):
		"""
		Etape finale de la descente dans l'architecture.
		Ceci va "ajouter" un L{Creneau} entre
		M{debut} et M{fin}.
		@param self: L'argument implicite
		@type debut: int [1, 48]
		@param debut: l'heure de début du créneau
		@type fin: int [1, 48]
		@param fin: l'heure de fin du créneau
		@type typeCreneau: enum
		@param typeCreneau: une valeur enumérée pour la fabrique de creneau
		@precondition: debut < fin, debut/fin doivent etre compris dans leurs intervalles respectifs
		@raise ValueError: Si un des arguments est mauvais.
		@rtype: L{Creneau}
		@return: un Creneau fraichement créé.
		"""
		horaire = None
		try:
			horaire = Horaire.Horaire(debut, fin)
		except AssertionError:
			raise ValueError("les horaires du creneaux sont invalides !")
		#try

		# L'identifiant sera attribué par les autorités habilités (Annee)
		nouveauCreneau = self._usine.fabrique(typeCreneau, 1, horaire)
		if nouveauCreneau is None:
			raise ValueError("Le créneau demandé " + str(typeCreneau) + " n'existe pas !")
		#if
		self.insererCreneau(nouveauCreneau)
		return nouveauCreneau
	#ajouterCreneau
	
	
	def supprimerCreneau(self, idCreneau):
		"""
		Lance la suppression d'un L{Creneau} si il existe.
		@param self: L'argument implicite
		@type idCreneau: Ce que l'on veut
		@param idCreneau: l'identifiant unique du créneau que l'on veut supprimer.
		@raise CreneauInexistant: En cas d'erreur sur les arguments.
		"""
		#stocker ailleurs ce creneau ? (ctrl-z, ctr-y)
		cible = None
		for creneau in self._creneaux:
			if creneau.identifiant == idCreneau:
				cible = creneau
				break
			#if
		#for
		if cible is None:
			raise ValueError(" Pas de créneau portant cet identifiant " + str(idCreneau))
		#if
		self._creneaux.remove(cible)
	#supprimerCreneau
	
#Jour
