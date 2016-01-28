#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.formation.Groupe import *

class Test_Groupe(unittest.TestCase):
	"""
	La classe qui teste le module Groupe
	"""
	
	def test_init_property(self):
		"""
		Teste de l'initialisation et des propiétés
		"""
		nb = 25
		num = 18
		cible = Groupe(nb, num)
		self.assertEqual(cible.nbPersonne, nb)
		self.assertEqual(cible.numero, num)
		cible = Groupe(0, -1)
		self.assertEqual(cible.nbPersonne, 1)
		self.assertEqual(cible.numero, 1)
	#fin test_init_property
	
	
	def test_setters_property(self):
		"""
		Test les mutateurs via les propriétés
		"""
		cible = Groupe(25, 15)
		cible.numero = 0
		self.assertEqual(cible.numero, 15)
		cible.numero = 1
		self.assertEqual(cible.numero, 1)
		cible.nbPersonne = 0
		self.assertEqual(cible.nbPersonne, 25)
		cible.nbPersonne = 1
		self.assertEqual(cible.nbPersonne, 1)
	#fin test_setters_property
	
#fin Test_Groupe

if __name__ == "__main__":
	unittest.main()
