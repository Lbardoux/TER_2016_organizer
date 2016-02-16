#!/usr/bin/python
# -*-coding:utf-8 -*
from Salle import Salle
from Formation import Formation
from Enseignant import Enseignant
from listeSalle import ListeSalle
from listeFormation import ListeFormation
from listeEnseignant import ListeEnseignant

class Base(object):
	"""
	"""
	def __init__(self):
		"""
		"""
		self._listeSalle = ListeSalle()
		self._listeFormation = ListeFormation()
		self._listeEnseignant = ListeEnseignant()
		self._configuration()
	#fin __init__
	
	def _configuration(self):
		"""
		"""
		self._listeEnseignant.ajouterEnseignant(Enseignant(1,"GUERIN LASSOUS", "Isabelle"))
		self._listeEnseignant.ajouterEnseignant(Enseignant(2,"GUILLOU", "Erwan"))
		self._listeEnseignant.ajouterEnseignant(Enseignant(3,"LEFEVRE", "Marie"))
		self._listeEnseignant.ajouterEnseignant(Enseignant(4,"BRANDEL", "Sylvain"))
		self._listeEnseignant.ajouterEnseignant(Enseignant(5,"TABARD", "Aurelien"))
		self._listeEnseignant.ajouterEnseignant(Enseignant(6,"COQUERY", "Emmanuel"))
		self._listeEnseignant.ajouterEnseignant(Enseignant(7,"GAVIN", "Gerald"))
		self._listeEnseignant.ajouterEnseignant(Enseignant(8,"JEAN-DAUBIAS", "Stephanie"))
		self._listeEnseignant.ajouterEnseignant(Enseignant(9,"CANIOU", "Yves"))
		self._listeEnseignant.ajouterEnseignant(Enseignant(10,"CHAINE", "Raphaelle"))
		self._listeEnseignant.ajouterEnseignant(Enseignant(11,"HASSAS", "Salima"))
		self._listeEnseignant.ajouterEnseignant(Enseignant(12,"AUSSEM", "Alexandre"))
		
		self._listeFormation.ajouterFormation(Formation(1, 4, "Informatique", 8))
		self._listeFormation.ajouterFormation(Formation(2, 5, "TI", 6))
		self._listeFormation.ajouterFormation(Formation(3, 5, "DS", 12))
		self._listeFormation.ajouterFormation(Formation(4, 5, "SRIV", 9))
		self._listeFormation.ajouterFormation(Formation(5, 5, "IA", 11))
		self._listeFormation.ajouterFormation(Formation(6, 5, "IMAGE", 10))
		
		self._listeSalle.ajouterSalle(Salle(1, "Nautibus C1", 70))
		self._listeSalle.ajouterSalle(Salle(2, "Nautibus C2", 70))
		self._listeSalle.ajouterSalle(Salle(3, "Nautibus C3", 70))
		self._listeSalle.ajouterSalle(Salle(4, "Nautibus C4", 70))
		self._listeSalle.ajouterSalle(Salle(5, "Nautibus C5", 70))
		self._listeSalle.ajouterSalle(Salle(6, "Nautibus TD1", 35))
		self._listeSalle.ajouterSalle(Salle(7, "Nautibus TD2", 35))
		self._listeSalle.ajouterSalle(Salle(8, "Nautibus TD3", 35))
		self._listeSalle.ajouterSalle(Salle(9, "Nautibus TD4", 35))
		self._listeSalle.ajouterSalle(Salle(10, "Nautibus TD5", 35))
		self._listeSalle.ajouterSalle(Salle(11, "Nautibus TP1", 20))
		self._listeSalle.ajouterSalle(Salle(12, "Nautibus TP2", 20))
		self._listeSalle.ajouterSalle(Salle(13, "Nautibus TP3", 20))
		self._listeSalle.ajouterSalle(Salle(14, "Nautibus TP4", 20))
		self._listeSalle.ajouterSalle(Salle(15, "Nautibus TP5", 20))
	#fin _configuration
	
	@property
	def salles(self):
		"""
		"""
		return self._listeSalle
	#fin salles
	
	@property
	def formations(self):
		"""
		"""
		return self._listeFormation
	#fin formations
	
	@property
	def enseignants(self):
		"""
		"""
		return self._listeEnseignant
	#fin enseignants
	
#fin Base
