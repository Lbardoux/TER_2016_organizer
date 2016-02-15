#!/usr/bin/python3
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.formation.Salle import *

class Test_Salle(unittest.TestCase):
	"""
	La classe de test de Seance
	"""

	def test_init_getters(self):
		"""
		Test du constructeur.
		"""
		cible = Salle(1, 25, 2)
		self.assertEqual(cible.idSalle, 1)
		self.assertEqual(cible.taille, 25)
		self.assertEqual(cible.typeSalle, 2)
		cible = Salle(-1, 0)
		self.assertEqual(cible.idSalle, 1)
		self.assertEqual(cible.taille, 1)
		self.assertEqual(cible.typeSalle, 0)
	#fin test_init_getters
	
	def test_setters(self):
		"""
		Tests des accesseurs
		"""
		cible = Salle(1, 25, 2)
		cible.idSalle = -2
		self.assertEqual(cible.idSalle, 1)
		cible.idSalle = 3
		self.assertEqual(cible.idSalle, 3)
		cible.taille = 0
		self.assertEqual(cible.taille, 25)
		cible.taille = 20
		self.assertEqual(cible.taille, 20)
		cible.typeSalle = 1
		self.assertEqual(cible.typeSalle, 1)
	#fin test_setters

#fin Test_Salle

if __name__ == "__main__":
	unittest.main()
#fin if
