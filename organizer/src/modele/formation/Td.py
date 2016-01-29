#!/usr/bin/python
# -*-coding:utf-8 -*
import Seance
class Td(Seance.Seance):
	"""
	La classe Td qui hérite la classe seance
	@version : 1.0
	@author : Liu Zhuying
	"""
	def __init__(self, idTd, idGroupe, description=""):
		"""
		Le constructeur de la classe Td.
		@param self : L'argument implicite
		@param idTd : l'identifiant du groupe qui aura ce Td
		@type idTd : entier naturel non nul
		@param idGroupe : l'identifiant du groupe qui aura ce Td
		@type idGroupe : entier naturel non nul
		@param description : Une courte description du Td.
		@type description : str
		"""
		super(Td, self).__init__(idTd, idGroupe, description)
	#fin __init__

#fin Td
