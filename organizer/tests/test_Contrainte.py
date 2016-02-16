#!/usr/bin/python3
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.contraintes.Contrainte import *

class Test_Contrainte(unittest.TestCase):
	"""
	La classe qui teste le module Contrainte
	@author :Laurent Bardoux p1108365
	"""	
	
	def test_injection(self):
		"""
		La fonction de test de la methode injectionContrainte, qui renvoie
		la lambda expression identité dans ce cas là
		"""
		test = Contrainte()
		lambdaFonction = test.injectionContrainte()
		valeur = 8
		self.assertEqual(valeur, lambdaFonction(valeur))
		
		valeur2 = "olol"
		self.assertEqual(valeur2, lambdaFonction(valeur2))
	#fin test_injection
	
#fin Test_Contrainte



if __name__ == "__main__":
	unittest.main()
#fin if
