#!/usr/bin/python3
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.contraintes.Blocage import *
from src.modele.agenda.Horaire import *

class Test_Blocage(unittest.TestCase):
	"""
	La classe de test de la contrainte Blocage
	@author : Laurent Bardoux p1108365
	"""
	
	@classmethod
	def setUpClass(cls):
		"""A faire au début des tests"""
		cls.cible = Blocage("id", Horaire(14, 28))
	#setUpClass
	
	
	def setUp(self):
		"""A faire avant chaque test"""
		self.cible._raison = ""
	#setUp
	
	
	def test_init_raison(self):
		"""Teste si raison a bien été mis vide"""
		self.assertEqual(self.cible._raison, "")
	#test_init_raison
	
	
	def test_get_raison(self):
		"""Teste la propriété get de la _raison"""
		oracle = "parce que :D"
		self.cible._raison = oracle
		self.assertEqual(self.cible.raison, oracle)
	#test_get_raison
	
	
	def test_set_raison(self):
		"""Teste la propriété set de la _raison"""
		oracle = "parce que :D"
		self.cible.raison = oracle
		self.assertEqual(self.cible.raison, oracle)
	#test_set_raison
	
#Test_Blocage

if __name__ == "__main__":
	unittest.main()
#if
