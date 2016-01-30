#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.formation.Cm import *

class Test_Cm(unittest.TestCase):
	"""
	La classe de test de Cm
	"""

	def test_init_getters(self):
		"""
		Test du constructeur.
		"""
		cible = Cm(1, 25, 13, "decrit toi")
		self.assertEqual(cible.idSeance, 1)
		self.assertEqual(cible.idGroupe, 25)
		self.assertEqual(cible.idEnseignant, 13)
		self.assertEqual(cible.description, "decrit toi")
		cible = Cm(-1, 0)
		self.assertEqual(cible.idSeance, 1)
		self.assertEqual(cible.idGroupe, 1)
		self.assertEqual(cible.idEnseignant, 0)
		self.assertEqual(cible.description, "")
	#fin test_init_getters
	
	
	def test_setters(self):
		"""
		Tests des accesseurs
		"""
		cible = Cm(5, 5, 7,"rien")
		cible.description = "nada"
		self.assertEqual(cible.description, "nada")
		cible.idEnseignant = -2
		self.assertEqual(cible.idEnseignant, 7)
		cible.idEnseignant = 14
		self.assertEqual(cible.idEnseignant, 14)
		cible.idGroupe = 0
		self.assertEqual(cible.idGroupe, 5)
		cible.idGroupe = 18
		self.assertEqual(cible.idGroupe, 18)
		cible.idSeance = 0
		self.assertEqual(cible.idSeance, 5)
		cible.idSeance = 18
		self.assertEqual(cible.idSeance, 18)
	#fin test_setters
	

#fin Test_Cm

if __name__ == "__main__":
	unittest.main()
#fin if
