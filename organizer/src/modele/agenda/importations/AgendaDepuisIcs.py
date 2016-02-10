#!/usr/bin/python
# -*-coding:utf-8 -*


import sys, os
import veventIcs
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../../outils")
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../../icalendar-3.9.2")
from icalendar import Calendar
import extension

# Mapping des composants que l'on veut traiter.
_composants = {
	"VEVENT" : veventIcs.parseVevent
	
}

# pas besoin de toucher à cela, tout se fait plus haut.
def importer(agenda, nom):
	"""
	Cette fonction est étroitement liée à un L{Agenda} pour l'import depuis
	un fichier ICS.
	Il utilisera aveuglément les méthodes d'insertions proposées par la partie
	frontale du modèle.
	@type agenda: L{Agenda}
	@param agenda: Un Agenda à remplir/compléter.
	@type nom: str
	@param nom: un nom de fichier
	@precondition: le nom doit avoir .ics comme extension !
	@raise ValueError: si le parsing marche mal (erreur de syntaxe en général).
	@raise IOError: si le fichier est introuvable
	@postcondition: l'Agenda est remplis avec les champs valides.
	"""
	ext = extension.nomFichier(nom)
	if ext != "ics":
		raise ValueError("L'extension doit etre ics !")
	#if
	
	with open(nom, 'r') as fichier:
		donnees = fichier.read()
		calendrier = Calendar.from_ical(donnees)
		for composant in calendrier.walk():
			fonction = _composants.get(composant.name, None)
			if fonction is not None:
				fonction(composant, agenda)
			#if
		#for
	#with, qui fait le close automatiquement
#importer
