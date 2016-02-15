#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.agenda.diff.utilitaireDiff import *
from src.modele.agenda.Creneau import *
from src.modele.agenda.Horaire import *

class Test_utilitaireDiff(unittest.TestCase):
	"""Teste le fonctionnement des méthodes utilitaires"""
	
	def test_convertitListe(self):
		"""Teste si la conversion se passe bien"""
		maliste = [Creneau(15, Horaire(12, 24)), Creneau(54, Horaire(8, 95))]
		res = convertitListe(maliste)
		#for i, elt in enumerate(res):
		#	print(str(i) + " : " + str(elt))
		
#Test_utilitaireDiff

if __name__ == "__main__":
	unittest.main()
