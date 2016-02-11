#!/usr/bin/python
# -*-coding:utf-8 -*

import sys, os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../../../outils")
import enum, Fabrique
import ExporteurIcs
import ExporteurTxt


exporteurs = enum.enum('TXT', 'ICS')

class FabriqueExporteur(Fabrique.Fabrique):
	"""
	La classe chargée de créer les exporteurs, afin d'assurer que ce soit
	la seule à devoir etre importer dans les fichiers nécéssitants une exportation.
	Cela assure une faible dépendance envers toute une arborescence de classes.
	
	@author: Laurent Bardoux p1108365
	@version: 1.0
	"""
	
	def __init__(self):
		"""
		Construit une instance de FabriqueExporteur.
		Cela va initialiser le dictionaire interne à toutes les Fabriques
		@param self: L'argument implicite.
		On peut ajouter des L{Exporteur} simplement en modifiant le dictionnaire
		et l'enum.
		"""
		dico = {
			exporteurs.ICS: lambda nom : ExporteurIcs.ExporteurIcs(nom)
			exporteurs.TXT : lambda nom : ExporteurTxt.ExporteurTxt(nom)
		}
		super(FabriqueExporteur, self).__init__(dico)
	#__init__
	
#FabriqueExporteur
