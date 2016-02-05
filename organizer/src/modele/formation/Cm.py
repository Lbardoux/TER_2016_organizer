#!/usr/bin/python
# -*-coding:utf-8 -*
import Seance
class Cm(Seance.Seance):
	"""
	La classe Cm qui hérite la classe seance
	@version : 1.0
	@author : Liu Zhuying
	"""
	
	def __init__(self, idCm, horaire):
		"""
		Le constructeur de la classe cm.
		@param self : L'argument implicite
		@param idCm : l'identifiant du groupe qui aura ce cm
		@type idCm : entier naturel non nul
		@type horaire : Horaire.
		@param horaire : L'horaire voulu
		"""
		super(Cm, self).__init__(idCm, horaire)
	#fin __init__

#fin Cm
