#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.formation.Formation import *

class Test_Formation(unittest.TestCase):
	"""
	La classe de test de Formation
	"""
	def test_init_getters(self):
		"""
		Test du constructeur.
		"""
	#fin test_init_getters
#fin Test_Formation

if __name__ == "__main__":
	unittest.main()
#fin if
