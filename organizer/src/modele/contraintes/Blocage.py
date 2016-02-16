#!/usr/bin/python33
# -*-coding:utf-8 -*

import Contrainte

class Blocage(Contrainte.Contrainte):
	"""
	La classe qui définit une contrainte de verrouillage d'un horaire
	Par exemple, il ne peux y avoir aucun cours entre 13h et 14h.
	@ivar _valeurs: la liste des valeurs interdites.
	@author: Laurent Bardoux p1108365
	@version: 1.0
	"""
	
	def __init__(self, *valeurs):
		"""
		Le constructeur de cette classe
		@precondition: M{self is not None} && M{valeurs => multiples entiers}
		@postcondition: self est bien initialisé, et la liste correctement parsée.
		@param self: L'argument implicite.
		@param valeurs: une nombre +/- fini d'entiers
		@type valeurs: liste d'entiers naturels
		"""
		self._valeurs = [n for n in valeurs if type(n) is int and n >= 0]
		
	#fin __init__


	def injectionContrainte(self):
		"""
		La fonction qui retourne une lambda expression exprimant un blocage.
		Via une fermeture sur son argument _valeurs.
		@precondition: M{self is not None} et self préalablement initialisé.
		@param self: L'argument implicite.
		"""
		return lambda x : self.estPasDansListe(x)

	#fin injectionContrainte


	def estPasDansListe(self, valeur):
		"""
		Fonction temporaire qui va effectuer le travail.
		Compare L{valeur} à tous les éléments de la liste _valeurs
		@precondition: self doit etre initialisé, et not None
		@return: true si valeur n'est pas dans la liste, false sinon
		"""
		liste = [n for n in self._valeurs if n == valeur]
		return not liste
	#fin estPasDansListe


	def valeurs(self):
		"""
		L'accesseur pour récupérer la liste des valeurs interdites.
		@param self: L'argument implicite
		@precondition: self doit etre préalablement construit
		@postcondition: self n'est pas modifié à l'issue de cet appel.
		@return: la liste d'entiers contenue dans cet objet.
		"""
		return self._valeurs
	#fin valeurs

#fin Blocage
