#!/usr/bin/python
# -*-coding:utf-8 -*
from Enseignant import Enseignant
class ListeEnseignant(object):
	"""
	La classe qui contient une liste d'enseignants
	@ivar _liste: La liste d'enseignants
	@author: Zhuying LIU
	@version: 1.0
	"""
	def __init__(self):
		"""
		Le constructeur de la liste d'enseignants
		Par défaut la liste et vide
		@param self : L'argument implicite
		"""
		self._liste = []
	#__init__
	
	@property
	def taille(self):
		"""
		La taille de cette liste
		"""
		return len(self._liste)
	#taille
	
	@property
	def liste(self):
		"""
		La liste complete
		"""
		return self._liste
	#liste
	
	def ajouterEnseignant(self, nouveau):
		"""
		La fonction qui ajoute un enseignant dans cette liste
		@param self: L'argument implicite
		@param nouveau: l'enseignant à ajouter
		@type nouveau: un enseignant
		"""
		if type(nouveau) is Enseignant: 
			self._liste.append(nouveau)
	#ajouterEnseignant
	
	def supprimerEnseignant(self, unEnseignant):
		"""
		La fonction qui supprime un enseignant dans cette liste
		@param self: L'argument implicite
		@param unEnseignant: l'enseignant à supprimer
		@type unEnseignant: un enseignant dans cette liste
		"""
		if type(unEnseignant) is Enseignant: 
			for i in self._liste:
				if(i.idEnseignant == unEnseignant.idEnseignant):
					self._liste.remove(i)
					break
				#if
			#for
		#if
	#supprimerEnseignant
	
	def trouverEnseignant(self, chaine):
		"""
		La fonction qui cherche un enseignant par son nom et prenom
		@param self: L'argument implicite
		@param chaine: nom + " " + prenom
		@type chaine: str
		"""
		for i in self._liste:
			if i.nom +" "+i.prenom == chaine:
				return i
		return None
	#trouverEnseignant
		
#ListeEnseignant
