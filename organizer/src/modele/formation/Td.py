#!/usr/bin/python
# -*-coding:utf-8 -*
import Seance
class Td(Seance.Seance):
	"""
	La classe Td qui hérite la classe seance
	@version : 1.0
	@author : Liu Zhuying
	"""
	def __init__(self, idTd, horaire):
		"""
		Le constructeur de la classe Td.
		@param self : L'argument implicite
		@param idTd : l'identifiant du groupe qui aura ce Td
		@type idTd : entier naturel non nul
		@type horaire : Horaire.
		@param horaire : L'horaire voulu
		"""
		super(Td, self).__init__(idTd, horaire)
	#fin __init__

#fin Td
