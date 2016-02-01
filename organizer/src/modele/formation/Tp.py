#!/usr/bin/python
# -*-coding:utf-8 -*
import Seance
class Tp(Seance.Seance):
	"""
	La classe tp qui hérite la classe seance
	@version : 1.0
	@author : Liu Zhuying
	"""
	def __init__(self, idTp, idGroupe, duree, idEnseignant = 0, description = ""):
		"""
		Le constructeur de la classe tp.
		@param self : L'argument implicite
		@param idTp : l'identifiant du groupe qui aura ce tp
		@type idTp : entier naturel non nul
		@param idGroupe : l'identifiant du groupe qui aura ce tp
		@type idGroupe : entier naturel non nul
		@param duree : la duree qui aura ce Tp
		@type duree : entier naturel non nul
		@param idEnseignant : l'identifiant de l'ensignant de ce Tp
		@type idEnseignant : entier naturel
		@param description : Une courte description du tp.
		@type description : str
		"""
		super(Tp, self).__init__(idTp, idGroupe, duree, idEnseignant, description)
	#fin __init__
	
#fin Tp
