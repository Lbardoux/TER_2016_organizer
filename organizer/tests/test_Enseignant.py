#!/usr/bin/python3
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.formation.Enseignant import *

class Test_Enseignant(unittest.TestCase):
	"""
	La classe de test de Seance
	"""

	def test_init_getters(self):
		"""
		Test du constructeur.
		"""
		cible = Enseignant(1, "CANIOU", "Yves")
		self.assertEqual(cible.idEnseignant, 1)
		self.assertEqual(cible.nom, "CANIOU")
		self.assertEqual(cible.prenom, "Yves")
		cible = Enseignant(-1, "", "coco")
		self.assertEqual(cible.idEnseignant, 1)
		self.assertEqual(cible.nom, "DEFAUTE")
		self.assertEqual(cible.prenom, "coco")
	#fin test_init_getters
	
	def test_setters(self):
		"""
		Tests des accesseurs
		"""
		cible = Enseignant(5, "BLA", "lol")
		cible.nom = " "
		self.assertEqual(cible.nom, "BLA")
		cible.nom = "  "
		self.assertEqual(cible.prenom, "lol")
		cible.prenom = "nada"
		self.assertEqual(cible.prenom, "nada")
		cible.nom = "naa"
		self.assertEqual(cible.nom, "naa")
		cible.idEnseignant = 0
		self.assertEqual(cible.idEnseignant, 5)
		cible.idEnseignant = 18
		self.assertEqual(cible.idEnseignant, 18)
		
	#fin test_setters

#fin Test_Enseignant

if __name__ == "__main__":
	unittest.main()
#fin if
