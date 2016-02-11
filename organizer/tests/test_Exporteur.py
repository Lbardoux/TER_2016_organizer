#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.agenda.exportations.Exporteur import *

class Test_Exporteur(unittest.TestCase):
	"""
	Teste les fonctionnalités de Exporteur.
	@author: Laurent Bardoux p1108365
	"""
	
	def test_init(self):
		"""Teste l'initialisation"""
		nom = "trololo"
		obj = Exporteur(nom)
		self.assertEqual(obj._nomFichier, nom)
	#test_init
	
	
	def test_exporter(self):
		"""Teste la fonction d'export"""
		obj = Exporteur("rien")
		#obj.exporter("agenda")
	#test_exporter
	
#Test_Exporteur

if __name__ == "__main__":
	unittest.main()
