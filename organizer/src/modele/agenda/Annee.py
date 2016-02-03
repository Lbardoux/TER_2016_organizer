#!/usr/bin/python
# -*-coding:utf-8 -*

import calendar
from datetime import datetime
from Jour import JOURS_LEGAUX
import Mois

class Annee(object):
	"""
	La classe la plus haute dans la hiérarchie de stockage d'un agenda.
	Elle représente une année, du 1er janvier au 31 decembre.
	De ce fait, elle gère les années spécifiques, et l'arborescence
	des L{Mois}, L{Semaines} et L{Jour}.
	C'est également le point d'entrée de la structure de stockage.
	@ivar _mois : un dictionnaire des L{Mois} disponibles.
	@ivar _an : l'année courante (2006 par exemple).
	@ivar _nbCreneaux : Un indicateur pour savoir si des créneaux existent
		dans cette année.
	@author : Laurent Bardoux p1108365
	@version : 1.0
	"""

	def __init__(self, an):
		"""
		Le constructeur principal de la classe.
		En se basant sur M{an}, il va initialiser la totalité d'une année,
		Ce paramètre servira de détecteur pour le premier jour (1er janvier).
		@param self : l'argument implicite.
		@type an : int
		@param an : Le numéro de l'année voulue.
		"""
		self._mois = dict()
		self._an = an
		self._nbCreneaux = 0
		
		# nombre de jours pour chaque mois :
		nbMaxJour = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		if calendar.isleap(an):
			nbMaxJour[1] = 29
		#if
		jour1 = self._premierJourAnnee(an)
		for i, nb in enumerate(Mois.MOIS_LEGAUX):
			temp = Mois.Mois(nb, jour1, nbMaxJour[i])
			self._mois[nb] = temp
			#tmp = jour1 #affichage
			jour1 = temp.jourApres
			#print("On crée " + nb + " avec " + str(nbMaxJour[i]) + " jours allant de " + tmp + " à " + jour1)
		#for
	#__init__
	
	
	def _premierJourAnnee(self, an):
		"""
		Fonction privée qui renvoie le nom du jour du 1er janvier de M{an}.
		@param self : L'argument implicite.
		@type an : int
		@param an : l'année dont on veut le nom du premier jour.
		@rtype : str
		@return : le nom du premier jour
		"""
		return JOURS_LEGAUX[datetime(an, 1, 1).weekday()]
	#_premierJourAnnee
	
	
	@property
	def an(self):
		"""
		L'accesseur pour l'année de cette...Année !
		@param self : L'argument implicite.
		@rtype : int
		@return : l'année en cours au format numérique.
		"""
		return self._an
	#an
	
	
	@property
	def nbCreneaux(self):
		"""
		L'accesseur pour le nombre de creneaux présents
		Si il n'y en a pas, pas la peine de dumper cette année dans un
		fichier.
		@param self : L'argument implicite.
		@rtype : int
		@return : le nombre de creneaux disponible dans cette annee.
		"""
		return self._nbCreneaux
	#an
	
	
	


#Annee
