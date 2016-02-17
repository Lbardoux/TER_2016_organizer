#!/usr/bin/python3
# -*-coding:utf-8 -*
import Seance
class Examen(Seance.Seance):
	"""
	La classe Examen qui hérite la classe seance
	@version: 1.0
	@author: Liu Zhuying
	"""
	def __init__(self, idExamen, horaire):
		"""
		Le constructeur de la classe Examen.
		@param self: L'argument implicite
		@param idExamen: l'identifiant du groupe qui aura cet Examen
		@type idExamen: entier naturel non nul
		@type horaire: Horaire.
		@param horaire: L'horaire voulu
		"""
		super(Examen, self).__init__(idExamen, horaire)
	#__init__
	
	
	def versChaine(self):
		"""
		Retourne sous forme de chaine une description.
		C'est une surcharge de la meme opération venant de Creneau.
		@param self: L'argument implicite
		@rtype: str
		@return: une chaine descriptive
		"""
		return "Un examen est prévu de " + self._horaire.debutstr + " à " + self._horaire.finstr
	#versChaine
	
	
	def __eq__(self, autre):
		"""
		Compare 2 L{Seance}s de type Examen entre eux
		@param self: L'argument implicite.
		@type autre: Creneau
		@param autre: Le second Creneau avec lequel comparer
		@rtype: bool
		@return: True si ils sont identiques, False sinon
		"""
		testSeance = Seance.Seance.__eq__(self, autre)
		#nos tests spécifiques à Examen
		return testSeance
	#__eq__
	
#Examen
