#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.agenda.Jour import *
from src.outils.erreurs.erreurs import *

class SimiliCreneau:
	def __init__(self, chiffre):
		self._chiffre = chiffre
		self.identifiant = chiffre

	def __le__(self, autre):
		return self._chiffre <= autre._chiffre
#SimiliCreneau


class Test_Jour(unittest.TestCase):
	"""
	Teste la classe Jour.
	A ce stade, ils doivent tous passer !
	@author : Laurent Bardoux p1108365
	@version : 2.0
	"""
	
	def test_init_1_argument(self):
		"""Teste le constructeur en utilisant la valeur par défaut."""
		cible = Jour(25)
		self.assertEqual(cible._numero, 25)
		self.assertTrue(not cible._creneaux)
		self.assertEqual(cible._nom, LUNDI)
		self.assertIsNotNone(cible._usine)
	#test_
	
	
	def test_init_2_arguments_ok(self):
		"""Teste le constructeur en précisant le second argument correctement."""
		for jour in JOURS_LEGAUX:
			cible = Jour(25, jour)
			self.assertEqual(cible._nom, jour)
		#for
	#test_
	
	
	def test_init_2_arguments_echec(self):
		"""Teste le constructeur en fournissant un second argument invalide."""
		cible = Jour(21, "invalide")
		self.assertEqual(cible._nom, LUNDI)
	#test_
	
	
	def test_get_numero(self):
		"""Teste la propriété get du _numero."""
		for i in [12, 15, 48, 689]:
			cible = Jour(i, LUNDI)
			self.assertEqual(i, cible.numero)
		#for
	#test_get_numero
	
	
	def test_set_numero_ok(self):
		"""Teste la propriété set du _numero avec de bons arguments."""
		cible = Jour(15, MARDI)
		for i in [elt+1 for elt in range(31)]:
			cible.numero = i
			self.assertEqual(cible.numero, i)
		#for
	#test_set_numero_ok
	
	
	def test_set_numero_echec(self):
		"""Teste la propriété set du _numero avec de mauvais arguments."""
		cible = Jour(15, MARDI)
		for i in [0, -1, -5, 32, 33, 589]:
			cible.numero = i
			self.assertEqual(cible.numero, 15)
		#for
	#test_set_numero_echec
	
	
	def test_get_nom(self):
		"""Teste la propriété get du _nom."""
		for jour in JOURS_LEGAUX:
			cible = Jour(25, jour)
			self.assertEqual(cible.nom, jour)
		#for
	#test_get_nom
	
	
	def test_get_creneaux(self):
		"""Teste la propriété get du _creneaux."""
		cible = Jour(31, LUNDI)
		self.assertTrue(type(cible.creneaux) is list)
	#test_get_creneaux
	
	
	def test_inserer_1_element(self):
		"""Teste l'insertion d'un seul "creneau"."""
		cible = Jour(18)
		valeur = 1254
		oracle = [valeur]
		cible.insererCreneau(valeur)
		
		self.assertFalse(not cible.creneaux)
		self.assertEqual(cible.creneaux, oracle)
	#test_inserer_1_element
	
	
	def test_inserer_plusieurs_element(self):
		"""Teste l'insertion de plusieurs "creneaux" afin d'en teter l'ordonnancement."""
		cible = Jour(18)
		oracle = [-254, 18, 56, 56, 256, 7852]
		for i in [18, 256, 56, 7852, -254, 56]:
			cible.insererCreneau(i)
		#for
		self.assertEqual(cible.creneaux, oracle)
	#test_inserer_1_element
	
	
	def test_ajouterCreneau_mauvais_horaire(self):
		"""Teste si un mauvais horaire renvoi bien une exception."""
		d = ["pas int", 14, 18]
		f = [25, "pas int", 14]
		i = 0
		cible = Jour(15, LUNDI)
		while i < len(f):
			with self.assertRaises(Exception):
				cible.ajouterCreneau(d[i], f[i])
			#with
			i += 1
		#while
	#test_ajouterCreneau_mauvais_horaire
	
	
	def test_ajouterCreneau_mauvais_creneau(self):
		"""Teste si un enum erroné renvoi bien une exception."""
		cible = Jour(15, LUNDI)
		with self.assertRaises(Exception):
			cible.ajouterCreneau(15, 18, "rate")
		#with
	#test_ajouterCreneau_mauvais_horaire
	
	
	def test_ajouterCreneau_ok(self):
		"""Teste un ajout qui se passe bien"""
		cible = Jour(15, LUNDI)
		self.assertIsNotNone(cible.ajouterCreneau(1, 13))
		self.assertTrue(cible.creneaux)
	#test_ajouterCreneau_mauvais_horaire
	
	
	def test_supprimerCreneau_ok(self):
		"""Teste une suppression qui se passe bien."""
		cible = Jour(15)
		oracle = [1, 18]
		for i in [1, 15, 18]:
			simili = SimiliCreneau(i)
			cible.creneaux.append(simili)
		#for
		cible.supprimerCreneau(15)
		self.assertEqual(len(cible.creneaux), 2)
		for i, elt in enumerate(cible.creneaux):
			self.assertEqual(oracle[i], elt.identifiant)
		#for
	#test_supprimerCreneau_ok
	
	
	def test_supprimerCreneau_echec(self):
		"""Teste une suppression qui echoue."""
		cible = Jour(15)
		for i in [1, 15, 18]:
			simili = SimiliCreneau(i)
			cible.creneaux.append(simili)
		#for
		with self.assertRaises(Exception):
			cible.supprimerCreneau(25)
		#with
	#test_supprimerCreneau_echec
	
#Test_Jour

if __name__ == "__main__":
	unittest.main()
#if
