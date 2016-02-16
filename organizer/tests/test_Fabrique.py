#!/usr/bin/python3
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.outils.Fabrique import *

class Test_Fabrique(unittest.TestCase):
	"""
	La classe qui teste la Fabrique Générique.
	@author : Laurent Bardoux p1108365
	"""
	
	def _fonction(self, x, y):
		"""Renvoi le max entre x et y"""
		return y if y > x else x
	#_fonction
	
	
	def setUp(self):
		"""A faire avant chaque test"""
		self.dico = {
			"1" : lambda x : x,
			"2" : lambda x, y : x if x < y else y,
			"3" : self._fonction
		}
		self.cible = Fabrique(self.dico)
	#setUp
	
	
	def test_init(self):
		"""Teste l'instanciation d'une Fabrique"""
		self.assertTrue(self.cible._choix is self.dico)
	#test_init
	
	
	def test_fabrique(self):
		"""Teste si la fabrication est correcte"""
		x = 8
		y = 9
		self.assertEqual(self.cible.fabrique("1", x), x)
		self.assertEqual(self.cible.fabrique("2", x, y), x)
		self.assertEqual(self.cible.fabrique("3", x, y), y)
	#test_fabrique


	def test_fabrique_echec(self):
		"""Teste l'echec d'une fabrication en cas de mauvaise clef"""
		self.assertTrue(self.cible.fabrique(25, 45, 57) is None)
	#test_fabrique_echec
	
#Test_Fabrique

if __name__ == "__main__":
	unittest.main()
