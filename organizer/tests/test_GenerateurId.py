#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.outils.GenerateurId import *

class Test_GenerateurId(unittest.TestCase):
	"""
	La classe qui teste un GenerateurId.
	@author : Laurent Bardoux p1108365
	"""
	
	def test_init(self):
		"""Teste la construction de cet objet"""
		lam = lambda x : x+1
		cible = GenerateurId(0, lam)
		self.assertEqual(0, cible._idDepart)
		self.assertEqual(0, cible._idActuel)
		self.assertEqual(lam, cible._increment)
	#test_init
	
	
	def test_suivant(self):
		"""Teste la methode suivant"""
		lam = lambda x : x+1
		cible = GenerateurId(0, lam)
		i = 0
		while i < 50:
			self.assertEqual(i, cible.suivant())
			i += 1
		#while
	#test_suivant
	
#Test_GenerateurId

if __name__ == "__main__":
	unittest.main()
