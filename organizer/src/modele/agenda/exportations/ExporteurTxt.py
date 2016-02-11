#!/usr/bin/python
# -*-coding:utf-8 -*

import Exporteur

class ExporteurTxt(Exporteur.Exporteur):
	"""
	La classe chargée d'exporter un Agenda au format texte.
	@author: Laurent Bardoux p1108365
	@version: 1.0
	"""
	
	def __init__(self, nom):
		"""
		Le constructeur de cette classe.
		@param self: L'argument implicite.
		@type nom: str
		@param nom: le nom du fichier dans lequel on veut exporter.
		"""
		super(ExporteurTxt, self).__init__(nom)
	#__init__
	
	
	def _faireJour(self, annee, mois, jour, fichier):
		"""
		La fonction à surcharger pour traiter une journée !
		elle doit traiter la liste des creneaux de M{jour}.
		@param self: L'argument implicite.
		@type annee: L{Annee}
		@param annee: L'L{Annee} que l'on veut traiter.
		@type mois: L{Mois}
		@param mois: le mois à traiter
		@type jour: L{Jour}
		@param jour: Le L{Jour} que l'on veut traiter.
		@type fichier: file
		@param fichier: le fichier dans lequel écrire.
		@raise IOError: En cas de problème d'écriture.
		"""
		for creneau in jour.creneaux:
			
		#for
	#_faireJour
	
	
	def _ecrireEntete(self, fichier):
		"""
		Va écrire l'entete dans le fichier.
		@param self: L'argument implicite.
		@type fichier: file
		@param fichier: Le fichier dans lequel écrire l'entete.
		@raise IOError: Si les droits d'écriture ne sont pas autorisés.
		"""
		fichier.write()
	#_ecrireEntete
	
	
	def _ecrirePied(self, fichier):
		"""
		Va écrire le pied dans le fichier.
		@param self: L'argument implicite.
		@type fichier: file
		@param fichier: Le fichier dans lequel écrire l'entete.
		@raise IOError: Si les droits d'écriture ne sont pas autorisés.
		"""
		fichier.write()
	#_ecrirePied
	
#ExporteurTxt
