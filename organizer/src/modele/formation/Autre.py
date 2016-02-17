#!/usr/bin/python3
# -*-coding:utf-8 -*

import Seance
import Creneau

class Autre(Seance.Seance):
	"""
	La classe Autre qui hérite la classe seance
	Ceci represente le type de séance autre que CM TD TP Examen
	@version : 1.0
	@author : Liu Zhuying
	"""
	
	def __init__(self, idAutre, horaire):
		"""
		Le constructeur de la classe Autre.
		@param self : L'argument implicite
		@param idAutre : l'identifiant du groupe qui aura cet Autre
		@type idAutre : entier naturel non nul
		@type horaire : L{Horaire}.
		@param horaire : L'horaire voulu
		"""
		super(Autre, self).__init__(idAutre, horaire)
	#fin __init__
	
	
	def versChaine(self):
		"""
		Retourne sous forme de chaine une description.
		C'est une surcharge de la meme opération venant de Creneau.
		@param self: L'argument implicite
		@rtype: str
		@return: une chaine descriptive
		"""
		return "Quelque chose de spécial est réservé de " + self._horaire.debutstr + " à " + self._horaire.finstr
	#versChaine
	
	
	def __eq__(self, autre):
		"""
		Compare 2 L{Seance}s de type Autre entre eux
		@param self: L'argument implicite.
		@type autre: Creneau
		@param autre: Le second Creneau avec lequel comparer
		@rtype: bool
		@return: True si ils sont identiques, False sinon
		"""
		testSeance = Seance.Seance.__eq__(self, autre)
		#nos tests spécifiques à Autre
		return testSeance
	#__eq__
	
#fin Autre

