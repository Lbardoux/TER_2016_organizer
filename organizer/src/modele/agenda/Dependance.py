#!/usr/bin/python3
# -*-coding:utf-8 -*

import Agenda
from FabriqueCreneau import CreneauxPossible as CP

class Dependance(Agenda.Agenda):
	"""
	La classe qui définit une dépendance pour un Agenda.
	Actuellement, une dépendance est un L{Agenda}, dont les
	créneaux sont considérés comme des L{Blocage}s, et qui est immuable
	(comprendre que, en tant que dépendance, on ne peut le modifier directement).
	Attention, on ne doit pas s'en servir comme Agenda principal (ie son
	attribut pere ne doit jamais etre None !)
	@author: Laurent Bardoux p1108365
	@version: 1.0
	"""
	
	def __init__(self, nom, annee):
		"""
		Le constructeur de cette classe.
		Il va construire un "Agenda" avec nom et annee.
		@param self: L'argument implicite.
		@type nom: str
		@param nom: le nom complet de l'agenda (chemin abslu/relatif inclus)
		@type annee: int
		@param annee: l'annee (car oui il en faut bien une) d'initialisation de l'agenda.
		@precondition: M{annee > 0}
		"""
		super(Dependance, self).__init__(nom, annee)
		
	#__init__
	
	
	def ajouterCreneau(self, annee, mois, jour, debut, fin, typeCreneau=CP.CRENEAU):
		"""
		Surcharge de cette méthode pour prendre en compte les spécifications d'une
		Dependance.
		Cela creera forcément un blocage
		Etape 1 de la descente dans l'architecture.
		Ceci va "ajouter" un L{Creneau} dans le M{mois} de l'annee M{annee},
		M{jour}, entre M{debut} et M{fin}.
		Noter que si annee n'existe pas, elle sera automatiquement créée.
		@param self: L'argument implicite
		@type annee: int
		@param annee: l'annee dans laquelle insérer ce créneau.
		@type mois: int
		@param mois: le numéro du mois dans lequel insérer ce créneau.
		@type jour: int
		@param jour: le numéro du jour dans lequel insérer ce créneau.
		@type debut: int [1, 48]
		@param debut: l'heure de début du créneau
		@type fin: int [1, 48]
		@param fin: l'heure de fin du créneau
		@type typeCreneau: enum
		@param typeCreneau: une valeur enumérée pour la fabrique de creneau
		@precondition: debut < fin, mois/jour/debut/fin doivent etre compris dans leurs intervalles respectifs
		@raise ValueError: si les arguments sont erronés.
		@rtype: L{Creneau}
		@return: Un créneau nouvellement créé.
		"""
		#traitements spécifiques ?
		# on ignore le paramètre précisé par l'utilisateur, et on met BLOCAGE a la place
		return super(Dependance, self).ajouterCreneau(annee, mois, jour, debut, fin, CP.BLOCAGE)
	#ajouterCreneau
	
#Dependance
