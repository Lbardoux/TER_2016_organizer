#!/usr/bin/python3
# -*-coding:utf-8 -*

from agenda.exportations.FabriqueExporteur import *
from agenda.importations.AgendaDepuisIcs import importer
from datetime import datetime
import agenda.Agenda

class ModeleAgenda(object):
	"""
	La classe qui permet de manipuler les L{Agenda}s et toutes les fonctionnalités
	liées.
	C'est elle qui va contenir tous les éléments que la Vue va pouvoir lire.
	@ivar _agendas: un dictionnaire mappant des L{Agenda}s par leurs noms
	@ivar _fabrique: La fabrique d'exporteurs pour les différentes exportations.
	@author: Laurent Bardoux p1108365
	@version: 1.0
	"""
	
	def __init__(self):
		"""
		Prépare l'API à etre utiliser par l'application.
		Elle va initialiser tout les composants qui seront alors
		utilisable.
		@param self: L'argument implicite.
		"""
		self._agendas = dict()
		self._fabrique = FabriqueExporteur()
	#__init__
	
	
	def chargerAgenda(self, nomFichier):
		"""
		Cette fonction permet de charger un Agenda dans le dictionnaire.
		nomFichier sera traité pour nommer l'Agenda.
		@param self: L'argument implicite.
		@type nomFichier: str
		@param nomFichier: le nom du fichier dont on doit lire le contenu pour créer un Agenda
		@raise IOError: Si un problème concernant la lecture/ouverture du fichier arrive.
		@rtype: L{Agenda}
		@return: L'agenda qui a été chargé, mappé par son nom (accessible par agenda.nom)
		"""
		#gaffe pour le coté windows, à vérifier
		nom = nomFichier.split('/')[-1]
		anneeActuelle = datetime.now().year
		agenda = Agenda.Agenda(nom, anneeActuelle)
		importer(agenda, nomFichier)
		# cas ou il y est déjà à gérer.
		self._agendas[nom] = agenda
		return agenda
	#chargerAgenda
	
	
	@property
	def agendas(self):
		"""Un accesseur pour les agendas disponibles"""
		return self._agendas
	#agendas
	
#ModeleAgenda
