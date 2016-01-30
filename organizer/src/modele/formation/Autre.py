#!/usr/bin/python
# -*-coding:utf-8 -*
import Seance
class Autre(Seance.Seance):
	"""
	La classe Autre qui hérite la classe seance
	Ceci represente le type de séance autre que CM TD TP Examen
	@version : 1.0
	@author : Liu Zhuying
	"""
	def __init__(self, idAutre, idGroupe, idEnseignant = 0, description = ""):
		"""
		Le constructeur de la classe Autre.
		@param self : L'argument implicite
		@param idAutre : l'identifiant du groupe qui aura cet Autre
		@type idAutre : entier naturel non nul
		@param idGroupe : l'identifiant du groupe qui aura cet Autre
		@type idGroupe : entier naturel non nul
		@param idEnseignant : l'identifiant de l'ensignant de cet Autre
		@type idEnseignant : entier naturel
		@param description : Une courte description du Autre.
		@type description : str
		"""
		super(Autre, self).__init__(idAutre, idGroupe, idEnseignant, description)
	#fin __init__
	
#fin Autre
