#!/usr/bin/python3
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.agenda.Horaire import Horaire
from src.modele.formation.Seance import *
#from src.modele.agenda.Creneau import *

class Test_Seance(unittest.TestCase):
	"""
	La classe de test de Seance
	"""
	
	def test_init(self):
		"""Test l'initialisation de l'instance"""
		horaire = Horaire(1, 15)
		cible = Seance(12, horaire)
	#test_init
	
#fin Test_Seance

if __name__ == "__main__":
	unittest.main()
#fin if
