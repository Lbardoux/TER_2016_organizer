#!/usr/bin/python3
# -*-coding:utf-8 -*


_heure_minimale = 7
_heure_maximale = 19

def parse_date(dateCal):
	"""
	Permet de parser une date venant d'un Icalendar
	@type dateCal: str
	@param dateCal: une date au format ICal
	@rtype: tuple
	@return: (annee, mois, jour, heure)
	"""
	split1 = dateCal.split(' ')
	dateComplete = split1[0]
	horaire = split1[1]
	
	chiffres = dateComplete.split('-')
	jour = int(chiffres[2])
	mois = int(chiffres[1])
	annee = int(chiffres[0])

	heures = horaire.split(':')
	heure = int(heures[0])
	minute = int(heures[1])
	
	if heure >= _heure_minimale and heure <= _heure_maximale:
		heure = ((heure - _heure_minimale)*4) + (minute//15) + 1
	else:
		heure = 85 #annule l'entrée courante
	#if
	return (annee, mois, jour, heure)
#parse_date


def _dtstart(obj, attribut):
	"""
	Parse un attribut de type DTSTART
	@type obj: VeventParser
	@param obj: l'objet conteneur
	@type attribut: ...
	@param attribut: l'attribut lu, pour pouvoir extraire sa valeur.
	"""
	Date = str(obj.composant.decoded(str(attribut[0])))
	(annee, mois, jour, heure) = parse_date(Date)
	obj.annee = annee
	obj.jour = jour
	obj.mois = mois
	obj.debut = heure
#_dtstart


def _dtend(obj, attribut):
	"""
	Parse un attribut de type DTEND
	@type obj: VeventParser
	@param obj: l'objet conteneur
	@type attribut:
	@param attribut: l'attribut lu, pour pouvoir extraire sa valeur.
	"""
	Date = str(obj.composant.decoded(str(attribut[0])))
	(annee, mois, jour, heure) = parse_date(Date)
	obj.fin = heure
#_dtend


def _uid(obj, attribut):
	"""
	Parse un attribut de type UID (cas ADE)
	@type obj: VeventParser
	@param obj: l'objet conteneur
	@type attribut: ...
	@param attribut: l'attribut lu, pour pouvoir extraire sa valeur.
	"""
	obj.uid = obj.composant.decoded(str(attribut[0]))
#_uid


def _summary(obj, attribut):
	"""
	Parse un attribut de type SUMMARY.
	@type obj : VeventParser
	@param obj: l'objet conteneur, dont on va devoir modifier les champs
	@type attribut: ...
	@param attribut: l'attribut lu, pour pouvoir extraire sa valeur.
	"""
	obj.summary = obj.composant.decoded(str(attribut[0]))
#_summary


_attribut_vevent = {
	"DTSTART" : _dtstart,
	"DTEND" : _dtend,
	"UID" : _uid,
	"SUMMARY" : _summary
}

class VeventParser:
	"""
	La classe conteneur chargée de récupérer les informations
	d'un Vevent dans le but de créer et remplir un Creneau par la suite.
	@ivar annee: l'annee lue
	@ivar mois: le mois lu
	@ivar jour: le jour lu
	@ivar uid: l'uid lu
	@ivar debut: l'heure de debut lue
	@ivar fin: l'heure de fin lue
	@ivar agenda: l'agenda cible
	@ivar composant: le composant à parser.
	@ivar informations: un dictionnaire contenant les informations non mappées
	@ivar summary: le résumé du Vevent
	@author: Laurent Bardoux p1108365
	@version: 1.0
	"""
	
	def parse(self):
		"""
		Lance la lecture du composant, et remplis les champs.
		@param self: L'argument implicite.
		"""
		for attribut in self.composant.items():
			fonction = _attribut_vevent.get(str(attribut[0]), None)
			if fonction is not None:
				fonction(self, attribut)
			else:
				self.informations[str(attribut[0])] = self.composant.decoded(str(attribut[0]))
			#if 
		#for
	#parse
	
	
	def injection(self):
		"""
		Crée le creneau et le rempli correctement.
		@param self: L'argument implicite.
		@raise ValueError: en cas d'une insertion qui échoue.
		"""
		creneau = self.agenda.ajouterCreneau(self.annee, self.mois, self.jour, self.debut, self.fin)
		if self.uid is not None:
			creneau.identifiant = self.uid
		#if
		if type(self.summary) is not str:
			self.summary = self.summary.decode("utf-8")
		#if
		creneau.resume = self.summary
		for clef in self.informations.keys():
			creneau.ajouterInformation(clef, self.informations[clef])
		#for
	#injection
	
	
	def __init__(self, agenda, composant):
		"""
		Le constructeur de cette classe.
		@param self: l'argument implicite
		@type agenda: L{Agenda}
		@param agenda: l'agenda qui va servir de relais pour la création du creneau.
		@type composant: ...
		@param composant: le composant duquel on va lire les attributs.
		"""
		self.annee = 0
		self.mois = 0
		self.jour = 0
		self.debut = 0
		self.fin = 0
		self.uid = None
		self.agenda = agenda
		self.composant = composant
		self.informations = dict()
		self.summary = ""
	#__init__
#VeventParser


def parseVevent(composant, agenda):
	"""
	Prépare la classe qui va travailler, l'execute, et gère
	les éventuelles exceptions.
	@type agenda: L{Agenda}
	@param agenda: l'agenda qui va servir de relais pour la création du creneau.
	@type composant:
	@param composant: le composant duquel on va lire les attributs.
	@postcondition: si tout s'est bien passé, un creneau est ajouté
	"""
	debug = False
	obj = VeventParser(agenda, composant)
	obj.parse()
	try:
		obj.injection()
	except ValueError as e:
		if debug:
			print("BEGIN:VEVENT -- erreur")
			for i in composant.items():
				print("\t" + str(i[0]) + ":" + str(composant.decoded(str(i[0]))))
			#for
			print("END:VEVENT")
		#if
	#try
#parseVevent
