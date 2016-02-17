#!/usr/bin/python3
# -*-coding:utf-8 -*

import Annee
import Jour
from FabriqueCreneau import CreneauxPossible as CP
from observateur.Observable import *
from observateur.Observeur import *

class Agenda(Observable, Observeur):
	"""
	La classe qui va représenter un agenda.
	Elle fournit donc les fonctions requises pour la création et la
	maintenance d'un agenda.
	Un agenda est une arborescence d'agendas, dont la racine est la partie
	principale.
	Les "fils" sont des dépendances (ou des contraintes) qu'il va falloir respecter.
	
	EXEMPLE ::
		AgendaCours
		|------ AgendaVacance
		|------ AgendaEnseignant1
		|              `-------------etc
		`------ AgendaRecherche
	
	Ainsi, toutes Modifications dans les fils doit impliquer des vérifications dans le
	père.
	A note que la liste des L{Annee} sera régit par un mécanisme d'autovivification.
	ie, que la demande d'une année qui n'existe pas dans la liste entrainera sa création,
	meme si celle-ci reste vide au final.
	
	@author: Laurent Bardoux p1108365
	@version: 1.0
	
	@ivar _nom: le nom de l'agenda courant
	@ivar _pere: l'agenda pere, None équivaut à la racine.
	@ivar _listeFils: Le niveau inférieur de l'arborescence
	@ivar _listeAnnees: la liste des L{Annee} disponible pour cet agenda.
	
	@ivar _formation: La Formation à laquelle est lié cet Agenda.
	@ivar _contraintes: Les contraintes auxquelles est lié cet Agenda
	"""
	
	def __init__(self, nom, annee):
		"""
		Le constructeur de la classe, qui prend simplement le nom de l'agenda en
		paramètre.
		@param self: L'argument implicite
		@param nom: le nom de cet agenda.
		@type nom: str
		@precondition: M{nom doit etre une chaine non vide}
		"""
		Observeur.__init__(self)
		Observable.__init__(self)
		self._nom = nom
		self._pere = None
		self._listeFils = list()
		self._listeAnnees = [Annee.Annee(annee)]
		
		#Branchement avec le reste, par composition
		self._formation = None
		# Les contraintes spécifiques à cet Agenda (pas celle des dépendances)
		self._contraintes = None
	#__init__
	
	
	@property
	def pere(self):
		"""Un accesseur pour le père de cet agenda."""
		return self._pere
	#pere
	
	
	@pere.setter
	@notifier
	def pere(self, agendaPere):
		"""
		Une fonction pour ajouter un père à cet agenda.
		@precondition: agendaPere is not None.
		"""
		self._pere = agendaPere
	#pere
	
	
	@property
	def nom(self):
		"""Un accesseur pour le nom de l'agenda courant (privé de l'arborescence)."""
		return self._nom.split("/")[-1]
	#nom
	
	
	@nom.setter
	@notifier
	def nom(self, autreNom):
		"""Le mutateur associé au nom."""
		if type(autreNom) is str:
			self._nom = autreNom
		#if
	#nom
	
	
	@property
	def listeAnnees(self):
		"""Un accesseur pour la liste des années"""
		return self._listeAnnees
	#listeAnnees
	
	
	@property
	def listeFils(self):
		"""L'accesseur pour récupérer la liste des fils d'un agenda."""
		return self._listeFils
	#fin listeFils
	

	@listeFils.setter
	def listeFils(self, autre):
		"""
		Le mutateur pour affecter une liste à la liste des fils
		Attention, la précédente liste est alors perdue !
		@precondition: autre doit etre une liste d'Agenda !
		"""
		if type(autre) is list:
			self._listeFils = autre
		#if
	#listeFils
	
	
	@property
	def nomComplet(self):
		"""Renvoi le nom complet de l'Agenda (chemin inclu)"""
		return self._nom
	#nomComplet
	
	
	@notifier
	def insererFils(self, *fils):
		"""
		Cette fonction permet d'insérer des fils à cet agenda.
		Les ajouts se feront à la fin de la liste.
		@param self: l'argument implicite
		@param fils: un nombre variable d'arguments, de préférence des agendas
		@type fils: list(Agenda)
		@precondition: *fils doit être constitué d'Agendas
		@postcondition: seul les agendas sont insérés dans la liste
		@rtype: int
		@return: le nombre d'élément dans la liste des fils.
		"""
		for fiston in fils:
			self._listeFils.append(fiston)
			fiston.pere = self
		#for
		return len(self._listeFils)
	#insererFils
	
	
	@notifier
	def retirerFils(self, *nomFils):
		"""
		La fonction qui permet de retirer des agendas fils.
		Elle devra surement être mis à jour pour éviter les références circulaires
		ou propager les destructions.
		En effet, on va propager la destruction en profondeur.
		@param self: l'argument implicite.
		@param nomFils: Les noms des agendas directs de l'agenda courant.
		@type nomFils: list(str)
		@postcondition: les agendas ayant les noms apparaissant dans la liste sont retirés
		"""
		for nom in [elt for elt in nomFils if type(elt) is str]:
			for i, element in enumerate(self._listeFils):
				if element.nom == nom or element.nomComplet == nom:
					element._pere = None
					#vider la liste des fils de cet element
					for fils in element._listeFils:
						element.retirerFils(fils.nom)
					#for
					del self._listeFils[i]
					break
				#if
			#for
		#for
	#retirerFils
	
	
	def _trouveAnnee(self, annee):
		"""
		Trouve et renvoi l'L{Annee} qui a M{annee} comme attribut an.
		@param self: L'argument implicite.
		@type annee: int
		@param annee: Le numéro de l'année voulue (2005 par exemple)
		@rtype: L{Annee}
		@return: None si pas trouvée, une référence sur L{Annee} sinon.
		"""
		for anneeConnue in self._listeAnnees:
			if anneeConnue.an == annee:
				return anneeConnue
			#if
		#for
		return None
	#_trouveAnnee
	
	
	def _autoVivification(self, cible, annee):
		"""
		Gère l'autovivification  de cette liste si cible est None.
		La liste des années est triée !
		Ie crée une nouvelle L{Annee} avec M{annee} comme numéro.
		Ne fait rien si cible n'est pas None.
		@param self: L'argument implicite.
		@type cible: L{Annee}
		@param cible: None (résultat de la recherche de _trouveAnnee) ou une Annee
		@type annee: int
		@param annee: l'annee que l'on veut potentiellement vivifier.
		@rtype: L{Annee}
		@return: une Annee, quoiqu'il arrive.
		"""
		if cible is None:
			temp = Annee.Annee(annee)
			
			# insertion triée
			for i, element in enumerate(self._listeAnnees):
				if element.an >= annee:
					self._listeAnnees.insert(i, temp)
					return temp
				#if
			#for
			self._listeAnnees.append(temp)
			return temp
		#if
		return cible
	#_autoVivification
	
	
	def ajouterCreneau(self, annee, mois, jour, debut, fin, typeCreneau=CP.CRENEAU):
		"""
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
		cible = self._autoVivification(self._trouveAnnee(annee), annee)
		creneau = cible.ajouterCreneau(mois, jour, debut, fin, typeCreneau)
		creneau.dateExacte = (annee, mois, jour)
		try:
			creneau.ajouterObserveur(self)
		except ReferenceError:
			pass
		#try
		return creneau
	#ajouterCreneau
	
	
	@notifier
	def supprimerCreneau(self, annee, mois, jour, creneau):
		"""
		Lance la suppression d'un L{Creneau} si il existe.
		@param self: L'argument implicite
		@type annee: int
		@param annee: l'année dont on veut supprimer un creneau.
		@type mois: int
		@param mois: le mois dont on veut supprimer le créneau.
		@type jour: int
		@param jour: le numéro du jour où le créneau se situe.
		@type creneau: ref(Creneau)
		@param creneau: la référence du Creneau que l'on veut supprimer.
		@raise ValueError: En cas d'erreur sur les arguments.
		"""
		anneeCible = self._trouveAnnee(annee)
		if anneeCible is None:
			raise ValueError("L'année " + str(annee) + " n'existe pas !")
		#if
		
		anneeCible.supprimerCreneau(mois, jour, creneau)
		try:
			creneau.enleverObserveur(self)
		except ValueError:
			pass
		#try
	#supprimerCreneau
	
	
	def recupererSemaineParNumJour(self, annee, mois, jour):
		"""
		Permet de récupérer une Semaine sous la forme d'un
		dictionnaire de jour (mapping : "lundi" -> list(Jour)).
		@param self: L'argument implicite.
		@type annee: int
		@param annee: l'Année dont on veut récupérer les données.
		@type mois: int
		@param mois: Le mois maintenant, de l'annee en question.
		@type jour: int
		@param jour: un des numéros de jours de ce mois
		@raise ValueError: si un des arguments ne matche pas 
		@rtype: L{Semaine}
		@return: La semaine désirée
		"""
		cible = self._autoVivification(self._trouveAnnee(annee), annee)
		semaine = cible.recupererSemaineParNumJour(mois, jour)
		return semaine
	#recupererSemaineParNumJour
	
	
	def recupererJour(self, annee, mois, jour):
		"""
		Permet de récupérer un jour spécifique selon le format suivant :
		jour_voulu = M{jour/mois/annee}
		L'autovivification est également assurée, permettant de toujours
		récupérer une liste si les arguments sont cohérents.
		@param self: L'argument implicite.
		@type annee: int
		@param annee: l'Année dont on veut récupérer les données.
		@type mois: int
		@param mois: Le mois maintenant, de l'annee en question.
		@type jour: int
		@param jour: un des numéros de jours de ce mois
		@rtype: list(Creneau)
		@return: la liste des L{Creneau} de ce jour là, toujours, meme si elle est vide.
		@raise ValueError: si un des arguments est mauvais.
		"""
		semaine = self.recupererSemaineParNumJour(annee, mois, jour)
		creneauxPrincipaux = semaine.trouveJour(jour).creneaux
		jourTemp = Jour.Jour(-5)
		#merge des fils
		for fils in self._listeFils:
			jourFils = fils.recupererJour(annee, mois, jour)
			for i in joursFils:
				jourTemp.insererCreneau(i)
			#for
		#for
		for i in creneauxPrincipaux:
			jourTemp.insererCreneau(i)
		#for
		
		return jourTemp.creneaux
	#recupererJour
	
	
	@notifier
	def deplacerCreneau(self, creneau, annee, mois, jour, debut ,fin):
		"""
		Cette fonction permet de déplacer un creneau dans l'Agenda courant.
		@param self: L'argument implicite
		@type creneau: L{Creneau}
		@param creneau: Le créneaux (ou une classe dérivée) que l'on veut déplacer.
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
		@raise ValueError: Si les données sont erronées.
		"""
		anneeActuelle, moisActuel, jourActuel = creneau.dateExacte
		self.supprimerCreneau(anneeActuelle, moisActuel, jourActuel, creneau)
		creneau.horaire.debut = debut
		creneau.horaire.fin = fin
		cible = self._autoVivification(self._trouveAnnee(annee), annee)
		cible.insererCreneau(creneau, mois, jour)
		creneau.dateExacte = (annee, mois, jour)
	#deplacerCreneau
	
	
	@notifier
	def miseAJour(self, observable, *arguments):
		"""
		Lorsque un créneau nous notifie d'une modification, on notifie
		nous aussi.
		@param self: L'argument implicite
		@type observable: L{Observable}
		@param observable: L'objet qui nous notifie du changement.
		@type arguments: list
		@param arguments: les éventuels arguments supplémentaires fournis lors de l'appel.
		"""
		pass
	#misAJour
	
	
	def detruire(self):
		"""
		Un destructeur pour l'Agenda.
		Cela va mettre à None pas mal de chose pour éviter les références circulaires.
		Toutes les listes seront vidées, et les Agendas fils également.
		@param self: L'argument implicite
		"""
		self._pere = None
		for fils in self._listeFils:
			fils.detruire()
		#for
		del self._listeFils
		del self._listeAnnees
	#detruireAgenda
	
#fin Agenda
