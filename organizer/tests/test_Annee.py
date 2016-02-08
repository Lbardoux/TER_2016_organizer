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
	
	
	def test_recupererSemaineParNumJour(self):
		"""Teste la récupération d'une semaine"""
		cible = Annee(2002)
		self.assertTrue(cible.recupererSemaineParNumJour(1, 15) is not None)
	#test_recupererSemaineParNumJour_echec
	
	
	def test_recupererSemaineParNumJour_echec(self):
		"""Teste la récupération d'une semaine en cas de mauvais argument."""
		cible = Annee(2002)
		with self.assertRaises(Exception):
			cible.recupererSemaineParNumJour(0, 15)
		#with
		with self.assertRaises(Exception):
			cible.recupererSemaineParNumJour(13, 15)
		#with
	#test_recupererSemaineParNumJour_echec
	
	
	def test_ajouterCreneau_ok(self):
		"""Teste l'ajout en cas de succès"""
		cible = Annee(2002)
		self.assertIsNotNone(cible.ajouterCreneau(2, 15, 2, 8))
		self.assertEqual(cible.nbCreneaux, 1)
	#test_ajouterCreneau_ok
	
	
	def test_ajouterCreneau_echec_interne(self):
		"""Teste l'ajout en cas d'echec plus bas dans l'arborescence"""
		cible = Annee(2002)
		with self.assertRaises(Exception):
			cible.ajouterCreneau(8, 33, 2, 5)
		#with
	#test_ajouterCreneau_echec_interne
	
	
	def test_ajouterCreneau_echec_local(self):
		"""Teste l'ajout en cas d'echec localement"""
		cible = Annee(2002)
		with self.assertRaises(Exception):
			cible.ajouterCreneau(24, 33, 2, 5)
		#with
		with self.assertRaises(Exception):
			cible.ajouterCreneau("15", 33, 2, 5)
		#with
	#test_ajouterCreneau_echec_local
	
	
	def test_supprimerCreneau_ok(self):
		"""Teste la suppression d'un creneau qui fonctionne"""
		cible = Annee(2002)
		cible.ajouterCreneau(2, 15, 2, 8)
		cible.ajouterCreneau(2, 15, 2, 8)
		cible.supprimerCreneau(2, 15, 1)
		self.assertEqual(cible.nbCreneaux, 1)
	#test_supprimerCreneau_ok
	
	
	def test_supprimerCreneau_echec_interne(self):
		"""
		Teste la suppression d'un creneau avec de mauvais arguments
		pour l'arborescence
		"""
		cible = Annee(2002)
		with self.assertRaises(Exception):
			cible.supprimerCreneau(1, 33, 158)
		#with
	#test_supprimerCreneau_echec_interne
	
	
	def test_supprimerCreneau_echec_local(self):
		"""Teste la suppression d'un creneau avec un mauvais numéro de mois"""
		cible = Annee(2002)
		with self.assertRaises(Exception):
			cible.supprimerCreneau(15, 25, 158)
		#with
	#test_supprimerCreneau_echec_local
	
#Test_Annee


if __name__ == "__main__":
	unittest.main()
#if
