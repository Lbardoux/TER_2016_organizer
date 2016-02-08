#!/usr/bin/python
# -*-coding:utf-8 -*

import sys
import ConstantesQuarts

class Horaire(object):
	"""
	La classe qui définit un horaire pour un Créneau.
	Notre calendrier est découpé en semaine (allant de Lundi à Vendredi).
	Ces jours sont découpées en quart d'heures de 8h du matin à 20h.
	Donc, pour modéliser une semaine, nous nous basons sur le nombre de
	quart d'heures disponibles, soit :
	M{12_heures * 4 = 240 quart d'heures}
	Il ne nous reste qu'a faire la division euclidienne du numéro par 240
	pour connaitre la semaine associée.

	@ivar _debut : le numéro de quart d'heure du début de cet horaire
	@ivar _fin : le numéro de quart d'heure de fin de cet horaire
	@cvar _valeurSemaine : la valeur maximale d'une semaine
	@cvar _valeurJour : la valeur maximale d'un jour
	@author : Laurent Bardoux p1108365
	@version : 1.0
	"""
	
	_valeurJour =ConstantesQuarts.TOTAL_PAR_JOUR
	_valeurSemaine = ConstantesQuarts.TOTAL_PAR_SEMAINE
	
	
	def __init__(self, debut, fin):
		"""
		Le constructeur de cette classe, qui initialise correctement un Horaire
		Levée d'une assertion si les precondition ne sont pas remplis!
		@param self : L'argument implicite
		@param debut : le numero de quart d'heure de début
		@type debut : un entier naturel non nul
		@param fin : le numero de quart d'heure de fin
		@type fin : un entier naturel non nul
		@raise AssertionError : si les paramètres sont mauvais 
		"""
		self._assertArguments(debut, fin)
		self._debut = debut
		self._fin = fin
	#fin __init__
	
	
	@property
	def debut(self):
		"""
		L'accesseur pour avoir le quart d'heure de début
		@param self : l'argument implicite
		@return : un entier représentant ce quart d'heure
		"""
		return self._debut
	#fin debut
	
	
	@debut.setter
	def debut(self, valeur):
		"""
		Le mutateur pour le quart d'heure de début.
		@param self : l'argument implicite
		@param valeur : le nouveau quart d'heure voulu
		@type valeur : entier naturel non nul
		@raise AssertionError : si les paramètres sont mauvais 
		"""
		if valeur > 0:
			self._assertArguments(valeur, self._fin)
			self._debut = valeur
		#if
	#fin debut
	
	
	@property
	def fin(self):
		"""
		L'accesseur pour avoir le quart d'heure de fin
		@param self : l'argument implicite
		@return : un entier représentant ce quart d'heure
		"""
		return self._fin
	#fin fin
	
	
	@fin.setter
	def fin(self, valeur):
		"""
		Le mutateur pour le quart d'heure de fin.
		@param self : l'argument implicite
		@param valeur : le nouveau quart d'heure voulu
		@type valeur : entier naturel non nul
		@raise AssertionError : si les paramètres sont mauvais 
		"""
		if valeur > 0:
			self._assertArguments(self._debut, valeur)
			self._fin = valeur
		#if
	#fin fin
	
	
	def _assertArguments(self, debut, fin):
		"""
		Cette fonction lève une exception si ses arguments ne sont pas bon.
		@param self : l'argument implicite.
		@param debut : le numero de quart d'heure de début
		@type debut : un entier naturel non nul
		@param fin : le numero de quart d'heure de fin
		@type fin : un entier naturel non nul
		"""
		assert type(debut) is int, "debut doit etre un entier"
		assert type(fin) is int, "fin doit etre un entier"
		assert debut >= 1 and debut <= 49, "debut doit etre supérieur à 1"
		assert fin > debut, "fin doit etre supérieur a debut"
		assert fin <= 49, "fin doit etre inférieur ou égal à 48"
	#fin _assertArguments
	
	
	def _getGenerique(self, valeur, total):
		"""
		Factorisation de getSemaineDe et getJourDe.
		@param self : l'argument implicite.
		@param valeur : valeur dont on veut la semaine
		@type valeur : entier naturel non nul
		@param total : le maximum atteignable pour la division
		@type total : entier naturel non nul
		@return : un entier naturel non nul M{[1, +oo[}
		"""
		if valeur%total == 0:
			return (valeur // total)
		return (valeur // total) + 1
	#fin _getGenerique
	
	
	def getSemaineDe(self, valeur):
		"""
		Permet de calculer la semaine à laquelle est lié valeur.
		@param self : l'argument implicite.
		@param valeur : valeur dont on veut la semaine
		@type valeur : entier naturel non nul
		@return : un entier naturel non nul M{[1, +oo[}
		"""
		return self._getGenerique(valeur, self._valeurSemaine)
	#fin getSemaine
	
	
	def getJourDe(self, valeur):
		"""
		Renvoi le jour auquel est associé valeur
		@param self : l'argument implicite
		@param valeur : valeur dont on veut le jour
		@type valeur : entier naturel non nul.
		@return : un entier représentant le jour
		"""
		return self._getGenerique(valeur, self._valeurJour)
	#fin getJour
	
	def changeHoraire(self, nouveauDebut, nouvelFin):
		"""
		Permet de changer le debut et la fin d'un Horaire en
		effectuant des vérifications (comme la fin après le début, etc).
		
		Lève une assertion en cas de mauvais emploi !
		
		@param self : L'argument implicite
		@param nouveauDebut : le nouvel Horaire de début
		@type nouveauDebut : entier naturel non nul
		@param nouvelFin : le nouvel Horaire de fin
		@type nouvelFin : entier naturel non nul
		@precondition : M{0 < nouveauDebut < nouvelFin}
		@raise AssertionError : si les paramètres sont mauvais
		"""
		self._assertArguments(nouveauDebut, nouvelFin)
		self._debut = nouveauDebut
		self._fin = nouvelFin
	#fin changeHoraire
	
#fin Horaire
