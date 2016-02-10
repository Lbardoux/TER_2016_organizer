#!/usr/bin/python
# -*-coding:utf-8 -*

import Agenda

class Exporteur(object):
	"""
	Voici une classe générique chargée d'exporter un L{Agenda}.
	Le format d'exportation sera spécifié dans les classes filles.
	@ivar _nomFichier: le nom du fichier dans lequel exporter l'L{Agenda}.
	@author: Laurent Bardoux
	@version: 1.0
	"""
	
	def __init__(self, nom):
		"""
		Le constructeur de cette classe générique.
		@param self: L'argument implicite.
		@type nom: str
		@param nom: le nom du fichier dans lequel écrire l'export de l'L{Agenda}
		@precondition: nom désigne un fichier valide
		"""
		self._nomFichier = nom
	#__init__
	
	
	def exporter(self, agenda):
		"""
		Lance l'exportation de agenda dans le fichier précisé lors de la construction.
		Cette version générique ne fait rien.
		@param self: L'argument implicite.
		@type agenda: L{Agenda}
		@param agenda: L' L{Agenda} à exporter.
		@precondition: self._nomFichier doit etre un fichier valide.
		@raise IOError: si le nom de fichier pose problème (droits, existence, etc)
		"""
		pass
	#exporter
	
#Exporteur
