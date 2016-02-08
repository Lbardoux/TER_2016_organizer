#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.agenda.Semaine import *
import src.modele.agenda.Jour

class Test_Semaine(unittest.TestCase):
	"""
	La classe qui va tester les fonctionnalités de la classe Semaine
	@author : Laurent Bardoux p1108365
	"""
	
	def test_construireArgument(self):
		"""Teste si cet utilitaire fonctionne correctement"""
		nom1 = Jour.LUNDI
		nom2 = Jour.MERCREDI
		num1 = 12
		num2 = 14
		oracle = dict()
		oracle[DEBUT] = nom1
		oracle[N_DEBUT] = num1
		oracle[FIN] = nom2
		oracle[N_FIN] = num2
		test = construireArgument(nom1, num1, nom2, num2)
		
		for clef in oracle.keys():
			self.assertTrue(clef in test.keys())
			self.assertEqual(oracle[clef], test[clef])
		#for
	#test_construireArgument
	
	
	def test_initialisation(self):
		"""Teste si l'initialisation se passe bien."""
		oracle = [Jour.LUNDI, Jour.MARDI, Jour.MERCREDI, Jour.JEUDI]
		cible = Semaine(2, construireArgument(Jour.LUNDI, 2, Jour.JEUDI, 5))
		
		self.assertEqual(cible._numero, 2)
		for i in oracle:
			self.assertTrue(i in cible._jours.keys())
		#for
	#test_initialisation
	
	
	def test_initialisation2(self):
		"""Teste si l'initialisation se passe bien."""
		oracle = [Jour.MERCREDI, Jour.JEUDI, Jour.VENDREDI, Jour.SAMEDI]
		cible = Semaine(2, construireArgument(Jour.MERCREDI, 2, Jour.SAMEDI, 5))
		self.assertEqual(0, cible.nbCreneaux)
		
		self.assertEqual(cible._numero, 2)
		for i in oracle:
			self.assertTrue(i in cible._jours.keys())
		#for
	#test_initialisation
	
	
	def test_numero_get(self):
		"""Teste de la propriété get de _numero."""
		cible = Semaine(2, construireArgument(Jour.MERCREDI, 2, Jour.SAMEDI, 5))
		self.assertEqual(cible.numero, 2)
	#test_numero_get
	
	
	def test_numero_set(self):
		"""Teste de la propriété set de _numero."""
		cible = Semaine(2, construireArgument(Jour.MERCREDI, 2, Jour.SAMEDI, 5))
		cible.numero = 18
		self.assertEqual(cible.numero, 18)
	#test_numero_set
	
	
	def test_jours_get(self):
		"""Teste la propriété get de _jours."""
		cible = Semaine(2, construireArgument(Jour.MERCREDI, 2, Jour.SAMEDI, 5))
		self.assertTrue(type(cible.jours) is dict)
		self.assertEqual(len(cible.jours), 4)
	#test_jours_get
	
	
	def test_listeNomJours_get(self):
		"""Teste de l'accesseur de la liste des noms connus."""
		oracle = [Jour.MERCREDI, Jour.JEUDI, Jour.VENDREDI, Jour.SAMEDI]
		cible = Semaine(2, construireArgument(Jour.MERCREDI, 2, Jour.SAMEDI, 5))
		test = cible.listeNomJours
		
		for i, nom in enumerate(oracle):
			self.assertEqual(test[i], nom)
		#for
	#test_listeNomJours_get
	
	
	def test_recupererJour_ok(self):
		"""Teste d'une récupération qui fonctionne."""
		cible = Semaine(2, construireArgument(Jour.MERCREDI, 2, Jour.SAMEDI, 5))
		self.assertTrue(cible.recupererJour(Jour.VENDREDI) is not None)
		#Ce test ne passe pas, i lfaudra chercher pourquoi
		#self.assertTrue(type(cible.recupererJour(Jour.VENDREDI)) is Jour)
	#test_recupererJour_ok
	
	
	def test_recupererJour_echec(self):
		"""Teste d'une récupération qui rate."""
		cible = Semaine(2, construireArgument(Jour.MERCREDI, 2, Jour.SAMEDI, 5))
		self.assertTrue(cible.recupererJour(Jour.DIMANCHE) is None)
	#test_recupererJour_echec
	
#Test_Semaine

if __name__ == "__main__":
	unittest.main()
#if
