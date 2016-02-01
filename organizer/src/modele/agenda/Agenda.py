#!/usr/bin/python
# -*-coding:utf-8 -*

import sys
sys.path.insert(0, "../../")
from outils.VerifierContenuListe import verifier

import Creneau

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
	
	@ivar _nom : le nom de l'agenda courant
	@ivar _pere : l'agenda pere, L{None} équivaut à la racine.
	@ivar _listeFils : Le niveau inférieur de l'arborescence
	@ivar _listeCreneaux : La liste des créneaux qui compose cet agenda.
	@author : Laurent Bardoux p1108365
	@version : 1.0
	"""
	
	def __init__(self, nom):
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
		self._listeCreneaux = list()
	#fin __init__
	
	
	@property
	def pere(self):
		"""
		Un accesseur pour le père de cet agenda.
		@param self : l'argument implicite
		@return une référene sur l'Agenda père, ou None si il n'y en a pas.
		"""
		return self._pere
	#fin pere
	
	
	@pere.setter
	def pere(self, agendaPere):
		"""
		Une fonction pour ajouter un père à cet agenda.
		/!\ ATTENTION /!\
		Une fois un père ajouté, la valeur associé à self._pere devient L{immuable}.
		@precondition : agendaPere is not None
		@postcondition : si self._pere était à None, agendaPere devient le père de cet agenda.
		@param self : le paramètre implicite
		@param agendaPere : le futur papa de l'agenda courant
		@type agendaPere : Agenda, ou un type dérivé
		"""
		if self._pere is None and agendaPere is not None and type(agendaPere) is Agenda:
			self._pere = agendaPere
	#fin pere
	
	
	@property
	def nom(self):
		"""
		Un accesseur pour le nom de l'agenda courant.
		@param self : L'argument implicite.
		@return une str contenant le nom de l'agenda courant.
		"""
		return self._nom
	#fin nom
	
	
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
	#fin nom
	
	
	@property
	def listeFils(self):
		"""
		L'accesseur pour récupérer la liste des fils d'un agenda.
		@param self : l'argument implicite.
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
		@type autre : une liste vide ou de Fils
		"""
		if type(autre) is list:
			if verifier(autre, lambda x : type(x) is Agenda):
				self._listeFils = autre
			#if
		#if
	#fin listeFils
	
	
	@property
	def listeCreneaux(self):
		"""
		L'accesseur pour récupérer la liste des créneaux d'un agenda.
		@param self : l'argument implicite.
		@return : une référence sur la liste des créneaux.
		"""
		return self._listeCreneaux
	#fin listeCreneaux
	
	
	@listeCreneaux.setter
	def listeCreneaux(self, autre):
		"""
		Le mutateur pour affecter une liste à la liste des Creneaux
		Attention, la précédente liste est alors perdue !
		@param self : l'argument implicite
		@param autre : la nouvelle liste, vide ou contenant des Creneaux
		@type autre : une liste vide ou de Creneaux
		"""
		if type(autre) is list:
			if verifier(autre, lambda x : x is not None):
				self._listeCreneaux = autre
			#if
		#if
	#fin listeCreneaux
	
	
	def insererFils(self, *fils):
		"""
		Cette fonction permet d'insérer des fils à cet agenda.
		Les ajouts se feront à la fin de la liste.
		@param self : l'argument implicite
		@param *fils : un nombre variable d'arguments, de préférence des agendas
		@type *fils : des Agendas
		@precondition : *fils doit être constitué d'Agendas
		@postcondition : seul les agendas sont insérés dans la liste
		@return : le nombre d'élément dans la liste des fils.
		"""
		for fiston in fils:
			if type(fiston) is Agenda:
				self._listeFils.append(fiston)
				fiston.pere = self
			#if
		#for
		return len(self._listeFils)
	#fin insererFils
	
	
	def insererCreneaux(self, *creneaux):
		"""
		Cette fonction permet d'insérer des crénaux à cet agenda.
		Les ajouts se feront à la fin de la liste.
		@param self : l'argument implicite
		@param *creneaux : un nombre variable d'arguments, de préférence des Creneaux
		@type *creneaux : Creneau (liste)
		@precondition : *creneaux doit être constitué de Creneau
		@postcondition : seul les Creneaux sont insérés dans la liste
		@return : le nombre d'élément dans la liste des Creneaux.
		"""
		for creneau in creneaux:
			if type(creneau) is Creneau:
				self._listeCreneaux.append(creneau)
			#if
		#for
		return len(self._listeCreneaux)
	#fin insererCreneaux
	
	
	def retirerFils(self, *nomFils):
		"""
		La fonction qui permet de retirer des agendas fils.
		Elle devra surement être mis à jour pour éviter les références circulaires
		ou propager les destructions.
		@param self : l'argument implicite.
		@param *nomFils : Les noms des agendas directs de l'agenda courant.
		@type *nomFils : list(str)
		@postcondition : les agendas ayant les noms apparaissant dans la liste sont 
			retirés
		"""
		for nom in nomFils:
			if type(nom) is str:
				self._listeFils = [fils for fils in self._listeFils if fils.nom != nom]
			#if
		#for
	#fin retirerFils
	
	
	def retirerCreneaux(self, *idCreneaux):
		"""
		Va permettre de retirer des Creneau de la liste.
		On se basera sur les identifiants des Creneaux.
		Elle devra surement être mis à jour pour éviter les références circulaires
		ou propager les destructions.
		@param self : l'argument implicite.
		@param *idCreneaux : Les identifiant directs des Creneaux.
		@type *idCreneaux : list(int)
		@postcondition : les crénaux ayant ces identifiants apparaissant dans la liste sont 
			retirés
		"""
		for ident in idCreneaux:
			if type(ident) is int:
				print("TODO :)")
				#self._listeCreneaux = [creneau for creneau in self._listeCreneaux if creneau.id != ident]
			#if
		#for
	#fin retirerCreneaux
	
#fin Agenda



