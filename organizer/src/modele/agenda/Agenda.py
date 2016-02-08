#!/usr/bin/python
# -*-coding:utf-8 -*

import Annee
import sys, os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../../outils")
#from VerifierContenuListe import verifier
from FabriqueCreneau import CreneauxPossible as CP
from erreurs.erreurs import *

class Agenda(object):
	"""
	La classe qui va représenter un agenda.
	Elle fournit donc les fonctions requises pour la création et la
	maintenance d'un agenda.
	Un agenda est une arborescence d'agendas, dont la racine est la partie
	principale.
	Les "fils" sont des dépendances (ou des contraintes) qu'il va falloir respecter.
	
	L{EXEMPLE} :
	AgendaCours
	   |------ AgendaVacance
	   |------ AgendaEnseignant1
	   |              `-------------etc
	   `------ AgendaRecherche
	Ainsi, toutes Modifications dans les fils doit impliquer des vérifications dans le
	père.
	
	@ivar _nom : le nom de l'agenda courant
	@ivar _pere : l'agenda pere, None équivaut à la racine.
	@ivar _listeFils : Le niveau inférieur de l'arborescence
	@ivar _listeAnnees : la liste des L{Annee} disponible pour cet agenda.
	
	A note que la liste des L{Annee} sera régit par un mécanisme d'autovivification.
	ie, que la demande d'une année qui n'existe pas dans la liste entrainera sa création,
	meme si celle-ci reste vide au final.
	
	@author : Laurent Bardoux p1108365
	@version : 1.0
	"""
	
	def __init__(self, nom, annee):
		"""
		Le constructeur de la classe, qui prend simplement le nom de l'agenda en
		paramètre.
		@param self : L'argument implicite
		@param nom : le nom de cet agenda.
		@type nom : str
		@precondition : M{nom doit etre une chaine non vide}
		"""
		self._nom = nom
		self._pere = None
		self._listeFils = list()
		self._listeAnnees = [Annee.Annee(annee)]
	#__init__
	
	
	@property
	def pere(self):
		"""
		Un accesseur pour le père de cet agenda.
		@param self : l'argument implicite
		@rtype : L{Agenda}
		@return une référence sur l'Agenda père, ou None si il n'y en a pas.
		"""
		return self._pere
	#pere
	
	
	@pere.setter
	def pere(self, agendaPere):
		"""
		Une fonction pour ajouter un père à cet agenda.
		@precondition : agendaPere is not None
		@postcondition : si self._pere était à None, agendaPere devient le père de cet agenda.
		@param self : le paramètre implicite
		@param agendaPere : le futur papa de l'agenda courant
		@type agendaPere : Agenda, ou un type dérivé
		"""
		self._pere = agendaPere
	#pere
	
	
	@property
	def nom(self):
		"""
		Un accesseur pour le nom de l'agenda courant.
		@param self : L'argument implicite.
		@rtype : str
		@return : le nom de l'agenda courant.
		"""
		return self._nom
	#nom
	
	
	@nom.setter
	def nom(self, autreNom):
		"""
		Le mutateur associé au nom.
		@param self : l'argument implicite.
		@param autreNom : le nom que l'on souhaite mettre.
		@type autreNom : str
		"""
		if type(autreNom) is str:
			self._nom = autreNom
		#if
	#nom
	
	
	@property
	def listeFils(self):
		"""
		L'accesseur pour récupérer la liste des fils d'un agenda.
		@param self : l'argument implicite.
		@rtype : list
		@return : une référence sur la liste des fils
		"""
		return self._listeFils
	#fin listeFils
	

	@listeFils.setter
	def listeFils(self, autre):
		"""
		Le mutateur pour affecter une liste à la liste des fils
		Attention, la précédente liste est alors perdue !
		@param self : l'argument implicite
		@param autre : la nouvelle liste, vide ou contenant des Fils
		@type autre : une liste vide ou de Fils.
		@precondition : autre doit etre une liste d'Agenda !
		"""
		if type(autre) is list:
			self._listeFils = autre
		#if
	#listeFils
	
	
	def insererFils(self, *fils):
		"""
		Cette fonction permet d'insérer des fils à cet agenda.
		Les ajouts se feront à la fin de la liste.
		@param self : l'argument implicite
		@param *fils : un nombre variable d'arguments, de préférence des agendas
		@type *fils : des Agendas
		@precondition : *fils doit être constitué d'Agendas
		@postcondition : seul les agendas sont insérés dans la liste
		@rtype : int
		@return : le nombre d'élément dans la liste des fils.
		"""
		for fiston in fils:
			if type(fiston) is Agenda:
				self._listeFils.append(fiston)
				fiston.pere = self
			#if
		#for
		return len(self._listeFils)
	#insererFils
	
	
	def retirerFils(self, *nomFils):
		"""
		La fonction qui permet de retirer des agendas fils.
		Elle devra surement être mis à jour pour éviter les références circulaires
		ou propager les destructions.
		@param self : l'argument implicite.
		@param *nomFils : Les noms des agendas directs de l'agenda courant.
		@type *nomFils : list(str)
		@postcondition : les agendas ayant les noms apparaissant dans la liste sont retirés
		"""
		for nom in nomFils:
			if type(nom) is str:
				self._listeFils = [fils for fils in self._listeFils if fils.nom != nom]
			#if
		#for
	#retirerFils
	
	
	def _trouveAnnee(self, annee):
		"""
		Trouve et renvoi l'L{Annee} qui a M{annee} comme attribut an.
		@param self : L'argument implicite.
		@type annee : int
		@param annee : Le numéro de l'année voulue (2005 par exemple)
		@rtype : L{Annee}
		@return : None si pas trouvée, une référence sur L{Annee} sinon.
		"""
		for anneeConnue in self._listeAnnees:
			if anneeConnue.an == annee:
				return anneeConnue
			#if
		#for
		return None
	#_trouveAnnee
	
	
	def ajouterCreneau(self, annee, mois, jour, debut, fin, typeCreneau=CP.CRENEAU):
		"""
		Etape 1 de la descente dans l'architecture.
		Ceci va "ajouter" un L{Creneau} dans le M{mois} de l'annee M{annee},
		M{jour}, entre M{debut} et M{fin}.
		Noter que si annee n'existe pas, elle sera automatiquement créée.
		@param self : L'argument implicite
		@type annee : int
		@param annee : l'annee dans laquelle insérer ce créneau.
		@type mois : int
		@param mois : le numéro du mois dans lequel insérer ce créneau.
		@type jour : int
		@param jour : le numéro du jour dans lequel insérer ce créneau.
		@type debut : int [1, 48]
		@param debut : l'heure de début du créneau
		@type fin : int [1, 48]
		@param fin : l'heure de fin du créneau
		@type typeCreneau : enum
		@param typeCreneau : une valeur enumérée pour la fabrique de creneau
		@precondition : debut < fin, mois/jour/debut/fin doivent etre
			compris dans leurs intervalles respectifs
		@raise ArgumentInvalide : si les arguments sont erronés.
		@rtype : L{Creneau}
		@return : Un créneau nouvellement créé.
		"""
		cible = self._trouveAnnee(annee)
		
		if cible is None: # cas ou on ne l'a pas trouvé --> auto-vivification
			cible = Annee.Annee(annee)
			self._listeAnnees.append(cible)
		#if

		#Cette ligne peut balancer l'exception !
		return cible.ajouterCreneau(mois, jour, debut, fin, typeCreneau)
	#ajouterCreneau
	
	
	def supprimerCreneau(self, annee, mois, jour, idCreneau):
		"""
		Lance la suppression d'un L{Creneau} si il existe.
		@param self : L'argument implicite
		@type annee : int
		@param annee : l'année dont on veut supprimer un creneau.
		@type mois : int
		@param mois : le mois dont on veut supprimer le créneau.
		@type jour : int
		@param jour : le numéro du jour où le créneau se situe.
		@type idCreneau : ...
		@param idCreneau : l'identifiant unique du créneau que l'on veut supprimer.
		@raise CreneauInexistant : En cas d'erreur sur les arguments.
		"""
		anneeCible = self._trouveAnnee(annee)
		if anneeCible is None:
			raise CreneauInexistant("L'année " + str(annee) + " n'existe pas !")
		#if
		
		# Cette ligne peut balancer une exception.
		anneeCible.supprimerCreneau(mois, jour, idCreneau)
	#supprimerCreneau
	
	
	def recupererSemaine(self, annee, mois, jour):
		"""
		Permet de récupérer une Semaine sous la forme d'un
		dictionnaire de jour (mapping : "lundi" -> list(Jour)).
		@param self : L'argument implicite.
		@type annee : int
		@param annee : l'Année dont on veut récupérer les données.
		@type mois : int
		@param mois : Le mois maintenant, de l'annee en question.
		@type jour : int
		@param jour : un des numéros de jours de ce mois
		@rtype : dict
		@return : le dictionnaire de la L{Semaine} dont le jour jour/mois/annee fait parti.
		"""
		#rustine
		return self._listeAnnees[0]._mois["janvier"]._semaines[1]._jours
	#recupererSemaine
	
#fin Agenda



