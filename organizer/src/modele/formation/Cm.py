#!/usr/bin/python
# -*-coding:utf-8 -*
import Seance
class Cm(Seance.Seance):
	"""
	La classe Cm qui hérite la classe seance
	@version : 1.0
	@author : Liu Zhuying
	"""
	def __init__(self, idCm, idGroupe, idEnseignant = 0, description = ""):
		"""
		Le constructeur de la classe cm.
		@param self : L'argument implicite
		@param idCm : l'identifiant du groupe qui aura ce cm
		@type idCm : entier naturel non nul
		@param idGroupe : l'identifiant du groupe qui aura ce cm
		@type idGroupe : entier naturel non nul
		@param idEnseignant : l'identifiant de l'ensignant de ce CM
		@type idEnseignant : entier naturel
		@param description : Une courte description du cm.
		@type description : str
		"""
		super(Cm, self).__init__(idCm, idGroupe, idEnseignant, description)
	#fin __init__

#fin Cm
