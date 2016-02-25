#!/usr/bin/python3
# -*-coding:utf-8 -*

class Groupe(object):
	"""
	La classe qui définit un groupe pour une formation.
	Ce groupe est commun à toutes les UEs disponibles dans cette formation.
	@ivar _numero: Le numéro du groupe au sein de la formation
	@ivar _nbPersonne: le nombre de personnes dans ce groupe.
	@author: Laurent Bardoux p1108365
	@version: 1.0
	"""
	
	def __init__(self, nbPersonne, numero):
		"""
		Le constructeur de cette classe.
		@precondition: M{numero > 0} and M{nbPersonne > 0}
		@postcondition: self est bien initialisé.
		@param self: L'argument implicite de la fonction
		@param nbPersonne: le nombre de personne dans ce groupe
		@type nbPersonne: entier naturel non nul
		@param numero: le nombre de personne dans ce groupe
		@type numero: entier naturel non nul
		"""
		if nbPersonne > 0:
			self._nbPersonne = nbPersonne
		else:
			self._nbPersonne = 1
		if numero > 0:
			self._numero = numero
		else:
			self._numero = 1
	#__init__
	
	
	@property
	def nbPersonne(self):
		"""Un accesseur pour le nombre de personne du groupe."""
		return self._nbPersonne
	#getNbPersonne
	
	
	@nbPersonne.setter
	def nbPersonne(self, nouveauNombre):
		"""
		Un mutateur pour le numero du groupe.
		Attention, aucune vérification sur les doublons !
		"""
		if nouveauNombre > 0:
			self._nbPersonne = nouveauNombre
	#setNbPersonne
	
	
	@property
	def numero(self):
		"""Un accesseur pour le numero de ce groupe."""
		return self._numero
	#getNumero
	
	
	@numero.setter
	def numero(self, nouveauNumero):
		"""
		Un mutateur pour le numero du groupe.
		Attention, aucune vérification sur les doublons !
		@precondition: M{nouveauNumero > 0}
		@postcondition: si nouveauNumero est correct, alors le numero du groupe change.
		"""
		if nouveauNumero > 0:
			self._numero = nouveauNumero
	#setNumero
	
#Groupe
