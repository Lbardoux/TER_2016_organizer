#!/usr/bin/python3
# -*-coding:utf-8 -*

from Observeur import Observeur

# Un décorateur pour ajouter les notifications facilements
def notifier(fonction):
	"""
	Une annotation à base de @ pour simplifier les notifications sans
	alourdir le corps d'une fonction.
	On s'en sert en annotant : @notifier.
	@type fonction: fonction
	@param fonction: la fonction qu'on a annoté.
	"""
	def vraiFonction(*param, **param2):
		#ça sent la ruse cette ligne, à améliorer
		self = param[0]
		v = fonction(*param, **param2)
		self.notifierObserveurs()
		return v
	
	return vraiFonction
#notifier


class Observable(object):
	"""
	L'alter-ego de la classe L{Observeur}.
	Elle offre et implémente tout le nécessaire à l'emploi du
	design pattern observateur.
	A l'inverse de Observeur, inutile de surcharger les fonctions dans son cas.
	En complément, elle offre un decorator, permettant de tagger les cas
	ou l'on doit notifier (mais sans propager d'arguments, hélas)
	@ivar _observeurs: une liste des observeurs connus
	@author: Laurent Bardoux p1108365
	@version: 1.0
	"""
	
	def __init__(self):
		"""
		Le constructeur de l'Observable, à appeller impérativement !
		@param self: L'argument implicite.
		"""
		self._observeurs = list()
	#__init__
	
	
	def ajouterObserveur(self, observeur):
		"""
		Va permettre d'ajouter un observeur à l'instance courante.
		Généralement, on procèdera comme cela, l'L{Observeur}, qui possède
		une référence sur l'Observable, va faire..
		M{observable.ajouterObserveur(self)}
		@param self: L'argument implicite.
		@type observeur: L{Observeur}
		@param observeur: L'observeur que l'on veut ajouter pour cette instance.
		@raise ReferenceError: si il est déjà dans la liste.
		"""
		if observeur in self._observeurs:
			raise ReferenceError("Déjà dans la liste")
		#if
		self._observeurs.append(observeur)
	#ajouterObserveur
	
	
	def enleverObserveur(self, observeur):
		"""
		Va permettre d'enlever un observeur à l'instance courante.
		Généralement, on procèdera comme cela, l'L{Observeur}, qui possède
		une référence sur l'Observable, va faire, avant de disparaitre.
		M{observable.enleverObserveur(self)}
		@param self: L'argument implicite.
		@type observeur: L{Observeur}
		@param observeur: L'observeur que l'on veut retirer pour cette instance.
		@raise ValueError: Si l'observeur n'est pas dans cette liste
		"""
		self._observeurs.remove(observeur)
	#enleverObserveur
	
	
	def notifierObserveurs(self, *arguments):
		"""
		Permet de notifier les observeurs de l'instance courante d'un
		changement d'état, pour qu'ils puissent se mettre à jour.
		@param self: L'argument implicite.
		@type arguments: list
		@param arguments: une liste d'arguments quelconque que l'on veut donner aux L{Observeur}s
		"""
		for o in self._observeurs:
			o.miseAJour(self, *arguments)
		#for
	#notifierObserveurs
	
#Observable
