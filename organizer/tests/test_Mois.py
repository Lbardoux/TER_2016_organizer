#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.agenda.Mois import *
import src.modele.agenda.Jour

class Test_Mois(unittest.TestCase):
	"""
	La classe qui teste la classe Mois.
	@author : Laurent Bardoux p1108365
	"""
	
	def test_initialisation(self):
		"""Teste l'initialisation"""
		cible = Mois(FEVRIER, Jour.LUNDI, 25)
		self.assertEqual(cible._nom, FEVRIER)
		self.assertEqual(cible._nbJours, 25)
		self.assertEqual(cible._jourApres, Jour.VENDREDI)
	#test_initialisation
	
	
	def test_get_nbjours(self):
		"""Teste de la propriété get de _nbJours."""
		cible = Mois(FEVRIER, Jour.LUNDI, 25)
		self.assertEqual(25, cible.nbJours)
	#test_get_nbjours
	
	
	def test_get_nom(self):
		"""Teste de la propriété get de _nom."""
		cible = Mois(FEVRIER, Jour.LUNDI, 25)
		self.assertEqual(FEVRIER, cible.nom)
	#test_get_nbjours


	def test_get_jourApres(self):
		"""Teste de la propriété get de _jourApres."""
		cible = Mois(FEVRIER, Jour.LUNDI, 25)
		self.assertEqual(cible._jourApres, Jour.VENDREDI)
	#test_get_nbjours
	
	
	def test_get_semaines(self):
		"""Teste de la propriété get de _semaines."""
		cible = Mois(FEVRIER, Jour.LUNDI, 25)
		self.assertTrue(type(cible.semaines) is list)
		self.assertEqual(len(cible.semaines), 4)
	#test_get_nbjours
	
	
	def test_recupererSemaine_ok(self):
		"""Teste d'une récupération de semaine qui marche."""
		cible = Mois(FEVRIER, Jour.MERCREDI, 29)
		self.assertTrue(cible.recupererSemaineParNumJour(23) is not None)
	#test_recupererSemaine_ok
	
	
	def test_recupererSemaine_echec(self):
		"""Teste d'une récupération de semaine qui échoue."""
		cible = Mois(FEVRIER, Jour.MERCREDI, 29)
		self.assertTrue(cible.recupererSemaineParNumJour(-1) is None)
		self.assertTrue(cible.recupererSemaineParNumJour(38) is None)
		self.assertTrue(cible.recupererSemaineParNumJour(31) is None)
	#test_recupererSemaine_echec
	
	
	def test_recupererSemaine_echec2(self):
		"""Teste d'une récupération de semaine qui échoue (encore)."""
		cible = Mois(FEVRIER, Jour.DIMANCHE, 23)
		self.assertTrue(cible.recupererSemaineParNumJour(-1) is None)
		self.assertTrue(cible.recupererSemaineParNumJour(38) is None)
		self.assertTrue(cible.recupererSemaineParNumJour(31) is None)
		self.assertTrue(cible.recupererSemaineParNumJour(24) is None)
	#test_recupererSemaine_echec2
	
#Test_Mois

if __name__ == "__main__":
	unittest.main()
