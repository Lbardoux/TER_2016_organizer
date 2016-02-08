#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.agenda.Creneau import *
from src.modele.agenda.Horaire import *

class Test_Agenda(unittest.TestCase):
	"""
	La classe qui va tester les fonctionnalités de la classe Creneau
	@author : Laurent Bardoux p1108365
	"""
	
	def test_init_ok(self):
		"""Teste si l'initialisation marche si on ne fait pas d'erreur"""
		cible = Creneau(18, Horaire(1, 8))
		self.assertEqual(cible._identifiant, 18)
		self.assertTrue(type(cible._informations) is dict)
		self.assertTrue(cible._horaire is not None)
	#test_init_ok
	
	
	def test_init_echec(self):
		"""Teste si l'initialisation ne marche pas si on ne fait une erreur"""
		with self.assertRaises(AssertionError):
			cible = Creneau(0, Horaire(1, 8))
		#with
		with self.assertRaises(AssertionError):
			cible = Creneau(-5, Horaire(1, 8))
		#with
		with self.assertRaises(AssertionError):
			cible = Creneau("lol", Horaire(1, 8))
		#with
	#test_init_echec
	
	
	def test_inferieur_ou_egal(self):
		"""Test si <= fonctionne bien entre Creneau"""
		c1 = Creneau(45, Horaire(15, 18))
		c2 = Creneau(45, Horaire(15, 24))
		c3 = Creneau(45, Horaire(18, 24))
		
		self.assertTrue(c1 <= c2)
		self.assertTrue(c1 <= c3)
		self.assertFalse(c3 <= c1)
	#test_inferieur_ou_egal
	
	
	def test_get_identifiant(self):
		"""Teste si la propriété get de _identifiant marche bien"""
		c1 = Creneau(45, Horaire(15, 18))
		self.assertEqual(c1._identifiant, c1.identifiant)
	#test_get_identifiant
	
	
	def test_get_horaire(self):
		"""Teste si la propriété get de _horaire fonctionne."""
		h =  Horaire(15, 18)
		c1 = Creneau(45, h)
		self.assertTrue(c1.horaire is h)
	#test_get_horaire
	
	
	def test_set_horaire(self):
		"""Teste si la propriété set de _horaire marche."""
		h =  Horaire(15, 18)
		c1 = Creneau(45, Horaire(18, 25))
		c1.horaire = h
		self.assertTrue(c1.horaire is h)
	#test_set_horaire
	
	
	def test_set_identifiant(self):
		"""Teste si la propriété set de _identifiant marche."""
		h =  Horaire(15, 18)
		c1 = Creneau(45, Horaire(18, 25))
		c1.identifiant = 64
		self.assertEqual(64, c1.identifiant)
	#test_set_horaire
	
	
	def test_get_informations(self):
		"""Teste si la propriété get de _informations marche"""
		c1 = Creneau(45, Horaire(18, 25))
		self.assertTrue(type(c1.informations) is dict)
	#test_get_informations
	
	
	def test_existe(self):
		"""Teste si la fonction existe trouve bien quand la clef existe"""
		c1 = Creneau(45, Horaire(18, 25))
		c1.ajouterInformation("TEST", "bonjour les amis")
		self.assertTrue(c1.existe("TEST"))
	#test_existe
	
	
	def test_existe_echec(self):
		"""Teste si la fonction existe ne trouve rien si ça n'existe pas"""
		c1 = Creneau(45, Horaire(18, 25))
		c1.ajouterInformation("TEST", "bonjour les amis")
		self.assertFalse(c1.existe("HAHA"))
	#test_existe_echec
	
	
	def test_ajouterInformation(self):
		"""Teste si l'ajout se passe bien lorsque la clef n'existe pas déjà"""
		c1 = Creneau(45, Horaire(18, 25))
		c1.ajouterInformation("TEST", "bonjour les amis")
		self.assertTrue(c1.existe("TEST"))
		self.assertEqual(c1.informations["TEST"], "bonjour les amis")
	#test_ajouterInformation
	
	
	def test_ajouterInformation_echec(self):
		"""Teste si l'ajout se passe mal lorsque la clef existe  déjà"""
		c1 = Creneau(45, Horaire(18, 25))
		c1.ajouterInformation("TEST", "bonjour les amis")
		c1.ajouterInformation("TEST", "a plus les amis")
		self.assertEqual(c1.informations["TEST"], "bonjour les amis")
	#test_ajouterInformation_echec
	
	
	def test_enleverInformation(self):
		"""Teste le retrait d'une information si elle existe"""
		c1 = Creneau(45, Horaire(18, 25))
		c1.ajouterInformation("TEST", "bonjour les amis")
		c1.ajouterInformation("ENCORE_TEST", "a plus les amis")
		c1.enleverInformation("ENCORE_TEST")
		self.assertFalse(c1.existe("ENCORE_TEST"))
	#test_enleverInformation
	
#fin Test_Creneau

if __name__ == "__main__":
	unittest.main()
#if
