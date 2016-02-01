#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.formation.Ue import *
from src.modele.formation.Seance import *
from src.modele.formation.Cm import *
from src.modele.formation.Td import *
from src.modele.formation.Tp import *
from src.modele.formation.Examen import *
from src.modele.formation.Autre import *


class Test_Ue(unittest.TestCase):
	"""
	La classe de test de Ue
	"""
	def test_init_getters(self):
		"""
		Test du constructeur.
		"""
		cible = Ue("MIF11", "Reseaux", 3)
		self.assertEqual(cible.code, "MIF11")
		self.assertEqual(cible.nom, "Reseaux")
		self.assertEqual(cible.idEnseignant, 3)
		self.assertEqual(cible.nombreInscrit, 1)
		self.assertEqual(cible.nombreGroupe, 1)
		self.assertEqual(cible.nombreCm, 0)
		self.assertEqual(cible.nombreTd, 0)
		self.assertEqual(cible.nombreTp, 0)
		self.assertEqual(cible.nombreExamen, 0)
		self.assertEqual(cible.nombreAutre, 0)
		self.assertEqual(cible.nombreSeance, 0)
		self.assertEqual(cible.listeSeance, [])
		self.assertEqual(cible.listeCm, [])
		self.assertEqual(cible.listeTd, [])
		self.assertEqual(cible.listeTp, [])
		self.assertEqual(cible.listeExamen, [])
		self.assertEqual(cible.listeAutre, [])
		
		cible = Ue(" ", "", -4)
		self.assertEqual(cible.code, "Code Null")
		self.assertEqual(cible.nom, "Nom Par Defaut")
		self.assertEqual(cible.idEnseignant, 1)
		self.assertEqual(cible.nombreInscrit, 1)
		self.assertEqual(cible.nombreGroupe, 1)
		self.assertEqual(cible.nombreCm, 0)
		self.assertEqual(cible.nombreTd, 0)
		self.assertEqual(cible.nombreTp, 0)
		self.assertEqual(cible.nombreExamen, 0)
		self.assertEqual(cible.nombreAutre, 0)
		self.assertEqual(cible.nombreSeance, 0)
		self.assertEqual(cible.listeSeance, [])
		self.assertEqual(cible.listeCm, [])
		self.assertEqual(cible.listeTd, [])
		self.assertEqual(cible.listeTp, [])
		self.assertEqual(cible.listeExamen, [])
		self.assertEqual(cible.listeAutre, [])
	#fin test_init_getters
	
	
	def test_setters(self):
		"""
		Tests des mutateurs
		"""
		cible = Ue("MIF11", "Reseaux", 3)
		cible.code = " "
		self.assertEqual(cible.code, "MIF11")
		cible.code = "MIF12"
		self.assertEqual(cible.code, "MIF12")
		cible.nom = " "
		self.assertEqual(cible.nom, "Reseaux")
		cible.nom = "Compilation"
		self.assertEqual(cible.nom, "Compilation")
		cible.idEnseignant = -2
		self.assertEqual(cible.idEnseignant, 3)
		cible.idEnseignant = 14
		self.assertEqual(cible.idEnseignant, 14)
		cible.nombreInscrit = -3
		self.assertEqual(cible.nombreInscrit, 1)
		cible.nombreInscrit = 25
		self.assertEqual(cible.nombreInscrit, 25)
		cible.nombreGroupe = -1
		self.assertEqual(cible.nombreGroupe, 1)
		cible.nombreGroupe = 30
		self.assertEqual(cible.nombreGroupe, 1)
		cible.nombreGroupe = 5
		self.assertEqual(cible.nombreGroupe, 5)
	#fin test_setters
	
	def test_ajouter_supprimer(self):
		"""
		Tests sur l'ajout et suppression de la liste des Seance
		"""
		cible = Ue("MIF11", "Reseaux", 3)
		seance1 = Cm(1, 25, 8, 13, "decrit toi")
		cible.ajouterSeance(seance1)
		self.assertEqual(cible.nombreCm, 1)
		self.assertEqual(cible.listeCm,[seance1])
		self.assertEqual(cible.nombreSeance, 1)
		self.assertEqual(cible.listeSeance,[seance1])
		seance2 = Td(2, 25, 8, 13, "decrit toi")
		cible.ajouterSeance(seance2)
		self.assertEqual(cible.nombreTd, 1)
		self.assertEqual(cible.listeTd,[seance2])
		self.assertEqual(cible.nombreSeance, 2)
		self.assertEqual(cible.listeSeance,[seance1,seance2])
		seance3 = Tp(3, 25, 8, 13, "decrit toi")
		cible.ajouterSeance(seance3)
		self.assertEqual(cible.nombreTp, 1)
		self.assertEqual(cible.listeTp,[seance3])
		self.assertEqual(cible.nombreSeance, 3)
		self.assertEqual(cible.listeSeance,[seance1,seance2,seance3])
		seance4 = Examen(4, 25, 8, 13, "decrit toi")
		cible.ajouterSeance(seance4)
		self.assertEqual(cible.nombreExamen, 1)
		self.assertEqual(cible.listeExamen,[seance4])
		self.assertEqual(cible.nombreSeance, 4)
		self.assertEqual(cible.listeSeance,[seance1,seance2,seance3,seance4])
		seance5 = Autre(5, 25, 8, 13, "decrit toi")
		cible.ajouterSeance(seance5)
		self.assertEqual(cible.nombreAutre, 1)
		self.assertEqual(cible.listeAutre,[seance5])
		self.assertEqual(cible.nombreSeance, 5)
		self.assertEqual(cible.listeSeance,[seance1,seance2,seance3,seance4,seance5])
		
		cible.supprimerSeance(seance5)
		self.assertEqual(cible.nombreAutre, 0)
		self.assertEqual(cible.listeAutre,[])
		self.assertEqual(cible.nombreSeance, 4)
		self.assertEqual(cible.listeSeance,[seance1,seance2,seance3,seance4])
		cible.supprimerSeance(seance4)
		self.assertEqual(cible.nombreExamen, 0)
		self.assertEqual(cible.listeExamen,[])
		self.assertEqual(cible.nombreSeance, 3)
		self.assertEqual(cible.listeSeance,[seance1,seance2,seance3])
		cible.supprimerSeance(seance3)
		self.assertEqual(cible.nombreTp, 0)
		self.assertEqual(cible.listeTp,[])
		self.assertEqual(cible.nombreSeance, 2)
		self.assertEqual(cible.listeSeance,[seance1,seance2])
		cible.supprimerSeance(seance2)
		self.assertEqual(cible.nombreTd, 0)
		self.assertEqual(cible.listeTd,[])
		self.assertEqual(cible.nombreSeance, 1)
		self.assertEqual(cible.listeSeance,[seance1])
		cible.supprimerSeance(seance1)
		self.assertEqual(cible.nombreCm, 0)
		self.assertEqual(cible.listeCm,[])
		self.assertEqual(cible.nombreSeance, 0)
		self.assertEqual(cible.listeSeance,[])
		
		
	#fin test_ajouter_supprimer
	
#fin Test_Ue

if __name__ == "__main__":
	unittest.main()
#fin if
