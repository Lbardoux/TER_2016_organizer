#!/usr/bin/python3
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.outils.observateur.Observeur import *


class Bidouille(Observeur):
	def __init__(self):
		super(Bidouille, self).__init__()
	
	def miseAJour(self, observable, *arguments):
		return True
	
#Bidouille


class Test_Observeur(unittest.TestCase):
	"""
	Teste si Observeur marche bien comme on l'attend
	@author: Laurent Bardoux p1108365
	"""
	
	def test_derivation_bidouille_par_Observeur(self):
		"""Teste si la dérivation marche bien"""
		cible = Bidouille()
		self.assertTrue(cible.miseAJour("rien"))
	#test_derivation_bidouille_par_Observeur
	
#Test_Observeur



if __name__ == "__main__":
	unittest.main()
#if
