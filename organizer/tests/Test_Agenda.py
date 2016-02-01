#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.agenda.Agenda import *

class Test_Agenda(unittest.TestCase):
	"""
	La classe qui teste la classe Agenda
	@author : Laurent Bardoux p1108365
	"""
	
	def setUp(self):
		"""
		A faire avant chaque test
		"""
		self.cible = Agenda("testons")
	#fin setUp
	
	
	def test_init(self):
		"""
		Teste le constructeur
		"""
		self.assertEqual(self.cible._nom, "testons")
		self.assertTrue(self.cible._pere is None)
		self.assertEqual(len(self.cible._listeFils), 0)
		self.assertEqual(len(self.cible._listeCreneaux), 0)
	#fin test_init
	
	
	def test_pere(self):
		"""
		Testes les propriétés liés à self._pere
		"""
		self.assertTrue(self.cible.pere is None)
		self.cible.pere = 25
		self.assertTrue(self.cible.pere is None)
		self.cible.pere = Agenda("Padre !")
		self.assertFalse(self.cible.pere is None)
	#fin test_pere
	
	
	def test_nom(self):
		"""
		Tests sur nom via les propriétés
		"""
		self.assertEqual(self.cible.nom, "testons")
		self.cible.nom = 25
		self.assertEqual(self.cible.nom, "testons")
		self.cible.nom = "bonjour"
		self.assertEqual(self.cible.nom, "bonjour")
	#fin test_nom
	
	
	def test_listeFils(self):
		"""
		Tests sur listeFils via les propriétés
		"""
		self.assertTrue(type(self.cible.listeFils) is list)
		self.cible.listeFils = 18
		self.assertTrue(type(self.cible.listeFils) is list)
	#fin test_listeFils
	
	
	def test_listeFils(self):
		"""
		Tests sur listeCreneaux via les propriétés
		"""
		self.assertTrue(type(self.cible.listeCreneaux) is list)
		self.cible.listeCreneaux = 18
		self.assertTrue(type(self.cible.listeCreneaux) is list)
	#fin test_listeCreneaux
	
	
	def test_insertionFils(self):
		"""
		Test des insertions d'agendas
		"""
		fils1 = Agenda("fiston1")
		fils2 = Agenda("fiston2")
		self.cible.insererFils(fils1, 18, fils2, "lol")
		self.assertEqual(len(self.cible.listeFils), 2)
		self.assertFalse(fils1.pere is None)
		self.assertFalse(fils2.pere is None)
	#fin test_insertionFils
	
	
	def test_insertionCreneaux(self):
		"""
		TODO
		"""
		self.assertEqual(1, 1)
	
	#fin test_insertionCreneaux
	
	
	def test_retirerFils(self):
		"""
		Test du retrait des fils dans la listeCreneaux
		"""
		fils1 = Agenda("fiston1")
		fils2 = Agenda("fiston2")
		fils3 = Agenda("fiston1")
		self.cible.insererFils(fils1, fils2, fils3)
		self.cible.retirerFils("fiston1")
		self.assertEqual(len(self.cible.listeFils), 1)
	#fin test_retirerFils
	
	
	def test_retirerCreneaux(self):
		"""
		TODO
		"""
		self.assertEqual(1, 1)
	
	#fin test_retirerCreneauxCreneaux
	
#fin Test_Agenda

if __name__ == "__main__":
	unittest.main()
#if