#!/usr/bin/python3
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.outils.observateur.Observable import *
from src.outils.observateur.Observeur import Observeur

class MonObserveur(Observeur):
	def __init__(self):
		super(MonObserveur, self).__init__()
		self.i = 2

	def miseAJour(self, observable, *arguments):
		self.i = 8
	
#MonObserveur

class MonObservable(Observable):
	def __init__(self):
		super(MonObservable, self).__init__()
	
	@notifier
	def jouer(self):
		pass
	
#MonObservable

class Test_Observable(unittest.TestCase):
	"""
	Teste si Observable marche bien comme on l'attend
	@author: Laurent Bardoux p1108365
	"""
	
	def setUp(self):
		"""A faire avant chaque test"""
		self.cible = Observable()
	#setUp
	
	
	def test_init_observeurs(self):
		"""Teste si l'initialisation fait le minimum vital"""
		self.cible = Observable()
		self.assertTrue(type(self.cible._observeurs) is list)
	#test_init_observeurs
	
	
	def test_ajout_observeur_ok(self):
		"""Teste si l'ajout se passe bien lorsque l'on est respectueux des règles"""
		self.cible.ajouterObserveur(Observeur())
		self.assertEqual(1, len(self.cible._observeurs))
	#test_ajout_observeur_ok
	
	
	def test_ajout_observeur_doublon(self):
		"""Teste si l'ajout échoue lorsque l'on essai d'ajouter un doublon"""
		o = Observeur()
		self.cible.ajouterObserveur(o)
		with self.assertRaises(ReferenceError):
			self.cible.ajouterObserveur(o)
		#with
	#test_ajout_observeur_ok
	
	
	def test_retrait_observeur_ok(self):
		"""Teste si le retrait d'un Observeur marche bien"""
		o = Observeur()
		self.cible.ajouterObserveur(o)
		self.cible.enleverObserveur(o)
		self.assertEqual(0, len(self.cible._observeurs))
	#test_retrait_observeur_ok
	
	
	def test_retrait_observeur_pas_dedans(self):
		"""Teste le retrait d'un observeur qui n'est pas liste"""
		o = Observeur()
		pasDedans = Observeur()
		self.cible.ajouterObserveur(o)
		with self.assertRaises(ValueError):
			self.cible.enleverObserveur(pasDedans)
		#with
	#test_retrait_observeur_pas_dedans
	
	
	def test_retrait_observeur_vide(self):
		"""Teste le retrait d'un observeur quand le liste est vide"""
		o = Observeur()
		pasDedans = Observeur()
		with self.assertRaises(ValueError):
			self.cible.enleverObserveur(pasDedans)
		#with
	#test_retrait_observeur_vide
	
	
	def test_notifications(self):
		"""Teste si les notifications fonctionnent"""
		a, b, c = MonObserveur(), MonObserveur(), MonObserveur()
		self.cible.ajouterObserveur(a)
		self.cible.ajouterObserveur(b)
		self.cible.ajouterObserveur(c)
		self.cible.notifierObserveurs()
		
		self.assertEqual(a.i, 8)
		self.assertEqual(b.i, 8)
		self.assertEqual(c.i, 8)
	#test_notifications
	
	
	def test_decorator(self):
		"""Teste si le decorator fonctionne bien"""
		a, b, c = MonObserveur(), MonObserveur(), MonObserveur()
		cible = MonObservable()
		cible.ajouterObserveur(a)
		cible.ajouterObserveur(b)
		cible.ajouterObserveur(c)
		cible.jouer()
		
		self.assertEqual(a.i, 8)
		self.assertEqual(b.i, 8)
		self.assertEqual(c.i, 8)
	#test_decorator
	
#Test_Observable

if __name__ == "__main__":
	unittest.main()
#if
