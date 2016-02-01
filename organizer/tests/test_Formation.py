#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.formation.Formation import *
from src.modele.formation.Ue import *

class Test_Formation(unittest.TestCase):
	"""
	La classe de test de Formation
	"""
	def test_init_getters(self):
		"""
		Test du constructeur.
		"""
		cible = Formation(2,4,"Informatique",5)
		self.assertEqual(cible.idFormation, 2)
		self.assertEqual(cible.niveau, 4)
		self.assertEqual(cible.nom, "Informatique")
		self.assertEqual(cible.idEnseignant, 5)
		self.assertEqual(cible.listeUe, [])
		self.assertEqual(cible.nombreUe, 0)
		self.assertEqual(cible.chaine,"Master"+" "+"1"+" "+"Informatique")
		cible = Formation(-2,-4,"",-6)
		self.assertEqual(cible.idFormation, 1)
		self.assertEqual(cible.niveau, 0)
		self.assertEqual(cible.nom, "Nom Par Defaut")
		self.assertEqual(cible.idEnseignant, 1)
		self.assertEqual(cible.listeUe, [])
		self.assertEqual(cible.nombreUe, 0)
		self.assertEqual(cible.chaine,""+" "+""+" "+"Nom Par Defaut")
	#fin test_init_getters_chaine
	
	
	def test_setters(self):
		"""
		Tests des mutateurs
		"""
		cible = Formation(2,4,"Informatique",5)
		cible.idFormation = -1
		self.assertEqual(cible.idFormation, 2)
		cible.idFormation = 3
		self.assertEqual(cible.idFormation, 3)
		cible.niveau = -5
		self.assertEqual(cible.niveau, 4)
		cible.niveau = 3
		self.assertEqual(cible.niveau, 3)
		cible.nom = "  "
		self.assertEqual(cible.nom, "Informatique")
		cible.nom = "coco"
		self.assertEqual(cible.nom, "coco")
		cible.idEnseignant = -2
		self.assertEqual(cible.idEnseignant, 5)
		cible.idEnseignant = 14
		self.assertEqual(cible.idEnseignant, 14)
	#fin test_setters
	
	def test_ajouter_supprimer(self):
		"""
		Tests sur l'ajout et suppression de la liste des Seance
		"""
		cible = Formation(2,4,"Informatique",5)
		ue1 = Ue("MIF11", "Reseaux", 3)
		cible.ajouterUe(ue1)
		self.assertEqual(cible.listeUe, [ue1])
		self.assertEqual(cible.nombreUe, 1)
		ue2 = Ue("MIF12", "Compilation", 7)
		cible.ajouterUe(ue2)
		self.assertEqual(cible.listeUe, [ue1,ue2])
		self.assertEqual(cible.nombreUe, 2)
		
		cible.supprimerUe(ue1)
		self.assertEqual(cible.listeUe, [ue2])
		self.assertEqual(cible.nombreUe, 1)
		cible.supprimerUe(ue2)
		self.assertEqual(cible.listeUe, [])
		self.assertEqual(cible.nombreUe, 0)
	#fin test_ajouter_supprimer
	
#fin Test_Formation

if __name__ == "__main__":
	unittest.main()
#fin if
