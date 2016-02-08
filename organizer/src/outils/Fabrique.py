#!/usr/bin/python
# -*-coding:utf-8 -*



class Fabrique(object):
	"""
	Une classe abstraite générique pour créer des fabriques plus facilements.
	Elle définit donc les bases communes à toutes les futurs fabrique,
	qui devront dériver de celle-ci.
	@ivar _choix : La gamme de choix, sous forme d'un dictionnaire.
	@author : Laurent Bardoux p1108365
	@version : 1.0
	"""
	
	def __init__(self, dictionnaire):
		"""
		Le constructeur qui prépare une fabrique pour l'utilisation.
		Le second paramètre définit son intervalle d'action.
		@param self : L'argument implicite.
		@type dictionnaire : dict(), mappant (clef --> fonction/lambda).
		@param dictionnaire : Les choix possibles pour la fabrique.
		@precondition : dictionnaire doit déjà etre rempli !
		"""
		self._choix = dictionnaire
	#__init__
	
	
	def fabrique(self, clef, *arguments):
		"""
		Ce qui va fabriquer votre objet.
		Attention, si la clef ne mappe rien, None sera retourné.
		@param self : L'argument implicite
		@type clef : ce que vous voulez.
		@param clef : Ce qui va permettre de choisir ce que l'on veut fabriquer.
		@type *arguments : un nombre variable d'arguments.
		@param *arguments : les arguments potentiels pour la fabrication.
		@precondition : clef doit exister dans la fabrique !
		"""
		# ici, None représente ce qu'il faut renvoyer si clef n'existe pas.
		resultat = self._choix.get(clef, None)
		if resultat is not None:
			return resultat(*arguments)
		#fin if
		return None
	#fin fabrique
	
#Fabrique
