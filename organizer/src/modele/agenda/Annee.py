#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys, os
import calendar, datetime
import Mois, Modifier, GenerateurId
from Jour import JOURS_LEGAUX
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../../outils/")
from FabriqueCreneau import CreneauxPossible as CP


class Annee(Modifier.Modifier):
	"""
	La classe la plus haute dans la hiérarchie de stockage d'un agenda.
	Elle représente une année, du 1er janvier au 31 decembre.
	De ce fait, elle gère les années spécifiques, et l'arborescence
	des L{Mois}, L{Semaine} et L{Jour}.
	C'est également le point d'entrée de la structure de stockage.
	@ivar _mois: un dictionnaire des L{Mois} disponibles.
	@ivar _an: l'année courante (2006 par exemple).
	@ivar _generateur: le générateur des identifiants spécifiques à cette année.
	@author: Laurent Bardoux p1108365
	@version: 1.0
	"""

	def __init__(self, an):
		"""
		Le constructeur principal de la classe.
		En se basant sur M{an}, il va initialiser la totalité d'une année,
		Ce paramètre servira de détecteur pour le premier jour (1er janvier).
		@param self: l'argument implicite.
		@type an: int
		@param an: Le numéro de l'année voulue.
		"""
		super(Annee, self).__init__()
		self._mois = dict()
		self._an = an
		self._generateur = GenerateurId.GenerateurId(1, lambda x : x+1)
		
		# nombre de jours pour chaque mois :
		nbMaxJour = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		if calendar.isleap(an):
			nbMaxJour[1] = 29
		#if
		jour1 = self._premierJourAnnee(an)
		for i, nb in enumerate(Mois.MOIS_LEGAUX):
			temp = Mois.Mois(nb, jour1, nbMaxJour[i])
			self._mois[nb] = temp
			jour1 = temp.jourApres
		#for
	#__init__
	
	
	def _premierJourAnnee(self, an):
		"""
		Fonction privée qui renvoie le nom du jour du 1er janvier de M{an}.
		@param self: L'argument implicite.
		@type an: int
		@param an: l'année dont on veut le nom du premier jour.
		@rtype: str
		@return: le nom du premier jour
		"""
		return JOURS_LEGAUX[datetime.datetime(an, 1, 1).weekday()]
	#_premierJourAnnee
	
	
	@property
	def an(self):
		"""L'accesseur pour l'année de cette...Année !"""
		return self._an
	#an
	
	
	@property
	def mois(self):
		"""Un accesseur pour les mois (dict)"""
		return self._mois
	#mois
	
	
	def _verifieNumeroMois(self, mois):
		"""
		Effectue la vérification et la levée d'exception sur le numéro de mois.
		@param self: L'argument implicite.
		@type mois: int
		@param mois: le numéro de mois à tester.
		@raise ValueError: Si le numéro de mois est erroné
		"""
		if mois < 1 or mois > 12:
			raise ValueError("Le numéro de mois " + str(mois) + " est invalide !")
		#if
	#_verifieNumeroMois
	
	
	def recupererSemaineParNumJour(self, mois, jour):
		"""
		Cette méthode est la suite de la chaine de récupération d'une semaine.
		Elle s'inscrit dans la successions d'appels pour récupérer une semaine, en
		descendant dans l'arborescence au fur et à mesure.
		@param self: L'argument implicite.
		@type mois: int [1,12]
		@param mois: le numéro du mois souhaité.
		@type jour: int
		@param jour: le numéro  du jour voulu.
		@raise ValueError: si le numéro de mois est incorrect.
		@rtype: L{Semaine}.
		@return: la semaine demandé si elle existe.
		"""
		self._verifieNumeroMois(mois)
		nomMois = Mois.MOIS_LEGAUX[mois-1]
		return self._mois[nomMois].recupererSemaineParNumJour(jour)
	#recupererSemaineParNumJour
	
	
	def ajouterCreneau(self, mois, jour, debut, fin, typeCreneau=CP.CRENEAU):
		"""
		Etape 2 de la descente dans l'architecture.
		Ceci va "ajouter" un L{Creneau} dans le M{mois}, M{jour}, entre
		M{debut} et M{fin}.
		@param self: L'argument implicite
		@type mois: int
		@param mois: le numéro du mois dans lequel insérer ce créneau.
		@type jour: int
		@param jour: le numéro du jour dans lequel insérer ce créneau.
		@type debut: int [1, 48]
		@param debut: l'heure de début du créneau
		@type fin: int [1, 48]
		@param fin: l'heure de fin du créneau
		@type typeCreneau: enum
		@param typeCreneau: une valeur enumérée pour la fabrique de creneau
		@precondition: debut < fin, mois/jour/debut/fin doivent etre compris dans leurs intervalles respectifs
		@raise ValueError: Si un problème avec les arguments a eu lieu.
		@rtype: L{Creneau}
		@return: un Creneau manipulable.
		"""
		self._verifieNumeroMois(mois)
		nomMois = Mois.MOIS_LEGAUX[mois-1]
		resultat = None
		try:
			resultat = self._mois[nomMois].ajouterCreneau(jour, debut, fin, typeCreneau)
		except ValueError:
			raise
		else:
			self.ajoutDeCreneau()
			resultat.identifiant = self._generateur.suivant()
		#try
		return resultat
	#ajouterCreneau
	
	
	def supprimerCreneau(self, mois, jour, creneau):
		"""
		Lance la suppression d'un L{Creneau} si il existe.
		@param self: L'argument implicite
		@type mois: int
		@param mois: le mois dont on veut supprimer le créneau.
		@type jour: int
		@param jour: le numéro du jour où le créneau se situe.
		@type creneau: L{Creneau}
		@param creneau : le créneau que l'on veut supprimer.
		@raise ValueError: En cas d'erreur sur les arguments.
		"""
		self._verifieNumeroMois(mois)
		nomMois = Mois.MOIS_LEGAUX[mois-1]
		moisCible = self._mois[nomMois]
		try:
			moisCible.supprimerCreneau(jour, creneau)
		except ValueError:
			raise
		else:
			self.retraitDeCreneau()
		#try
	#supprimerCreneau
	
	
	def insererCreneau(self, creneau, mois, jour):
		"""
		Cette fonction permet d'insérer un creneau dans l'Année courant.
		@param self: L'argument implicite
		@type creneau: L{Creneau}
		@param creneau: Le créneaux (ou une classe dérivée) que l'on veut insérer.
		@type mois: int
		@param mois: le numéro du mois dans lequel insérer ce créneau.
		@type jour: int
		@param jour: le numéro du jour dans lequel insérer ce créneau.
		@raise ValueError: Si les données sont erronées.
		"""
		self._verifieNumeroMois(mois)
		nomMois = Mois.MOIS_LEGAUX[mois-1]
		moisCible = self._mois[nomMois]
		try:
			moisCible.insererCreneau(creneau, jour)
		except ValueError:
			raise
		else:
			self.ajoutDeCreneau()
		#try
	#insererCreneau
	
#Annee
