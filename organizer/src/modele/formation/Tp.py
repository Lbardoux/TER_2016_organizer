#!/usr/bin/python
# -*-coding:utf-8 -*
import Seance
class Tp(Seance.Seance):
	"""
	La classe tp qui hérite la classe seance
	@version : 1.0
	@author : Liu Zhuying
	"""
	def __init__(self, idTp, horaire):
		"""
		Le constructeur de la classe tp.
		@param self : L'argument implicite
		@param idTp : l'identifiant du groupe qui aura ce tp
		@type idTp : entier naturel non nul
		@type horaire : Horaire.
		@param horaire : L'horaire voulu
		"""
		super(Tp, self).__init__(idTp, horaire)
	#fin __init__
	
#fin Tp
