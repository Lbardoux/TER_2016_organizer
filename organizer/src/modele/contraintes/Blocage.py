#!/usr/bin/python3
# -*-coding:utf-8 -*

import Creneau

class Blocage(Creneau.Creneau):
	"""
	La classe qui définit une contrainte de verrouillage d'un horaire
	Par exemple, il ne peux y avoir aucun cours entre 13h et 14h.
	@ivar _raison: la raison pour laquelle ce L{Creneau} est verrouillé.
	@author: Laurent Bardoux p1108365
	@version: 2.0
	"""
	
	def __init__(self, ident, horaire):
		"""
		Le constructeur de cette classe.
		La raison ne sera pas renseigné immédiatemment, il faudra le faire via
		les propriétés.
		@param self: L'argument implicite.
		@type ident: object
		@param ident: l'identificateur voulu pour ce créneaux
		@type horaire: L{Horaire}
		@param horaire: l'horaire voulue
		"""
		super(Blocage, self).__init__(ident, horaire)
		self._raison = ""
	#__init__
	
	
	@property
	def raison(self):
		"""Une propriété get pour la raison du blocage."""
		return self._raison
	#raison
	
	
	@raison.setter
	def raison(self, valeur):
		"""Une propriété set pour la raison du Blocage."""
		self._raison = valeur
	#raison
	
	
	def versChaine(self):
		"""
		Retourne sous forme de chaine une description du Creneau.
		Elle doit etre surchargé par les classes dérivées.
		@param self: L'argument implicite
		@rtype: str
		@return: une chaine descriptive
		"""
		return "Le créneau entre " + self._horaire.debutstr + " et " + self._horaire.finstr + " est bloqué !"
	#versChaine
	
#Blocage
