#!/usr/bin/python3
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.agenda.diff.Diff import *
from src.modele.agenda.Agenda import *

class Test_DIff(unittest.TestCase):
	"""
	Premiere version en TDD, ceux-là ne sont donc pas censé passer
	au debut, mais passeront au fur et à mesure.
	@author: Laurent Bardoux p1108365
	"""
	
	@classmethod
	def setUpClass(cls):
		"""A faire au tout début"""
		agenda1 = Agenda("premier", 2016)
		agenda2 = Agenda("second", 2016)
		cls.agenda1 = agenda1
		cls.agenda2 = agenda2
		cls.test = Diff(agenda1, agenda2)
	#setUpClass
	
	
	def test_init_agenda1(self):
		"""Teste si l'agenda 1 est bien initialisé"""
		self.assertTrue(self.agenda1 is self.test._agenda1)
	#test_init_agenda1
	
	
	def test_init_agenda2(self):
		"""Teste si l'agenda 2 est bien initialisé"""
		self.assertTrue(self.agenda2 is self.test._agenda2)
	#test_init_agenda2
	
	
	def test_init_differences(self):
		"""Teste si le dictionnaire des différence est bien initialisé"""
		self.assertEqual(len(self.test._differences), 0)
	#test_init_differences
	
	
	def test_init_moments(self):
		"""Teste si la liste des moments est bien initialisé"""
		self.assertEqual(len(self.test._differences), 0)
	#test_init_moments
	
	
	def test_get_agenda1(self):
		"""Teste la propriété get de _agenda1"""
		self.assertTrue(self.test.agenda1 is self.agenda1)
	#test_get_agenda1
	
	
	def test_get_agenda2(self):
		"""Teste la propriété get de _agenda2"""
		self.assertTrue(self.test.agenda2 is self.agenda2)
	#test_get_agenda2
	
	
	def test_get_moments(self):
		"""Teste la propriété get de _moments"""
		self.assertTrue(type(self.test.moments) is list)
	#test_get_moments
	
	
	def test_get_differences(self):
		"""teste la propriété get de la liste des différences"""
		self.assertTrue(type(self.test.differences) is dict)
	#test_get_differences
	
	
	def test_comparaison_rien_a_voir(self):
		"""Teste si la comparaison de 2 Agenda complètement différent renvoie bien une liste vide"""
		a1 = Agenda("rien", 2015)
		a2 = Agenda("rien", 2016)
		test = Diff(a1, a2)
		oracle = list()
		#test.comparer()
		#self.assertEqual(test._moments, oracle)
	#test_comparaison_rien_a_voir
	
	
	def test_petite_comparaison(self):
		"""Teste une comparaison minimale"""
		a1 = Agenda("rien", 2016)
		a2 = Agenda("rien", 2016)
		a1.ajouterCreneau(2015, 12, 1, 24, 28)
		a2.ajouterCreneau(2015, 12, 1, 24, 28)
		test = Diff(a1, a2)
		#test.comparer()
	#test_petite_comparaison
	
#Test_Diff

if __name__ == "__main__":
	unittest.main()
#if
