#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.agenda.Modifier import *

class Test_Modifier(unittest.TestCase):
	"""
	La classe qui va tester Modifier.py
	@author : Laurent Bardoux p1108365
	"""
	
	def test_init(self):
		"""Testsi l'__init__ se passe bien."""
		cible = Modifier()
		self.assertEqual(cible._nbCreneaux, 0)
	#test_init
	
	
	def test_get_nbCreneau(self):
		"""Test de la propriété get de _nbCreneaux."""
		cible = Modifier()
		self.assertEqual(cible.nbCreneaux, 0)
		cible._nbCreneaux = 8
		self.assertEqual(cible.nbCreneaux, 8)
	#test_get_nbCreneau
	
	
	def test_set_nbCreneau_echoue_bien(self):
		"""Test si la propriété set génère bien une exception."""
		cible = Modifier()
		with self.assertRaises(AttributeError):
			cible.nbCreneaux = 8
		#with
	#test_set_nbCreneau_echoue_bien
	
	
	def test_ajoutCreneau(self):
		"""Test si l'ajout se passe bien"""
		cible = Modifier()
		i = 1
		while i < 150:
			cible.ajoutDeCreneau()
			self.assertEqual(cible.nbCreneaux, i)
			i += 1
		#while
	#test_ajoutCreneau
	
	
	def test_retraitCreneau(self):
		"""Test si le retrait fonctionne tant que nbCreneaux > 0"""
		cible = Modifier()
		cible._nbCreneaux = 25
		i = 50
		while i > 0:
			cible.retraitDeCreneau()
			i -= 1
			if i > 25:
				self.assertEqual(i-25, cible.nbCreneaux)
			else:
				self.assertEqual(0, cible.nbCreneaux)
			#if
		#while
	#test_retraitCreneau
	
#Test_Modifier

if __name__ == "__main__":
	unittest.main()
