#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.agenda.FabriqueCreneau import *
from src.modele.agenda.Horaire import *

class Test_FabriqueCreneau(unittest.TestCase):
	"""
	La classe qui teste la fabrique de Creneau.
	@author : Laurent Bardoux p1108365
	"""
	
	def test_init(self):
		"""Teste l'initialisation de la Fabrique."""
		cible = FabriqueCreneau()
		self.assertTrue(type(cible._choix) is dict)
		self.assertTrue(CreneauxPossible.CM in cible._choix.keys())
		self.assertTrue(CreneauxPossible.TD in cible._choix.keys())
		self.assertTrue(CreneauxPossible.TP in cible._choix.keys())
		self.assertTrue(CreneauxPossible.EXAMEN in cible._choix.keys())
		self.assertTrue(CreneauxPossible.AUTRE in cible._choix.keys())
		self.assertTrue(CreneauxPossible.CRENEAU in cible._choix.keys())
		self.assertTrue(CreneauxPossible.SEANCE in cible._choix.keys())
	#test_init
	
	
	def test_fabrique_TD(self):
		"""Teste la fabrication d'un TD."""
		cible = FabriqueCreneau()
		horaire = Horaire(12, 18)
		self.assertTrue(cible.fabrique(CreneauxPossible.TD, 45, horaire) is not None)
		
	#test_fabrique_TD
	
	
	def test_fabrique_TP(self):
		"""Teste la fabrication d'un TP."""
		cible = FabriqueCreneau()
		cible = FabriqueCreneau()
		horaire = Horaire(12, 18)
		self.assertTrue(cible.fabrique(CreneauxPossible.TP, 45, horaire) is not None)
		
	#test_fabrique_TP
	
	
	def test_fabrique_CM(self):
		"""Teste la fabrication d'un CM."""
		cible = FabriqueCreneau()
		cible = FabriqueCreneau()
		horaire = Horaire(12, 18)
		self.assertTrue(cible.fabrique(CreneauxPossible.CM, 45, horaire) is not None)
		
	#test_fabrique_CM
	
	
	def test_fabrique_EXAMEN(self):
		"""Teste la fabrication d'un Examen."""
		cible = FabriqueCreneau()
		cible = FabriqueCreneau()
		horaire = Horaire(12, 18)
		self.assertTrue(cible.fabrique(CreneauxPossible.EXAMEN, 45, horaire) is not None)
		
	#test_fabrique_EXAMEN
	
	
	def test_fabrique_CRENEAU(self):
		"""Teste la fabrication d'un Creneau."""
		cible = FabriqueCreneau()
		cible = FabriqueCreneau()
		horaire = Horaire(12, 18)
		self.assertTrue(cible.fabrique(CreneauxPossible.CRENEAU, 45, horaire) is not None)
		
	#test_fabrique_CRENEAU
	
	
	def test_fabrique_AUTRE(self):
		"""Teste la fabrication d'un Autre."""
		cible = FabriqueCreneau()
		cible = FabriqueCreneau()
		horaire = Horaire(12, 18)
		self.assertTrue(cible.fabrique(CreneauxPossible.AUTRE, 45, horaire) is not None)
		
	#test_fabrique_Autre
	
	
	def test_fabrique_SEANCE(self):
		"""Teste la fabrication d'une Seance."""
		cible = FabriqueCreneau()
		cible = FabriqueCreneau()
		horaire = Horaire(12, 18)
		self.assertTrue(cible.fabrique(CreneauxPossible.SEANCE, 45, horaire) is not None)
		
	#test_fabrique_SEANCE
	
#Test_FabriqueCreneau

if __name__ == "__main__":
	unittest.main()
