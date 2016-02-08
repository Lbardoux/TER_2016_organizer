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
		"""A faire avant chaque test"""
		self.cible = Agenda("testons", 2016)
	#fin setUp
	
	
	def test_init(self):
		"""Teste le constructeur"""
		self.assertEqual(self.cible._nom, "testons")
		self.assertTrue(self.cible._pere is None)
		self.assertEqual(len(self.cible._listeFils), 0)
		self.assertEqual(len(self.cible._listeAnnees), 1)
	#fin test_init
	
	
	def test_pere(self):
		"""Testes les propriétés liés à self._pere"""
		self.assertIsNone(self.cible.pere)
		self.cible.pere = 25
		self.assertIsNotNone(self.cible.pere)
		self.cible.pere = Agenda("Padre !", 2015)
		self.assertIsNotNone(self.cible.pere)
	#fin test_pere
	
	
	def test_nom(self):
		"""Tests sur nom via les propriétés"""
		self.assertEqual(self.cible.nom, "testons")
		self.cible.nom = 25
		self.assertEqual(self.cible.nom, "testons")
		self.cible.nom = "bonjour"
		self.assertEqual(self.cible.nom, "bonjour")
	#fin test_nom
	
	
	def test_listeFils(self):
		"""Tests sur listeFils via les propriétés"""
		self.assertTrue(type(self.cible.listeFils) is list)
		self.cible.listeFils = 18
		self.assertTrue(type(self.cible.listeFils) is list)
	#fin test_listeFils
	
	
	def test_insertionFils(self):
		"""Test des insertions d'agendas"""
		fils1 = Agenda("fiston1", 2010)
		fils2 = Agenda("fiston2", 1850)
		self.cible.insererFils(fils1, 18, fils2, "lol")
		self.assertEqual(len(self.cible.listeFils), 2)
		self.assertFalse(fils1.pere is None)
		self.assertFalse(fils2.pere is None)
	#fin test_insertionFils
	
	
	def test_retirerFils(self):
		"""Test du retrait des fils dans la listeCreneaux"""
		fils1 = Agenda("fiston1", 2015)
		fils2 = Agenda("fiston2", 2015)
		fils3 = Agenda("fiston1", 2015)
		self.cible.insererFils(fils1, fils2, fils3)
		self.cible.retirerFils("fiston1")
		self.assertEqual(len(self.cible.listeFils), 1)
	#fin test_retirerFils
	
	
	def test_ajouterCreneau_ok(self):
		"""Teste l'ajout d'un creneau quand tout va bien"""
		self.assertIsNotNone(self.cible.ajouterCreneau(2016, 5, 24, 12, 18))
		self.assertEqual(self.cible._listeAnnees[0].nbCreneaux, 1)
	#test_ajouterCreneau_ok
	
	
	def test_ajouterCreneau_ok_vivification(self):
		"""Teste l'ajout d'un creneau quand tout va bien, avec auto-vivification"""
		self.assertIsNotNone(self.cible.ajouterCreneau(2015, 5, 24, 12, 18))
		self.assertEqual(len(self.cible._listeAnnees), 2)
	#test_ajouterCreneau_ok_vivification
	
	
	def test_ajouterCreneau_echec_interne(self):
		"""
		Teste l'ajout d'un creneau en echec à cause d'une erreur d'argument
		dans l'arborescence
		"""
		with self.assertRaises(Exception):
			self.cible.ajouterCreneau(2008, 18, 15, 15, 18)
		#with
	#test_ajouterCreneau_echec_interne
	
	
	def test_supprimerCreneau_ok(self):
		"""Teste la suppression lorsque tout est ok"""
		self.assertIsNotNone(self.cible.ajouterCreneau(2015, 5, 24, 12, 18))
		self.assertIsNotNone(self.cible.ajouterCreneau(2015, 5, 24, 18, 24))
		self.cible.supprimerCreneau(2015, 5, 24, 1)
		self.assertEqual(self.cible._listeAnnees[1].nbCreneaux, 1)
	#test_supprimerCreneau_ok
	
	
	def test_supprimerCreneau_echec_local(self):
		"""Teste la suppression qu iéchoue à cause d'un mauvais numéro d'année"""
		self.assertIsNotNone(self.cible.ajouterCreneau(2015, 5, 24, 12, 18))
		self.assertIsNotNone(self.cible.ajouterCreneau(2015, 5, 24, 18, 24))
		with self.assertRaises(Exception):
			self.cible.supprimerCreneau(2014, 15, 14, 25, 25)
		#with
	#test_supprimerCreneau_echec_local
	
	
	def test_supprimerCreneau_echec_interne(self):
		"""Teste la suppression qu iéchoue plus bas à cause des arguments"""
		self.assertIsNotNone(self.cible.ajouterCreneau(2015, 5, 24, 12, 18))
		self.assertIsNotNone(self.cible.ajouterCreneau(2015, 5, 24, 18, 24))
		with self.assertRaises(Exception):
			self.cible.supprimerCreneau(2015, 18, 24, 1)
		#with
	#test_supprimerCreneau_echec_interne
	
#fin Test_Agenda

if __name__ == "__main__":
	unittest.main()
#if
