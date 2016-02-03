#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.agenda.Jour import *

class Test_Jour(unittest.TestCase):
	"""
	La classe qui va tester les fonctionnalités de la classe Jour
	@author : Laurent Bardoux p1108365
	"""
	
	def test_instanciation_defaut(self):
		"""Teste la méthode __init__ avec un argument par défaut."""
		numJour = 25
		cible = Jour(numJour)
		
		self.assertEqual(cible._numero, numJour)
		self.assertEqual(cible._nom, "lundi")
		self.assertEqual(len(cible._creneaux), 0)
	#test_instanciation
	
	
	def test_instanciation_nom(self):
		"""Teste la fonction __init__ en fournissant tous les arguments."""
		numJour = 25
		nomJour = MARDI
		cible = Jour(numJour, nomJour)
		
		self.assertEqual(cible._numero, numJour)
		self.assertEqual(cible._nom, nomJour)
		self.assertEqual(len(cible._creneaux), 0)
	#test_instanciation_nom
	
	
	def test_instanciation_erreur_nom(self):
		"""Teste la fonction __init__ en se plantant dans le nom."""
		cible = Jour(24, "Mardis")
		self.assertEqual(cible._nom, LUNDI)
	#test_instanciation_erreur_nom
	
	
	def test_numero_get(self):
		"""Teste la propriété get de _numero."""
		numJour = 25
		cible = Jour(numJour)
		
		self.assertEqual(cible.numero, numJour)
	#test_numero_get
	
	
	def test_numero_set_correct(self):
		"""Teste la propriété set du _numero."""
		numJour = 25
		cible = Jour(numJour)
		
		cible.numero = 18
		self.assertEqual(cible.numero, 18)
	#test_numero_set_correct
	
	
	def test_numero_set_incorrect(self):
		"""Teste la propriété set du _numero."""
		numJour = 25
		cible = Jour(numJour)
		listeChoix = [0, -1, 32, 45, -5]
		
		for i in listeChoix:
			cible.numero = i
			self.assertEqual(cible.numero, numJour)
		#for
	#test_numero_set_incorrect
	
	
	def test_nom_get(self):
		"""Teste la propriété get du _nom."""
		cible = Jour(1)
		self.assertEqual(cible.nom, "lundi")
	#test_nom_get
	
	
	def test_nom_set(self):
		"""Teste la propriété get du _nom."""
		cible = Jour(1)
		self.assertEqual(cible.nom, "lundi")
	#test_nom_get
	
	
	def test_nom_set(self):
		"""Teste la propriété set du _nom."""
		cible = Jour(1)
		cible.nom = "jeudi"
		self.assertEqual(cible.nom, "jeudi")
	#test_nom_set
	
	
	def test_creneaux_get(self):
		"""Teste la propriété get du _creneaux."""
		cible = Jour(28)
		self.assertTrue(type(cible.creneaux) is list)
	#test_creneaux_get
	
	
	def test_ajouterCreneau(self):
		"""Teste si l'ajout insère correctement les éléments."""
		oracle = [15, 41, 41, 52, 332]
		cible = Jour(14)
		cible.ajouterCreneau(52)
		cible.ajouterCreneau(15)
		cible.ajouterCreneau(41)
		cible.ajouterCreneau(332)
		cible.ajouterCreneau(41)
		
		for i, element in enumerate(oracle):
			self.assertEqual(element, cible.creneaux[i])
		#for
	#test_ajouterCreneau
	
#Test_Jour

if __name__ == "__main__":
	unittest.main()
#if