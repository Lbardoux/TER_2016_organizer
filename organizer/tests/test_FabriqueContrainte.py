#!/usr/bin/python3
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.contraintes.FabriqueContrainte import *

class Test_FabriqueContrainte(unittest.TestCase):
	"""
	La classe qui va tester la fabrique
	"""
	
	def setUp(self):
		"""
		A faire a chaque test
		"""
		self.cible = FabriqueContrainte()
	#fin setUp
	
	
	def test_blocage(self):
		"""
		Test l'instanciation d'un Blocage
		"""
		blocage = self.cible.fabrique(Contraintes.BLOCAGE, 1, 2, 3)
		self.assertTrue(blocage is not None)
		fonction = blocage.injectionContrainte()
		self.assertTrue(fonction(5))
		self.assertFalse(fonction(2))
	#fin test_init

	def test_precedence(self):
		"""
		Test l'instanciation d'une Precedence
		"""
		element = self.cible.fabrique(Contraintes.PRECEDENCE, 25, 488)
		self.assertTrue(element is not None)
		fonction = element.injectionContrainte()
		self.assertTrue(fonction(5, 8))
		self.assertFalse(fonction(8, 5))
	#fin test_precedence
	
	
	def test_dateLimite(self):
		"""
		Test l'instanciation d'une DateLimite
		"""
		element = self.cible.fabrique(Contraintes.DATE_LIMITE, 25)
		self.assertTrue(element is not None)
		fonction = element.injectionContrainte()
		self.assertTrue(fonction(5))
		self.assertFalse(fonction(25))
		self.assertFalse(fonction(28))
	#fin test_dateLimite
	
	
	def test_obligation(self):
		"""
		Test l'instanciation d'une Obligation
		"""
		element = self.cible.fabrique(Contraintes.OBLIGATION, 25)
		self.assertTrue(element is not None)
		fonction = element.injectionContrainte()
		self.assertTrue(fonction(25))
		self.assertFalse(fonction(24))
		self.assertFalse(fonction(28))
	#fin test_obligation
	

#fin Test_FabriqueContrainte


if __name__ == "__main__":
	unittest.main()
#fin if
