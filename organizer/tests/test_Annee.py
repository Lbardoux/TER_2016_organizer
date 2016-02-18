#!/usr/bin/python3
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.agenda.Annee import *
from src.modele.agenda.Creneau import *
from src.modele.agenda.Horaire import *
from src.modele.agenda.Jour import *

class Test_Annee(unittest.TestCase):
	"""
	La classe qui va tester Annee.
	@author : Laurent Bardoux p1108365.
	"""
	
	def setUp(self):
		"""A faire avant chaque test"""
		self.cible = Annee(2015)
	#setUp
	
	
	def test_init_an(self):
		"""Teste l'initialisation d'une Annee sur le champs an."""
		self.assertEqual(self.cible._an, 2015)
	#test_init_an
	
	
	def test_init_nbCreneau(self):
		"""Teste l'initialisation d'une Annee sur le champs an."""
		self.assertEqual(self.cible._nbCreneaux, 0)
	#test_init_nbCreneau
	
	
	def test_init_usine(self):
		"""Certifie qu'une usine ou assimilé est mise à l'instanciation"""
		self.assertEqual(self.cible._generateur.suivant(), 1)
	#test_init_usine
	
	
	def test_init_nbMois(self):
		"""Teste l'initialisation d'une Annee sur les mois"""
		self.assertEqual(len(self.cible._mois), 12)
	#test_init_nbMois
	
	
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
	
	
	def test_get_mois(self):
		"""Teste la propriété get de _mois"""
		self.assertEqual(len(self.cible.mois), 12)
	#test_get_mois
	
	
	def test_recupererSemaineParNumJour(self):
		"""Teste la récupération d'une semaine"""
		cible = Annee(2002)
		self.assertTrue(cible.recupererSemaineParNumJour(1, 15) is not None)
	#test_recupererSemaineParNumJour_echec
	
	
	def test_recupererSemaineParNumJour_echec_num_mois(self):
		"""Teste la récupération d'une semaine en cas de mauvais argument sur le numéro de mois."""
		with self.assertRaises(ValueError):
			self.cible.recupererSemaineParNumJour(0, 15)
		#with
	#test_recupererSemaineParNumJour_echec_num_mois
	
	
	def test_recupererSemaineParNumJour_echec_num_jour(self):
		"""Teste la récupération d'une semaine en cas de mauvais argument sur le numéro de jour."""
		with self.assertRaises(ValueError):
			self.cible.recupererSemaineParNumJour(0, -1)
		#with
	#test_recupererSemaineParNumJour_echec_num_mois
	
	
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
		c1 = cible.ajouterCreneau(2, 15, 2, 8)
		c2 = cible.ajouterCreneau(2, 15, 2, 8)
		cible.supprimerCreneau(2, 15, c1)
		self.assertEqual(cible.nbCreneaux, 1)
	#test_supprimerCreneau_ok
	
	
	def test_supprimerCreneau_echec_interne(self):
		"""
		Teste la suppression d'un creneau avec de mauvais arguments
		pour l'arborescence
		"""
		cible = Annee(2002)
		with self.assertRaises(ValueError):
			cible.supprimerCreneau(1, 33, 158)
		#with
	#test_supprimerCreneau_echec_interne
	
	
	def test_supprimerCreneau_echec_local(self):
		"""Teste la suppression d'un creneau avec un mauvais numéro de mois"""
		cible = Annee(2002)
		with self.assertRaises(ValueError):
			cible.supprimerCreneau(15, 25, 158)
		#with
	#test_supprimerCreneau_echec_local
	
	
	def test_inserer_creneau_mauvais_num_mois(self):
		"""Teste si l'insertion echoue si le numéro de mois est erroné"""
		with self.assertRaises(ValueError):
			self.cible.insererCreneau("whatever", -1, 15)
		#with
	#test_inserer_creneau_mauvais_num_mois
	
	
	def test_inserer_creneau_mauvais_num_jour(self):
		"""Teste si l'insertion echoue si le numéro de jour est erroné"""
		with self.assertRaises(ValueError):
			self.cible.insererCreneau("whatever", 10, 35)
		#with
	#test_inserer_creneau_mauvais_num_jour
	
	
	def test_inserer_creneau_reussi(self):
		"""Teste si l'insertion echoue si le numéro de mois est erroné"""
		self.cible.insererCreneau(Creneau(25, Horaire.Horaire(2, 4)), 10, 15)
		self.assertEqual(self.cible.nbCreneaux, 1)
	#test_inserer_creneau_mauvais_num_mois
	
#Test_Annee


if __name__ == "__main__":
	unittest.main()
#if
