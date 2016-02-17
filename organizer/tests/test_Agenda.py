#!/usr/bin/python3
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
	
	
	def test_listeAnnees(self):
		"""Teste la propriété get de _listeAnnees"""
		self.assertTrue(type(self.cible.listeAnnees) is list)
	#test_listeAnnees
	
	
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
		self.cible.insererFils(fils1, fils2)
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
		c1 = self.cible.ajouterCreneau(2015, 5, 24, 12, 18)
		c2 = self.cible.ajouterCreneau(2015, 5, 24, 18, 24)
		self.cible.supprimerCreneau(2015, 5, 24, c1)
		self.assertEqual(self.cible._listeAnnees[0].nbCreneaux, 1)
	#test_supprimerCreneau_ok
	
	
	def test_supprimerCreneau_echec_local(self):
		"""Teste la suppression qu iéchoue à cause d'un mauvais numéro d'année"""
		c1 = self.cible.ajouterCreneau(2015, 5, 24, 12, 18)
		c2 = self.cible.ajouterCreneau(2015, 5, 24, 18, 24)
		with self.assertRaises(ValueError):
			self.cible.supprimerCreneau(2014, 15, 14, 25)
		#with
	#test_supprimerCreneau_echec_local
	
	@unittest.skip("")
	def test_supprimerCreneau_echec_interne(self):
		"""Teste la suppression qui échoue plus bas à cause des arguments"""
		c1 = self.cible.ajouterCreneau(2015, 5, 24, 12, 18)
		c2 = self.cible.ajouterCreneau(2015, 5, 24, 18, 24)
		with self.assertRaises(ValueError):
			self.cible.supprimerCreneau(2015, 18, 24, None)
		#with
	#test_supprimerCreneau_echec_interne
	
	
	def test_recupererSemaineParNumJour_ok(self):
		"""Teste la récupération en succes"""
		test = self.cible.recupererSemaineParNumJour(2016, 5, 5)
		self.assertIsNotNone(test)
	#test_recupererSemaineParNumJour_ok
	
	
	def test_recupererSemaineParNumJour_echec(self):
		"""Teste la récupération en echec"""
		with self.assertRaises(Exception):
			self.cible.recupererSemaineParNumJour(2016, 35, 5)
		#with
	#test_recupererSemaineParNumJour_echec
	
	
	def test_recupererJour_ok(self):
		"""Teste la recuperation d'un jour avec de bons arguments"""
		#cela renverra forcément quelque chose
		listeMois = [i+1 for i in range(12)]
		listeJourCommuns = [i+1 for i in range(27)]
		anneecibles = [2005, 2016, 2012]
		
		for i in anneecibles:
			for j in listeMois:
				for k in listeJourCommuns:
					self.assertTrue(type(self.cible.recupererJour(i, j, k)) is list)
				#for
			#for
		#for
	#test_recupererJour_ok
	
	
	def test_recupererJour_echec(self):
		"""Teste la recuperation d'un jour en echec si les arguments sont mauvais"""
		for i in [-1, 0, 13]:
			with self.assertRaises(ValueError):
				self.cible.recupererJour(2015, i, 15)
			#with
		#for
	#test_recupererJour_ok
	
#fin Test_Agenda

if __name__ == "__main__":
	unittest.main()
#if
