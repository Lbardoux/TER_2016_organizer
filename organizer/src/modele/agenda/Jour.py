#!/usr/bin/python
# -*-coding:utf-8 -*



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
	@ivar _numero : Le numéro du jour dans le mois.
	@ivar _nom : le nom du jour parmi ceux connus.
	@ivar _creneaux : la liste de L{Creneau} que contient cette journée.
	Bien entendu, ces numéros ne sont pas fixés à l'avance, ils vont varier lors
	de la création de chaque journée, selon le calendrier européen.
	@author : Laurent Bardoux p1108365
	@version : 1.0
	"""
	
	def __init__(self, numero, nom=LUNDI):
		"""
		Permet de créer un jour en précisant les données temporelles.
		@param self : L'argument implicite.
		@type numero : int [1, 31].
		@param numero : le numéro du jour dans le mois.
		@type nom : str.
		@param nom : le nom du jour (de Lundi à Dimanche), optionnel (lundi par défaut).
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
		@param self : L'argument implicite.
		@rtype : int
		@return : Le numéro du jour.
		"""
		return self._numero
	#numero
	
	
	@numero.setter
	def numero(self, nouveauNumero):
		"""
		Le mutateur pour changer le numéro.
		Attention, aucune vérification n'est faîtes à ce niveau là !
		@param self : L'argument implicite.
		@type nouveauNumero : int
		@param nouveauNumero : la nouvelle valeur pour le numéro du jour.
		@precondition : M{0 < nouveauNumero <= 31}
		"""
		if nouveauNumero>0 and nouveauNumero<=31:
			self._numero = nouveauNumero
		#if
	#numero
	
	
	@property
	def nom(self):
		"""
		L'accesseur pour le nom du jour dans la semaine.
		@param self : L'argument implicite.
		@rtype : str.
		@return : le nom du jour.
		"""
		return self._nom
	#nom
	
	
	@nom.setter
	def nom(self, nouveauNom):
		"""
		Le mutateur pour changer le nom de ce jour.
		@param self : L'argument implicite.
		@type nouveauNom : str.
		@param nouveauNom : le nom souhaité pour ce jour.
		"""
		self._nom = nouveauNom
	#nom
	
	
	@property
	def creneaux(self):
		"""
		L'accesseur pour la liste triée des L{Creneau}.
		@param self : L'argument implicite.
		@rtype : list.
		@return : la liste des L{Creneau}.
		"""
		return self._creneaux
	#creneaux
	
	
	def ajouterCreneau(self, creneau):
		"""
		Cette fonction permet d'ajouter proprement un L{Creneau} dans la liste.
		Les insertions se font à l'aide tu tri par insertion afin que l'on puisse lire séquentiellement
		les L{Creneau} dans le but d'une conversion au format texte par exemple.
		@param self : L'argument implicite.
		@type creneau : L{Creneau}.
		@param creneau : le créneau que l'on souhaite ajouter.
		A noter qu'il est tout à fait possible d'ajouter des créneaux aux même horaires (par exemple,
		dans le cas de plusieurs groupes pour un même cours).
		@postcondition : la liste interne est triée après l'insertion.
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
	
	
	def retirerCreneaux(self, *arguments):
		"""
		TODO
		"""
	#retirerCreneaux
	
	
	
#Jour