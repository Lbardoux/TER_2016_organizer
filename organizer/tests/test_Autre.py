#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.formation.Autre import *

class Test_Autre(unittest.TestCase):
	"""
	La classe de test de Autre
	"""

	def test_init_getters(self):
		"""
		Test du constructeur.
		"""
		cible = Autre(1, 25, 8, 13, "decrit toi")
		self.assertEqual(cible.idSeance, 1)
		self.assertEqual(cible.idGroupe, 25)
		self.assertEqual(cible.duree, 8)
		self.assertEqual(cible.idEnseignant, 13)
		self.assertEqual(cible.description, "decrit toi")
		cible = Autre(-1, 0, 6)
		self.assertEqual(cible.idSeance, 1)
		self.assertEqual(cible.idGroupe, 1)
		self.assertEqual(cible.duree, 6)
		self.assertEqual(cible.idEnseignant, 0)
		self.assertEqual(cible.description, "")
	#fin test_init_getters
	
	
	def test_setters(self):
		"""
		Tests des accesseurs
		"""
		cible = Autre(5, 5, 6, 7,"rien")
		cible.description = "nada"
		self.assertEqual(cible.description, "nada")
		cible.duree = -4
		self.assertEqual(cible.duree, 6)
		cible.duree = 8
		self.assertEqual(cible.duree, 8)
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

	

#fin Test_Autre

if __name__ == "__main__":
	unittest.main()
#fin if
