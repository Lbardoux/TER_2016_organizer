#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.formation.Examen import *

class Test_Examen(unittest.TestCase):
	"""
	La classe de test de Examen
	"""

	def test_init_getters(self):
		"""
		Test du constructeur.
		"""
		cible = Examen(1, 25, "decrit toi")
		self.assertEqual(cible.idSeance, 1)
		self.assertEqual(cible.idGroupe, 25)
		self.assertEqual(cible.description, "decrit toi")
		cible = Examen(-1, 0)
		self.assertEqual(cible.idSeance, 1)
		self.assertEqual(cible.idGroupe, 1)
		self.assertEqual(cible.description, "")
	#fin test_init_getters
	
	def test_setters(self):
		"""
		Tests des accesseurs
		"""
		cible = Examen(5, 5, "rien")
		cible.description = "nada"
		self.assertEqual(cible.description, "nada")
		cible.idGroupe = 0
		self.assertEqual(cible.idGroupe, 5)
		cible.idGroupe = 18
		self.assertEqual(cible.idGroupe, 18)
		cible.idSeance = 0
		self.assertEqual(cible.idSeance, 5)
		cible.idSeance = 18
		self.assertEqual(cible.idSeance, 18)
	#fin test_setters
	

#fin Test_Examen

if __name__ == "__main__":
	unittest.main()
#fin if

