#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.formation.Tp import *

class Test_Tp(unittest.TestCase):
	"""
	La classe de test de Tp
	"""

	def test_init_getters(self):
		"""
		Test du constructeur.
		"""
		cible = Tp(1, 25, "decrit toi")
		self.assertEqual(cible.idSeance, 1)
		self.assertEqual(cible.idGroupe, 25)
		self.assertEqual(cible.description, "decrit toi")
		cible = Tp(-1, 0)
		self.assertEqual(cible.idSeance, 1)
		self.assertEqual(cible.idGroupe, 1)
		self.assertEqual(cible.description, "")
	#fin test_init_getters
	
	def test_setters(self):
		"""
		Tests des accesseurs
		"""
		cible = Tp(5, 5, "rien")
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
	

#fin Test_Tp

if __name__ == "__main__":
	unittest.main()
#fin if
