#!/usr/bin/python3
# -*-coding:utf-8 -*
import Seance
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
		@type horaire : Horaire.
		@param horaire : L'horaire voulu
		"""
		super(Autre, self).__init__(idAutre, horaire)
	#fin __init__
	
#fin Autre

