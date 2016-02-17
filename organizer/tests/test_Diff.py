#!/usr/bin/python3
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.agenda.diff.Diff import *
from src.modele.agenda.Agenda import *
from src.modele.agenda.FabriqueCreneau import CreneauxPossible as CP

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
	
	
	def test_compare_meme_agendas(self):
		"""Teste la comparaison entre 2 agendas identiques"""
		a1 = Agenda("lol", 2015)
		a1.ajouterCreneau(2015, 11, 11, 8, 24, CP.CM)
		a1.ajouterCreneau(2015, 11, 11, 26, 32, CP.TP)
		a1.ajouterCreneau(2015, 12, 10, 26, 32, CP.TD)
		d = Diff(a1, a1)
		d.comparer()
		self.assertEqual(d.moments, [])
	#test_compare_meme_agendas
	
	
	def test_compare_2_agendas_differents(self):
		"""Teste la comparaison entre 2 agendas identiques"""
		a1 = Agenda("agenda 1", 2015)
		a1.ajouterCreneau(2015, 11, 11, 8, 24, CP.CM)
		a1.ajouterCreneau(2015, 11, 11, 26, 32, CP.TP)
		a1.ajouterCreneau(2015, 12, 10, 26, 32, CP.TD)
		
		a2 = Agenda("agenda 2", 2015)
		a2.ajouterCreneau(2015, 11, 11, 8, 24, CP.CM)
		a2.ajouterCreneau(2015, 11, 11, 26, 32, CP.TP)
		a2.ajouterCreneau(2015, 8, 10, 26, 32, CP.TD)
		
		d = Diff(a1, a2)
		d.comparer()
		#for clef in d.moments:
		#	print(clef)
		#	for i in d.differences[clef]:
		#		print(i)
		#	#if
		#if
	#test_compare_2_agendas_differents
	
#Test_Diff

if __name__ == "__main__":
	unittest.main()
#if
