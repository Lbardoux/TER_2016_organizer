#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys, ConstantesQuarts

def transformeHoraire(horaire):
	"""
	Opère la conversion d'un entier représentant un horaire
	vers des unités plus ... human friendly.
	conversion d'un entier entre 1 et 49 vers des heures
	allant de 7h00 à 19h00 de 15 minutes à chaque fois
	@type horaire: int
	@param horaire: l'entier que l'on veut convertir.
	@rtype: tuple
	@return: un tuple contenant (heures, minutes)
	"""
	temp = (horaire-1)*15
	heure = 7 + (temp//60)
	minute = (temp)%60
	return (heure, minute)
#transformeHoraire


def traiteChiffre(chiffre):
	"""
	Transforme un entier en chaine, et si celui-ci n'a que des unités,
	ajoute un 0 supplémentaire devant.
	@type chiffre: int
	@param chiffre: l'entier à retravailler.
	@rtype: str
	@return: une chaine formatée pour ce chiffre.
	"""
	if chiffre < 10:
		return "0" + str(chiffre)
	#if
	return str(chiffre)
#traiteChiffre


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
	
	@ivar _debut: le numéro de quart d'heure du début de cet horaire
	@ivar _fin: le numéro de quart d'heure de fin de cet horaire
	@cvar _valeurJour: la valeur maximale d'un jour
	@author: Laurent Bardoux p1108365
	@version: 1.0
	"""
	
	_valeurJour =ConstantesQuarts.TOTAL_PAR_JOUR
	
	
	def __init__(self, debut, fin):
		"""
		Le constructeur de cette classe, qui initialise correctement un Horaire
		Levée d'une assertion si les precondition ne sont pas remplis!
		@param self: L'argument implicite
		@param debut: le numero de quart d'heure de début
		@type debut: un entier naturel non nul
		@param fin: le numero de quart d'heure de fin
		@type fin: un entier naturel non nul
		@raise AssertionError: si les paramètres sont mauvais 
		"""
		self._assertArguments(debut, fin)
		self._debut = debut
		self._fin = fin
	#fin __init__
	
	
	@property
	def debut(self):
		"""L'accesseur pour avoir le quart d'heure de début"""
		return self._debut
	#debut
	
	
	@debut.setter
	def debut(self, valeur):
		"""
		Le mutateur pour le quart d'heure de début.
		@raise AssertionError: si les paramètres sont mauvais 
		"""
		if valeur > 0:
			self._assertArguments(valeur, self._fin)
			self._debut = valeur
		#if
	#debut
	
	
	@property
	def debutstr(self):
		"""Renvoie l'heure de debut au format chaine"""
		h, m = transformeHoraire(self._debut)
		return traiteChiffre(h) + "h" + traiteChiffre(m)
	#debutstr
	
	
	@property
	def finstr(self):
		"""Renvoie l'heure de fin au format chaine"""
		h, m = transformeHoraire(self._fin)
		return traiteChiffre(h) + "h" + traiteChiffre(m)
	#finstr
	
	
	@property
	def fin(self):
		"""L'accesseur pour avoir le quart d'heure de fin"""
		return self._fin
	#fin
	
	
	@fin.setter
	def fin(self, valeur):
		"""
		Le mutateur pour le quart d'heure de fin.
		@raise AssertionError: si les paramètres sont mauvais 
		"""
		if valeur > 0:
			self._assertArguments(self._debut, valeur)
			self._fin = valeur
		#if
	#fin
	
	
	def _assertArguments(self, debut, fin):
		"""
		Cette fonction lève une exception si ses arguments ne sont pas bon.
		@param self: l'argument implicite.
		@param debut: le numero de quart d'heure de début
		@type debut: un entier naturel non nul
		@param fin: le numero de quart d'heure de fin
		@type fin: un entier naturel non nul
		"""
		assert type(debut) is int, "debut doit etre un entier"
		assert type(fin) is int, "fin doit etre un entier"
		assert fin > debut, "fin doit etre supérieur a debut"
	#_assertArguments
	
	
	def changeHoraire(self, nouveauDebut, nouvelFin):
		"""
		Permet de changer le debut et la fin d'un Horaire en
		effectuant des vérifications (comme la fin après le début, etc).
		Lève une assertion en cas de mauvais emploi !
		@param self: L'argument implicite
		@param nouveauDebut: le nouvel Horaire de début
		@type nouveauDebut: entier naturel non nul
		@param nouvelFin: le nouvel Horaire de fin
		@type nouvelFin: entier naturel non nul
		@precondition: M{0 < nouveauDebut < nouvelFin}
		@raise AssertionError: si les paramètres sont mauvais
		"""
		self._assertArguments(nouveauDebut, nouvelFin)
		self._debut = nouveauDebut
		self._fin = nouvelFin
	#fin changeHoraire
	
	
	def __eq__(self, autre):
		"""
		Teste l'égalité entre deux Horaires.
		@param self: L'argument implicite
		@type autre: Horaire
		@param autre: l'horaire avec lequel faire la comparaison
		@rtype: bool
		@return: True si ces deux Horaires sont égaux, False sinon
		"""
		return ((self._debut == autre._debut) and (self._fin == autre._fin))
	#__eq__
	
#Horaire
