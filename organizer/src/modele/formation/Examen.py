#!/usr/bin/python
# -*-coding:utf-8 -*
import Seance
class Examen(Seance.Seance):
	"""
	La classe Examen qui hérite la classe seance
	@version : 1.0
	@author : Liu Zhuying
	"""
	def __init__(self, idExamen, horaire):
		"""
		Le constructeur de la classe Examen.
		@param self : L'argument implicite
		@param idExamen : l'identifiant du groupe qui aura cet Examen
		@type idExamen : entier naturel non nul
		@type horaire : Horaire.
		@param horaire : L'horaire voulu
		"""
		super(Examen, self).__init__(idExamen, horaire)
	#fin __init__
	
#fin Examen
