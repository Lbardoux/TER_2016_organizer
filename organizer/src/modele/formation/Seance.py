#!/usr/bin/python
# -*-coding:utf-8 -*

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../agenda")
from Creneau import Creneau

class Seance(Creneau):
	"""
	La classe mere pour tout element d'une formation.
	ELle contient donc toutes les informations communes aux différents
	composant d'une formation.
	Elle fait également le lien avec la modélisation d'un agenda, et
	définit en conséquence les éléments utilisables.
	@version : 1.0
	@author : Liu Zhuying
	@version : 2.0
	@author : Laurent Bardoux p1108365
	"""
	
	def __init__(self, idSeance, horaire):
		"""
		Le constructeur de la classe "abstraite" Seance.
		@param self : L'argument implicite
		@param idSeance : l'identifiant de cette Seance
		@type idSeance : entier naturel non nul
		@type horaire : Horaire.
		@param horaire : L'horaire voulu
		"""
		super(Seance, self).__init__(idSeance, horaire)
	#fin __init__
	
#fin Seance
