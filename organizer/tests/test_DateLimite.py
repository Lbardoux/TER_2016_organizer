#!/usr/bin/python3
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.contraintes.DateLimite import *

class Test_DateLimite(unittest.TestCase):
	"""
	La classe qui teste le module DateLimite.py
	@author : Laurent Bardoux p1108365
	"""
	
	def setUp(self):
		"""
		A faire avant chaque test
		"""
		self.obj = DateLimite(5)
	#fin setUp
		
	
	def test_injection(self):
		"""
		Teste de la fermeture de la lambda expression
		"""
		fonction = self.obj.injectionContrainte()
		self.assertTrue(fonction(2))
		self.assertFalse(fonction(5))
		self.assertFalse(fonction(10))
	#fin test_injection
	
	
	def test_init_getter(self):
		"""
		Test du constructeur
		"""
		self.assertEqual(self.obj.limite(), 5)
	#fin test_init_getter

#fin Test_DateLimite

if __name__ == "__main__":
	unittest.main()
