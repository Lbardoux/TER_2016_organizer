#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.agenda.Horaire import *

class Test_Horaire(unittest.TestCase):
	"""
	La classe de test de la classe Horaire
	@author : Laurent Bardoux p1108365
	"""
	
	def test_init(self):
		"""
		Test de l'initialisation
		"""
		cible = Horaire(18, 22)
		self.assertEqual(cible._debut , 18)
		self.assertEqual(cible._fin , 22)
		with self.assertRaises(AssertionError):
			cible = Horaire(45, 51)
		#with
	#fin test_init
	
	
	def test_debut(self):
		"""
		Tests sur debut avec les propriétés
		"""
		cible = Horaire(55, 58)
		self.assertEqual(55, cible.debut)
		cible.debut = -1
		self.assertEqual(55, cible.debut)
		cible.debut = 56
		self.assertEqual(56, cible.debut)
		with self.assertRaises(AssertionError):
			cible.debut = 59
		#with
		with self.assertRaises(AssertionError):
			cible.debut = 45
		#with
	#fin test_debut
	
	
	def test_fin(self):
		"""
		Tests sur fin avec les propriétés
		"""
		cible = Horaire(15, 18)
		self.assertEqual(18, cible.fin)
		cible.fin = -8
		self.assertEqual(18, cible.fin)
		cible.fin = 42
		self.assertEqual(42, cible.fin)
		with self.assertRaises(AssertionError):
			cible.fin = 14
		#with
		with self.assertRaises(AssertionError):
			cible.fin = 58
		#with
	#fin test_fin
	
	
	def test_changeHoraire(self):
		"""
		Tests de changeHoraire
		"""
		cible = Horaire(40, 48) # de 19 à 20h, pas cool ;(
		with self.assertRaises(AssertionError):
			cible.changeHoraire(34, 49)
		#with
		with self.assertRaises(AssertionError):
			cible.changeHoraire(222, 241)
		#with
		cible.changeHoraire(222, 240)
		with self.assertRaises(AssertionError):
			cible.changeHoraire(240, 222)
		#with
	#fin test_changeHoraire
	
	
	def test_getJourDe(self):
		"""
		Tests de getJourDe
		"""
		cible = Horaire(1, 2)
		self.assertEqual(cible.getJourDe(1), cible.getJourDe(45))
		self.assertNotEqual(cible.getJourDe(84), cible.getJourDe(42))
		self.assertEqual(cible.getJourDe(57), cible.getJourDe(96))
		self.assertNotEqual(cible.getJourDe(235), cible.getJourDe(242))
	#fin test_getJourDe
	
	
	def test_getSemaineDe(self):
		"""
		Tests de getJourDe
		"""
		cible = Horaire(1, 2)
		self.assertEqual(cible.getSemaineDe(1), cible.getSemaineDe(240))
		self.assertNotEqual(cible.getSemaineDe(84), cible.getSemaineDe(241))
		self.assertEqual(cible.getSemaineDe(241), cible.getSemaineDe(480))
		self.assertNotEqual(cible.getSemaineDe(235), cible.getSemaineDe(242))
	#fin test_getSemaineDe
	
#fin Test_Horaire

if __name__ == "__main__":
	unittest.main()
#if
