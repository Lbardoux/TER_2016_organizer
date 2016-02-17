#!/usr/bin/python3
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.agenda.Mois import *
from src.modele.agenda.Jour import *

class Test_Mois(unittest.TestCase):
	"""
	Teste la classe Mois.
	@author : Laurent Bardoux p1108365
	@version : 2.0
	"""
	
	def setUp(self):
		"""A faire avant chaque test."""
		self.cible = Mois(JANVIER, LUNDI, 31)
	#setUp
	
	
	def test_init(self):
		"""Teste si la construction se passe bien"""
		self.assertEqual(self.cible.nbCreneaux, 0)
		self.assertEqual(self.cible._nom, JANVIER)
		self.assertEqual(self.cible._nbJours, 31)
		self.assertTrue(self.cible._semaines)
	#test_init
	
	
	def test_get_nom(self):
		"""Teste la propriété get du _nom"""
		self.assertEqual(JANVIER, self.cible.nom)
	#test_get_nom
	
	
	def test_get_semaines(self):
		"""Teste la propriété get du _semaines"""
		self.assertTrue(type(self.cible.semaines) is list)
	#test_get_semaines
	
	
	def test_get_jourApres(self):
		"""Teste la propriété get du _jourApres"""
		self.assertIsNotNone(self.cible.jourApres)
	#test_get_jourApres
	
	
	def test_get_nbJours(self):
		"""Teste la propriété get du _nbJours"""
		self.assertEqual(self.cible.nbJours, 31)
	#test_get_nbJours
	
	
	def test_recupererSemaineParNumJour_ok(self):
		"""Teste cette méthode de récupération en succes"""
		for i in [elt+1 for elt in range(31)]:
			self.assertIsNotNone(self.cible.recupererSemaineParNumJour(i))
		#for
	#test_recupererSemaineParNumJour_ok
	
	
	def test_recupererSemaineParNumJour_echec(self):
		"""Teste cette méthode de récupération en echec"""
		self.assertIsNone(self.cible.recupererSemaineParNumJour(32))
		self.assertIsNone(self.cible.recupererSemaineParNumJour(-1))
	#test_recupererSemaineParNumJour_echec
	
	
	def test_ajouterCreneau_ok(self):
		"""Teste de l'ajout d'un creneau en succès"""
		self.assertIsNotNone(self.cible.ajouterCreneau(8, 2, 14))
		self.assertEqual(self.cible.nbCreneaux, 1)
	#test_ajouterCreneau_ok
	
	
	def test_ajouterCreneau_echec_numjour(self):
		"""Teste de l'ajout d'un creneau en echec à cause d'un numéro de jour"""
		with self.assertRaises(ValueError):
			self.cible.ajouterCreneau(-5, 0, 14)
		#with
	#test_ajouterCreneau_echec_numjour
	
	
	def test_ajouterCreneau_echec_interne(self):
		"""Teste de l'ajout d'un creneau à cause d'une erreur interne"""
		with self.assertRaises(Exception):
			self.cible.ajouterCreneau(32, 2, 14)
		#with
	#test_ajouterCreneau_echec_interne
	
	
	def test_supprimerCreneau_ok(self):
		"""Teste de la suppression si tout va bien"""
		c1 = self.cible.ajouterCreneau(8, 12, 14)
		c2 = self.cible.ajouterCreneau(7, 12, 14)
		self.cible.supprimerCreneau(7, c2)
		self.assertFalse(self.cible.semaines[0].jours[DIMANCHE].creneaux)
	#test_supprimerCreneau_ok
	
	
	def test_supprimerCreneau_echec_interne(self):
		"""Teste de la suppression en cas de mauvais arguments"""
		self.cible.ajouterCreneau(8, 12, 14)
		self.cible.ajouterCreneau(7, 12, 14)
		with self.assertRaises(ValueError):
			self.cible.supprimerCreneau(7, None)
		#with
	#test_supprimerCreneau_echec_interne
	
	
	def test_supprimerCreneau_echec_numjour(self):
		"""Teste de la suppression en cas de mauvais numéro de jour"""
		self.cible.ajouterCreneau(8, 12, 14)
		self.cible.ajouterCreneau(7, 12, 14)
		with self.assertRaises(ValueError):
			self.cible.supprimerCreneau(-1, 1)
		#with
	#test_supprimerCreneau_echec_numjour
	
	
	def test_jours(self):
		"""Teste la propriété get des jours d'un mois"""
		self.assertEqual(len(self.cible.jours), 31)
	
#Test_Mois

if __name__ == "__main__":
	unittest.main()
#if
