#!/usr/bin/python3
# -*-coding:utf-8 -*

# attention, les imports se font depuis le répertoire du script !
import sys, os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../../src")

from modele.agenda.Agenda import *

class IntegrationAgenda:
	"""
	Voici un test d'intégration, qui vérifie que un Agenda fonctionne
	bien avec tous les composants associés.
	
	En cas de succès, il sera meme possible de récupérer l'Agenda créé !
	@ivar resultat : Là ou est stocké l'Agenda construit par ce test.
	
	@author : Laurent Bardoux p1108365
	"""
	
	def __init__(self):
		"""Génère un Agenda pour l'année 2016"""
		self.resultat = Agenda("essai.ics", 2016)

		# Génération d'une journée remplie le 05/01/2016
		for i in [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45]:
			self.resultat.ajouterCreneau(2016, 1, 5, i, i+4)
		#for
	#__init__
	
	def choperDonnees(self):
		"""Renvoi le dictionnaire de jour pour tester"""
		return self.resultat.recupererSemaineParNumJour(2016, 1, 5)
	#choperDonnees
	
#IntegrationAgenda

if __name__ == "__main__":
	test = IntegrationAgenda()
#if
