#!/usr/bin/python3
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
		"""Test de l'initialisation"""
		cible = Horaire(18, 22)
		self.assertEqual(cible._debut , 18)
		self.assertEqual(cible._fin , 22)
	#fin test_init
	
	
	def test_debut(self):
		"""Tests sur debut avec les propriétés"""
		cible = Horaire(25, 48)
		self.assertEqual(25, cible.debut)
		cible.debut = -1
		self.assertEqual(25, cible.debut)
		cible.debut = 26
		self.assertEqual(26, cible.debut)
	#fin test_debut
	
	
	def test_fin(self):
		"""Tests sur fin avec les propriétés"""
		cible = Horaire(15, 18)
		self.assertEqual(18, cible.fin)
		cible.fin = -8
		self.assertEqual(18, cible.fin)
		cible.fin = 42
		self.assertEqual(42, cible.fin)
		with self.assertRaises(AssertionError):
			cible.fin = 14
		#with
	#fin test_fin
	
	
	def test_changeHoraire(self):
		"""Tests de changeHoraire"""
		cible = Horaire(40, 48) # de 19 à 20h, pas cool ;(
	#fin test_changeHoraire
	
#fin Test_Horaire

if __name__ == "__main__":
	unittest.main()
#if
