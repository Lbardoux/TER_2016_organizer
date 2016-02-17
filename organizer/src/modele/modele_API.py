#!/usr/bin/python3
# -*-coding:utf-8 -*

from agenda.exportations.FabriqueExporteur import *
from agenda.diff.Diff import *
from agenda.importations.AgendaDepuisIcs import importer
from datetime import datetime
import agenda.Agenda
import agenda.Dependance

class ModeleAgenda(object):
	"""
	La classe qui permet de manipuler les L{Agenda}s et toutes les fonctionnalités
	liées.
	C'est elle qui va contenir tous les éléments que la Vue va pouvoir lire.
	Elle permet essentiellement de stocker les Agendas ouverts.
	B{Mais aussi de gérer l'ouverture/fermeture de dépendances (vu que cela consiste
	à charger/décharger des fichiers.}
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
		@todo: cas ou le fichier est déjà chargé, doublons de noms, confirmation, attente, etc
		"""
		agenda = Agenda.Agenda(nomFichier, datetime.now().year)
		importer(agenda, nomFichier)
		self._agendas[nomFichier] = agenda
		return agenda
	#chargerAgenda
	
	
	def dechargerAgenda(self, agenda):
		"""
		Cette fonction permet de décharger un Agenda de la mémoire.
		Il ne sera donc plus pris en compte par le modèle.
		Il doit donc en conséquence ne plus etre accessible par la Vue
		du coté vue.
		Rien se sera sauvegardé non plus, à la charge de la vue de notifier
		l'utilisateur.
		@param self: L'argument implicite
		@type agenda: L{Agenda}
		@param agenda: L'agenda à décharger
		"""
		cible = self._agendas.get(agenda.nomComplet, None)
		if cible is not None:
			cible.detruire()
		#if
	#dechargerAgenda
	
	
	def ajouterDependanceA(self, agenda, nomFichier):
		"""
		Permet d'ajouter une dépendance à un L{Agenda}, importée depuis
		le fichier nomFichier.
		@param self: L'argument implicite
		@type agenda: L{Agenda}
		@param agenda: L'agenda sur lequel ajouter la dépendance
		@type nomFichier: str
		@param nomFichier: un nom de fichier existant
		@raise IOError: Si un problème arrive avec les opérations sur nomFichier
		"""
		dependance = Dependance.Dependance(nomFichier, datetime.now().year)
		importer(dependance, nomFichier)
		agenda.insererFils(dependance)
	#ajouterDependanceA
	
	
	def enleverDependanceDe(self, agenda, nomDependance):
		"""
		Permet de retirer une dépendance de I{agenda}, en se basant sur
		son nom I{nomDependance}.
		Il faut savoir que la recherche d'une dépendance se fait uniquement
		au niveau inférieur de l'agenda cible (ie parmis les fils directs)
		@param self: L'argument implicite
		@type agenda: L{Agenda}
		@param agenda: un agenda duquel on veut retirer une dépendance.
		@type nomDependance: str
		@param nomDependance: le nom de fichier qui représente la dépendance
		"""
		# savoir si on fonctionne par nom ou par références
		agenda.retirerFils(nomDependance)
	#enleverDependanceDe
	
	
	def sauvegarderAgenda(self, agenda, nomDeSauvegarde=None):
		"""
		Permet de sauvegarder un agenda, pour pouvoir le charger plus tard.
		Si on ne fournit pas le nomDeSauvegarde, on utilisera le nom de
		l'agenda.
		@param self: L'argument implicite.
		@type agenda: L{Agenda}
		@param agenda: L'agenda que l'on veut sauvegarder.
		@type nomDeSauvegarde: str
		@param nomDeSauvegarde: un nom de fichier valide
		@raise IOError: Si un problème de droit, d'ecriture, d'ouverture survient.
		"""
		nom = agenda.nomComplet
		if nomDeSauvegarde is not None:
			nom = nomDeSauvegarde
		#if
		exporteur = self._fabrique.fabrique(FabriqueExporteur.exporteurs.ICS, nom)
		exporteur.exporter(agenda)
	#sauvegarderAgenda
	
	
	def faireDiff(self, agenda1, agenda2):
		"""
		Lance une comparaison entre I{agenda1} et I{agenda2}.
		@param self: L'argument implicite.
		@type agenda1: L{Agenda}
		@param agenda1: le premier agenda à comparer.
		@type agenda2: L{Agenda}
		@param agenda2: le second agenda à comparer.
		@rtype: L{Diff}
		@return: Renvoi un objet Diff contenant les différences.
		"""
		if agenda1 is None or agenda2 is None:
			raise ValueError()
		#if
		monDiff = Diff(agenda1, agenda2)
		monDiff.comparer()
		return monDiff
	#faireDiff
	
	
	def avoirAgendaParNomComplet(self, nom):
		"""
		Permet de récupérer un agenda grace à son nom (complet ou non)
		@param self: L'argument implicite
		@type nom: str
		@param nom: le nom (complet ou non) de l'agenda que l'on veut.
		@raise ValueError: si le nom n'existe pas dans le conteneur
		@rtype: L{Agenda}
		@return: L'agenda voulu si il existe dans le conteneur.
		"""
		if nom not in self._agendas.keys():
			for agenda in self._agendas.values():
				if agenda.nom == nom or agenda.nomComplet == nom:
					return agenda
				#if
			#for
			raise ValueError("L'agenda " + str(nom) + " est inconnu !")
		#if
		return self._agendas.get(nom)
	#avoirAgendaParNomComplet
	
	
	@property
	def agendas(self):
		"""Un accesseur pour les agendas disponibles"""
		return self._agendas
	#agendas
	
#ModeleAgenda
