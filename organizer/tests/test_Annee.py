#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.agenda.Annee import *
from src.modele.agenda.Jour import *
import calendar

class Test_Annee(unittest.TestCase):
	"""
	La classe qui va tester Annee.
	@author : Laurent Bardoux p1108365.
	"""
	
	def test_init(self):
		"""Teste l'initialisation d'une Annee."""
		cible = Annee(2015)
		self.assertEqual(cible._an, 2015)
		self.assertEqual(cible._nbCreneaux, 0)
		self.assertEqual(len(cible._mois), 12)
	#test_init
	
	
	def test_premierJourAnnee(self):
		"""Teste la méthode qui renvoie le premier jour d'une année."""
		cible = Annee(2016)
		self.assertEqual(cible._premierJourAnnee(2016), VENDREDI)
		self.assertEqual(cible._premierJourAnnee(2015), JEUDI)
		self.assertEqual(cible._premierJourAnnee(2014), MERCREDI)
		self.assertEqual(cible._premierJourAnnee(2017), DIMANCHE)
	#test_premierJourAnnee
	
	
	def test_get_an(self):
		"""Teste de la propriété get de _an"""
		cible = Annee(2002)
		self.assertEqual(cible.an, 2002)
	#test_get_an
	
	
	@unittest.skip("inutile désormais, ici à titre de document")
	def test_isleap(self):
		"""Test de calendar.isleap()."""
		print(calendar.isleap(2016))
		print(calendar.isleap(2015))
		print(calendar.isleap(1900))
	#test_isleap
	
#Test_Annee


if __name__ == "__main__":
	unittest.main()
#if
