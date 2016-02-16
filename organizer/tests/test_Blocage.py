#!/usr/bin/python3
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.contraintes.Blocage import *

class Test_Blocage(unittest.TestCase):
	"""
	La classe de test de la contrainte Blocage
	@author : Laurent Bardoux p1108365
	"""
	
	def test_init_getter(self):
		"""
		Les tests du getter et du constructeur
		"""
		maliste = [1, 2, 3, 4, 5, 6]
		cible = Blocage(1,2,3,4,5,6)
		self.assertFalse(cible.valeurs() is None)
		self.assertEqual(len(cible.valeurs()), 6)
		for i, elt in enumerate(cible.valeurs()):
			self.assertEqual(elt, maliste[i])
		#fin for
	#fin test_init_getter


	def test_init_getter_2(self):
		"""
		Plus de tests sur les cas d'erreurs
		"""
		cible = Blocage(-1, 5, "lol")
		self.assertEqual(len(cible.valeurs()), 1)
	#fin test_init_getter_2

	def test_injection(self):
		"""
		Test de la lambda expression retournée.
		"""
		cible = Blocage(1,2,3,4,5,6)
		fonction = cible.injectionContrainte()
		self.assertTrue(fonction(18))
		self.assertTrue(fonction(0))
		self.assertFalse(fonction(6))
		self.assertFalse(fonction(1))
		self.assertFalse(fonction(3))
	#fin test_injection
	
#fin Test_Blocage

if __name__ == "__main__":
	unittest.main()
#fin if
