#!/usr/bin/python3
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.agenda.Dependance import *
from src.modele.agenda.FabriqueCreneau import *

class Test_Dependance(unittest.TestCase):
	"""
	Teste la class Dependance, ses spécificités uniquement.
	@author: Laurent Bardoux p1108365
	@version: 1.0
	"""
	
	def test_ajouterCreneau_resultat_est_blocage(self):
		"""Teste si l'ajout d'un creneau est bien un blocage"""
		cible = Dependance("nom", 2016)
		resultat = cible.ajouterCreneau(2016, 12, 12, 2, 8)
		self.assertEqual(resultat.typeCreneau, CreneauxPossible.BLOCAGE)
	#test_ajouterCreneau_resultat_est_blocage
	
#Test_Dependance

if __name__ == "__main__":
	unittest.main()
