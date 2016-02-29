#!/usr/bin/python3
# -*-coding:utf-8 -*

"""
Ce module contient la classe qui sert de partie frontale pour le modèle.

Elle aura pour principale tache le chargement/déchargement de fichiers,
et les fonctionnalités imposant le recours à plusieurs Agenda différents
(Comme le diff, etc).

Utilisation
===========
	Il suffit juste d'instancier un objet de type ModeleAgenda.
	
	>>> monModele = ModeleAgenda()
	# On peut donc utiliser monModele ensuite
	
	
Fonctions publiques
===================
	1. L{ModeleAgenda.chargerAgenda}(self, nomFichier)
		
		B{Description}:
		
		Cette fonction permet de charger un agenda à partir d'un fichier .ics
		
		B{Usage}
		
		>>> monModele.chargerAgenda("monFichier.ics")
		<Agenda 0x********>
	
	2. L{ModeleAgenda.dechargerAgenda}(self, agenda)
		
		B{Description}:
		
		Cette fonction permet de décharger un agenda à partir de son nom
		
		B{Usage}
		
		>>> monModele.dechargerAgenda(monAgenda.nom)
		# Suppression en mémoire de cet Agenda si il est chargé.
	
	3. L{ModeleAgenda.ajouterDependanceA}(self, agenda, nomFichier)
		
		B{Description}:
		
		Cette fonction permet d'ajouter une dépendance à I{agenda} en chargeant
		un nouvel agenda depuis I{nomFichier}.
		
		B{Usage}
		
		>>> monModele.ajouterDependanceA(monAgenda, "monAgendaDependance.ics")
		# monAgenda possède désormais monAgendaDependance comme ... dépendance.
		
	4. L{ModeleAgenda.enleverDependanceDe}(self, agenda, nomDependance)
		
		B{Description}:
		
		Cette fonction permet d'enlever une dépendance à I{agenda} en se basant sur le nom
		de la dépendance I{nomDependance}.
		
		B{Usage}
		
		>>> monModele.enleverDependanceDe(monAgenda, "monAgendaDependance.ics")
		# Si elle existe, cette dépendance (et toutes les dépendances liées) seront supprimés.
		
	5. L{ModeleAgenda.sauvegarderAgenda}(self, agenda, nomDeSauvegarde=None)
		
		B{Description}:
		
		Cette fonction permet de sauvegarder un agenda.
		Si aucun nom n'est fourni, cela équivaut à sauvegarder avec le nom de l'agenda.
		Si I{nomDeSauvegarde} est donné, cela équivaut à un enregistrer sous.
		
		B{Usage}
		
		>>> monModele.sauvegarderAgenda(monAgenda)
		# monAgenda est sauvegarder avec comme nom I{monAgenda.nom}
		
		>>> monModele.sauvegarderAgenda(monAgenda, "nouveauNom.ics")
		# monAgenda est sauvegarder avec comme nom nouveauNom.ics
		
	6. L{ModeleAgenda.faireDiff}(self, agenda1, agenda2)
		
		B{Description}:
		
		Cette fonction lance la recherche de différence entre I{agenda1} et I{agenda2}.
		B{cf :} L{Diff}
		
		B{Usage}
		
		>>> monDiff = monModele.faireDiff(monAgenda1, monAgenda2)
		>>> monDiff
		<Diff 0x*******>
		
	7. L{ModeleAgenda.avoirAgendaParNomComplet}(self, nom)
		
		B{Description}:
		
		Cette fonction permet de récupérer un agenda via son nom.
		
		B{Usage}
		
		>>> monModele.avoirAgendaParNomComplet("monFichier.ics")
		<Agenda 0x00000000>
		
	8. L{ModeleAgenda.exporterAuFormatTxt}(self, agenda, nomExport)
		
		B{Description}:
		
		Cette fonction permet d'exporter un agenda au format texte
		
		B{Usage}
		
		>>> monModele.exporterAuFormatTxt("monFichier.txt")
		# Voici le nouveau fichier nommé monFichier.txt
"""

from agenda.exportations.FabriqueExporteur import *
from diff.Diff import *
from importations.AgendaDepuisIcs import importer
from datetime import datetime
import Agenda
import Dependance

class ModeleAgenda(object):
	"""
	La classe qui permet de manipuler les L{Agenda}s et toutes les fonctionnalités
	liées.
	C'est elle qui va contenir tous les éléments que la Vue va pouvoir lire.
	Elle permet essentiellement de stocker les Agendas ouverts.
	B{Mais aussi de gérer l'ouverture/fermeture de dépendances (vu que cela consiste
	à charger/décharger des fichiers).}
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
		@todo: Exporter tout les calendrier ouverts (sous ensemble), checkboxes
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
		@raise ValueError: Si le fichier n'est pas un ICS.
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
			del self._agendas[agenda.nomComplet]
			del agenda
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
		exporteur = self._fabrique.fabrique(exporteurs.ICS, nom)
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
	
	
	def exporterAuFormatTxt(self, agenda, nomExport):
		"""
		Permet d'exporter l'I{agenda} au format texte.
		@param self: L'argument implicite.
		@type agenda: L{Agenda}
		@param agenda: L'agenda que l'on veut exporter.
		@type nomExport: str
		@param nomExport: le nom sous lequel exporter (nom de fichier)
		@raise IOError: si un problème survient avec les manipulations de fichiers.
		"""
		exporteur = self._fabrique.fabrique(exporteurs.TXT, nomExport)
		exporteur.exporter(agenda)
	#exporterAuFormatTxt
	
	
	@property
	def agendas(self):
		"""Un accesseur pour les agendas disponibles"""
		return self._agendas
	#agendas
	
#ModeleAgenda
