#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.contraintes.Precedence import *

class Test_Precedence(unittest.TestCase):
	"""
	Une classe qui teste le module Precedence
	@author: Laurent Bardoux p1108365
	"""
	
	def setUp(self):
		"""
		A faire avant chaque test
		"""
		self.prec = Precedence('a', 'b')
	#fin setUp
	
	def test_init_getters(self):
		"""
		Test sur le constructeur et les getters()
		"""
		self.assertEqual(self.prec.idAvant(), 'a')
		self.assertEqual(self.prec.idEnsuite(), 'b')
	#fin test_init_getters
	
	
	def test_injection(self):
		"""
		Test de la lambda crée par la fonction injectionContrainte
		"""
		fonction = self.prec.injectionContrainte()
		self.assertTrue(fonction(5, 8)) 
		self.assertFalse(fonction(8, 8)) 
		self.assertFalse(fonction(10, 8)) 
	#fin test_injection
	
#fin Test_Precedence


if __name__ == "__main__":
	unittest.main()
#fin if
