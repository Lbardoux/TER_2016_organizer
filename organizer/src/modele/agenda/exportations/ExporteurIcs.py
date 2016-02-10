#!/usr/bin/python
# -*-coding:utf-8 -*

import sys, os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../../agenda")
import Exporteur

class ExporteurIcs(Exporteur.Exporteur):
	"""
	La classe chargée d'exporter un L{Agenda} au format .ics.
	Elle dérive de Exporteur.
	@author: Laurent Bardoux p1108365
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
		super(ExporteurIcs, self).__init__(nom)
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
		with open(self._nomFichier, 'w') as fichier:
			self._ecrireEntete(fichier)
			for annee in agenda.listeAnnees:
				if annee.nbCreneaux > 0:
					self._faireAnnee(annee, fichier)
				#if
			#for
			fichier.write("END:VCALENDAR\n")
		#with
	#exporter
	
	
	def _traiteChiffre(self, chiffre):
		"""
		Transforme un entier en chaine, et si celui-ci n'a que des unités,
		ajoute un 0 supplémentaire devant.
		@param self: L'argument implicite.
		@type chiffre: int
		@param chiffre: l'entier à retravailler.
		@rtype: str
		@return: une chaine formatée pour ce chiffre.
		"""
		if chiffre < 10:
			return "0" + str(chiffre)
		#if
		return str(chiffre)
	#_traiteChiffre
	
	
	def _assembleDate(self, annee, mois, jour, heure):
		"""
		Assemble une date dans le format suivant :
		YYYYMMDDTHHMMSSZ
		@param self: L'argument implicite.
		@type annee: int
		@param annee: le numéro d'annee.
		@type mois: int
		@param mois: le numéro de mois
		@type jour: int
		@param jour: Le numéro de jour
		@type heure: int
		@param heure: le numéro d'horaire venant d'Agenda, a convertir au format horaire.
		@rtype: str
		@return: une date au format précisé plus haut.
		"""
		chaine = str(annee)
		chaine += self._traiteChiffre(mois)
		chaine += self._traiteChiffre(jour)
		chaine += "T"
		temp = (heure-1)*15
		heureDebut = 7 + (temp//60)
		minuteDebut = (temp)%60
		chaine += self._traiteChiffre(heureDebut)
		chaine += self._traiteChiffre(minuteDebut)
		chaine += "00Z"
		return chaine
	#_assembleDate
	
	
	def _faireAnnee(self, annee, fichier):
		"""
		Lis dans une L{Annee} et ecrit seulement les L{Annee}s qui contiennent
		des L{Creneau}x.
		@param self: L'argument implicite.
		@type annee: L{Annee}
		@param annee: L'L{Annee} que l'on veut traiter.
		@type fichier: file
		@param fichier: le fichier dans lequel écrire.
		@raise IOError: En cas d eproblème d'écriture.
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
		@raise IOError: En cas d eproblème d'écriture.
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
		for jour in semaine.jours.values():
			for creneau in jour.creneaux:
				debut = self._assembleDate(annee.an, mois.numero, jour.numero, creneau.horaire.debut)
				fin = self._assembleDate(annee.an, mois.numero, jour.numero, creneau.horaire.fin)
				fichier.write("BEGIN:VEVENT\n")
				fichier.write("DTSTART:" + debut + "\n")
				fichier.write("DTEND:" + fin + "\n")
				fichier.write("UID:" + str(creneau.identifiant) + "\n")
				for info in creneau.informations.keys():
					fichier.write(str(info) + ":" + str(creneau.informations[info]) + "\n")
				#for
				fichier.write("END:VEVENT\n")
			#for
		#for
	#_faireSemaine
	
	
	def _ecrireEntete(self, fichier):
		"""
		Va écrire l'entete d'un ICS dans le fichier.
		@param self: L'argument implicite.
		@type fichier: file
		@param fichier: Le fichier dans lequel écrire l'entete.
		@raise IOError: Si les droits d'écriture ne sont pas autorisés.
		"""
		lignes = [
			"BEGIN:VCALENDAR",
			"METHOD:REQUEST",
			"PRODID:-//CSP_Organizer",
			"VERSION:2.0",
			"CALSCALE:GREGORIAN"
		]
		for l in lignes:
			fichier.write(l + "\n")
		#for
	#_ecrireEntete
	
#ExporteurIcs
