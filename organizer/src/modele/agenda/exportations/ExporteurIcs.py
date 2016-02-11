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
		#temp = (heure-1)*15
		heureDebut, minuteDebut = self._transformeHoraire(heure)
		#heureDebut = 7 + (temp//60)
		#minuteDebut = (temp)%60
		chaine += self._traiteChiffre(heureDebut)
		chaine += self._traiteChiffre(minuteDebut)
		chaine += "00Z"
		return chaine
	#_assembleDate
	
	
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
	
	
	def _ecrirePied(self, fichier):
		"""
		Va écrire le pied dans le fichier.
		@param self: L'argument implicite.
		@type fichier: file
		@param fichier: Le fichier dans lequel écrire l'entete.
		@raise IOError: Si les droits d'écriture ne sont pas autorisés.
		"""
		fichier.write("END:VCALENDAR\n")
	#_ecrirePied
	
#ExporteurIcs
