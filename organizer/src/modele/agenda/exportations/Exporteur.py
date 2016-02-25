#!/usr/bin/python3
# -*-coding:utf-8 -*


class Exporteur(object):
	"""
	Voici une classe générique chargée d'exporter un L{Agenda}.
	Le format d'exportation sera spécifié dans les classes filles.
	@ivar _nomFichier: le nom du fichier dans lequel exporter l'L{Agenda}.
	@ivar _nomAgenda: Le nom de l'agenda que l'on va exporter.
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
		@todo: gestion des récurrences.
		"""
		self._nomFichier = nom
		self._nomAgenda = ""
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
		self._nomAgenda = agenda.nom
		with open(self._nomFichier, 'w') as fichier:
			self._ecrireEntete(fichier)
			for annee in agenda.listeAnnees:
				if annee.nbCreneaux > 0:
					self._faireAnnee(annee, fichier)
				#if
			#for
			self._ecrirePied(fichier)
		#with
	#exporter
	
	
	def _faireAnnee(self, annee, fichier):
		"""
		Lis dans une L{Annee} et ecrit seulement les L{Annee}s qui contiennent
		des L{Creneau}x.
		@param self: L'argument implicite.
		@type annee: L{Annee}
		@param annee: L'L{Annee} que l'on veut traiter.
		@type fichier: file
		@param fichier: le fichier dans lequel écrire.
		@raise IOError: En cas de problème d'écriture.
		"""
		for mois in annee.mois.keys():
			if annee.mois[mois].nbCreneaux > 0:
				self._faireMois(annee, annee.mois[mois], fichier)
			#if
		#for
	#_faireAnnee
	
	
	def _faireMois(self, annee, mois, fichier):
		"""
		Lis dans un L{Mois} et ecrit seulement les L{Mois} qui contiennent
		des L{Creneau}x.
		@param self: L'argument implicite.
		@type annee: L{Annee}
		@param annee: L'L{Annee} que l'on veut traiter.
		@type mois: L{Mois}
		@param mois: le mois à traiter
		@type fichier: file
		@param fichier: le fichier dans lequel écrire.
		@raise IOError: En cas de problème d'écriture.
		"""
		for semaine in mois.semaines:
			if semaine.nbCreneaux > 0:
				self._faireSemaine(annee, mois, semaine, fichier)
			#if
		#for
	#_faireMois
	
	
	def _faireSemaine(self, annee, mois, semaine, fichier):
		"""
		Lis dans une L{Semaine} et ecrit seulement les L{Semaine}s qui contiennent
		des L{Creneau}x.
		@param self: L'argument implicite.
		@type annee: L{Annee}
		@param annee: L'L{Annee} que l'on veut traiter.
		@type mois: L{Mois}
		@param mois: le mois à traiter
		@type semaine: L{Semaine}
		@param semaine: La L{Semaine} que l'on veut traiter.
		@type fichier: file
		@param fichier: le fichier dans lequel écrire.
		@raise IOError: En cas de problème d'écriture.
		"""
		for nomJour in semaine.listeNomJours:
			jour = semaine.jours[nomJour]
			#for jour in semaine.jours.values():
			if len(jour.creneaux) > 0:
				self._faireJour(annee, mois, jour, fichier)
			#if
		#for
	#_faireSemaine
	
	
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
		pass
	#_faireJour
	
	
	def _ecrireEntete(self, fichier):
		"""
		Va écrire l'entete dans le fichier.
		@param self: L'argument implicite.
		@type fichier: file
		@param fichier: Le fichier dans lequel écrire l'entete.
		@raise IOError: Si les droits d'écriture ne sont pas autorisés.
		"""
		pass
	#_ecrireEntete
	
	
	def _ecrirePied(self, fichier):
		"""
		Va écrire le pied dans le fichier.
		@param self: L'argument implicite.
		@type fichier: file
		@param fichier: Le fichier dans lequel écrire l'entete.
		@raise IOError: Si les droits d'écriture ne sont pas autorisés.
		"""
		pass
	#_ecrirePied
	
#Exporteur
