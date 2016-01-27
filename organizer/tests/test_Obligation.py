#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.contraintes.Obligation import *

class Test_Obligation(unittest.TestCase):
	"""
	La classe qui va gérer les tests unitaires pour Obligation
	@author : Laurent Bardoux p1108365
	@version : 1.0
	"""
	
	def test_init(self):
		"""
		Tests du constructeur et de l'accesseur dans la foulée.
		"""
		cible = Obligation(18)
		self.assertEqual(cible.valeur(), 18)
	#fin test_init
	
	
	def test_injectionContrainte(self):
		"""
		Test de la lambda obtenue lors de l'appel
		"""
		cible = Obligation(25)
		fonction = cible.injectionContrainte()
		self.assertFalse(fonction is None)
		self.assertTrue(fonction(25))
		self.assertFalse(fonction(5))
	#fin test_injectionContrainte

#fin Test_Obligation

if __name__ == "__main__":
	unittest.main()
#fin if
