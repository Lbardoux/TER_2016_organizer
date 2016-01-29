#!/usr/bin/python
# -*-coding:utf-8 -*
import Seance
class Tp(Seance.Seance):
	"""
	La classe tp qui hérite la classe seance
	@version : 1.0
	@author : Liu Zhuying
	"""
	def __init__(self, idTp, idGroupe, description=""):
		"""
		Le constructeur de la classe tp.
		@param self : L'argument implicite
		@param idTp : l'identifiant du groupe qui aura ce tp
		@type idTp : entier naturel non nul
		@param idGroupe : l'identifiant du groupe qui aura ce tp
		@type idGroupe : entier naturel non nul
		@param description : Une courte description du tp.
		@type description : str
		"""
		super(Tp, self).__init__(idTp, idGroupe, description)
	#fin __init__
	
#fin Tp
