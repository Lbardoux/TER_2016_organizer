#!/usr/bin/python3
# -*-coding:utf-8 -*

import Seance
import Creneau

class Tp(Seance.Seance):
	"""
	La classe tp qui hérite la classe seance
	@version: 1.0
	@author: Liu Zhuying
	"""
	def __init__(self, idTp, horaire):
		"""
		Le constructeur de la classe tp.
		@param self: L'argument implicite
		@param idTp: l'identifiant du groupe qui aura ce tp
		@type idTp: entier naturel non nul
		@type horaire: Horaire.
		@param horaire: L'horaire voulu
		"""
		super(Tp, self).__init__(idTp, horaire)
	#__init__
	
	
	def versChaine(self):
		"""
		Retourne sous forme de chaine une description.
		C'est une surcharge de la meme opération venant de Creneau.
		@param self: L'argument implicite
		@rtype: str
		@return: une chaine descriptive
		"""
		return "Un TP nommé " + self._nom + " est prévu de " + self._horaire.debutstr + " à " + self._horaire.finstr
	#versChaine
	
	
	def __eq__(self, autre):
		"""
		Compare 2 L{Seance}s de type Tp entre eux
		@param self: L'argument implicite.
		@type autre: Creneau
		@param autre: Le second Creneau avec lequel comparer
		@rtype: bool
		@return: True si ils sont identiques, False sinon
		"""
		testSeance = Seance.Seance.__eq__(self, autre)
		#nos tests spécifiques à Tp
		return testSeance
	#__eq__
	
#Tp
