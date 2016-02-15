#!/usr/bin/python3
# -*-coding:utf-8 -*



class Modifier(object):
	"""
	Classe commune aux L{Annee}, L{Mois}, L{Semaine}, permettant
	de savoir si il y a de la donnée intéressante dedans.
	Ainsi si l'on veut sauvegarder, seules les classes ayant des
	L{Creneau} seront dumpées.
	@ivar _nbCreneaux: un entier représentant le nombre de créneaux présent.
	@author: Laurent Bardoux p1108365
	@version: 1.0
	"""

	def __init__(self):
		"""
		Initialisation de cette classe simple.
		@param self: L'argument implicite.
		"""
		self._nbCreneaux = 0
	#__init__
	
	
	@property
	def nbCreneaux(self):
		"""Permet de récupérer la valeur de _nbCreneau via une propriété get."""
		return self._nbCreneaux
	#nbCreneaux
	
	
	def ajoutDeCreneau(self):
		"""
		Symbolise l'ajout d'un L{Creneau}.
		Permet de tenir à jour le compteur.
		@param self: L'argument implicite.
		"""
		self._nbCreneaux += 1
	#ajoutDeCreneau
	
	
	def retraitDeCreneau(self):
		"""
		Symbolise le retrait d'un L{Creneau}.
		Permet de tenir à jour le compteur.
		@param self: L'argument implicite.
		"""
		if self.nbCreneaux > 0:
			self._nbCreneaux -= 1
		#if
	#retraitDeCreneau
	
#Modifier
