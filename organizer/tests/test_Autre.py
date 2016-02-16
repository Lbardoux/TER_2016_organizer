#!/usr/bin/python3
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.formation.Autre import *
from src.modele.agenda.Horaire import *
from src.modele.agenda.FabriqueCreneau import *

class Test_Autre(unittest.TestCase):
	"""Tests de la classe Autre"""
	
	def setUp(self):
		"""A faire avant chaque fonction"""
		self._fabrique = FabriqueCreneau()
	#setUp
	
	def test_eq_echec(self):
		"""Teste l'egalité entre 2 Creneaux qui échoue"""
		h = Horaire(15, 45)
		autre = self._fabrique.fabrique(CreneauxPossible.AUTRE, "iduidue", h)
		cren = self._fabrique.fabrique(CreneauxPossible.CRENEAU, "iduidue", h)
		self.assertFalse(autre == cren)
	#test_eq
	
	
	def test_eq_win(self):
		"""Teste l'egalité entre 2 Creneaux"""
		h = Horaire(15, 45)
		autre = self._fabrique.fabrique(CreneauxPossible.AUTRE, "iduidue", h)
		cren = self._fabrique.fabrique(CreneauxPossible.AUTRE, "iduidue", h)
		self.assertTrue(autre == cren)
	#test_eq
	
#Test_Autre

if __name__ == "__main__":
	unittest.main()
#if
