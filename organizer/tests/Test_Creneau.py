#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.agenda.Creneau import *

class Test_Agenda(unittest.TestCase):
	"""
	La classe qui va tester les fonctionnalités de la classe Creneau
	@author : Laurent Bardoux p1108365
	"""

	def test_init(self):
		"""
		Teste l'initialisation d'un Creneau
		"""
		cible = Creneau(18, None)
		self.assertEqual(18, cible.identifiant)
		self.assertTrue(cible.horaire is None)
		self.assertTrue(cible.informations)
	#fin test_init


	def test_identifiant(self):
		"""
		test des propriétés sur identifiants
		"""
		cible = Creneau(18, None)
		self.assertEqual(18, cible.identifiant)
		cible.identifiant = 25
		self.assertEqual(18, cible.identifiant)
	#fin test_identifiant


	def test_horaire(self):
		"""
		tests des propriétés sur horaire.
		"""
		cible = Creneau(48, "bullshit")
		self.assertEqual("bullshit", self.horaire)
		cible.horaire = None
		self.assertEqual("bullshit", self.horaire)
		self.horaire = "trop tard"
		self.assertEqual("trop tard", self.horaire)
	#fin test_horaire
	
	
	def test_informations(self):
		"""
		Tests sur les informations via les propriétés
		"""
		cible = Creneau(48, "bullshit")
		self.assertTrue(cible.informations)
		self.assertTrue(type(cible.informations) is dict)
		cible.informations["lol"] = None
		cible.informations = "lol"
		self.assertTrue(type(cible.informations) is dict)
	#fin test_informations
	
	
	def test_ajout(self):
		"""
		Test les ajouts et la fonction d'existence
		"""
		cible = Creneau(45, "horaire temporaire")
		cible.ajouterInformation("date", None)
		self.assertTrue(not cible.informations)
		self.assertTrue("date" in cible.informations.keys())
		cible.ajouterInformation(None, None)
		self.assertEqual(1, len(cible.informations))
	#fin test_ajout
	
#fin Test_Creneau

if __name__ == "__main__":
	unittest.main()
#if
