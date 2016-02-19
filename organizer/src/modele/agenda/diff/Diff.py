#!/usr/bin/python3
# -*-coding:utf-8 -*

import Agenda
import Mois
from utilitaireDiff import *

class Diff(object):
	"""
	La classe chargée de faire un "diff", donc de donner les différences
	au format texte, entre 2 L{Agenda}s.
	Pour ce faire, une opération de type && sera effectué pour chaque L{Creneau}
	présents dans les différents Agenda.
	La présentation des différences se fait de la façon suivante :
	_moments contient les "clefs" des différences (date DD/MM/YYYY)
	et _differences associe cette clef à une liste de str, représentants
	les différences "~détaillées".
	@ivar _agenda1: Le premier L{Agenda}
	@ivar _agenda2: Le second L{Agenda}
	@ivar _differences: un dictionnaire de listes des différences relevées lors de la comparaison.
	@ivar _moments: Les différents moments où il y a des différences.
	@author: Laurent Bardoux p1108365
	@version: 1.0
	"""
	
	def __init__(self, agenda1, agenda2):
		"""
		Le constructeur de cette classe, il prend en paramètre les 2
		agendas qu'il va devoir comparer lors de l'appel à la méthode.
		@param self: L'argument implicite
		@type agenda1: L{Agenda}
		@param agenda1: Le premier agenda à comparer.
		@type agenda2: L{Agenda}
		@param agenda2: Le second agenda à comparer.
		@precondition: les 2 agendas ne doivent pas etre None
		"""
		self._agenda1 = agenda1
		self._agenda2 = agenda2
		self._differences = dict()
		self._moments = list()
	#__init__
	
	
	def comparer(self):
		"""
		Lance la comparaison entre les deux L{Agenda}s
		Un compte-rendu sera mis dans _diffences.
		Actuellement, la comparaison ne s'effectue que sur les années communes
		des 2 agendas.
		@param self: L'argument implicite
		"""
		liste1, liste2 = self._assembleListesAComparer()
		for i, elt in enumerate(liste1):
			annee1 = elt
			annee2 = liste2[i]
			for nomMois in Mois.MOIS_LEGAUX:
				mois1 = annee1.mois[nomMois]
				mois2 = annee2.mois[nomMois]
				if mois1.nbCreneaux > 0 or mois2.nbCreneaux > 0:
					self._faireLesMois(mois1, mois2, str(annee1.an) + ":")
				#if
			#for
		#for
	#comparer
	
	
	def _faireLesMois(self, mois1, mois2, phrase):
		"""
		Va appliquer un traitements aux L{Mois}.
		En gros, propager le déroulements aux jours.
		@param self: L'argument implicite
		@type mois1: L{Mois}
		@param mois1: Le mois de la première liste
		@type mois2: L{Mois}
		@param mois2: Le mois de la première liste
		@type phrase: str
		@param phrase: la phrase d'entete des différences
		"""
		jours1 = mois1.jours
		jours2 = mois2.jours
		for i, jour in enumerate(jours1):
			clef = "Pour le " + str(jour.nom) + " " + str(jour.numero) + " " + str(mois1.nom) + " " + phrase
			nb1 = len(jour.creneaux)
			nb2 = len(jours2[i].creneaux)
			if (nb1 == 0 and nb2 != 0) or (nb2 == 0 and nb1 != 0):
				self._faireCasSimple(jour.creneaux, jours2[i].creneaux, clef)
			elif nb1 != 0 and nb2 != 0:
				self._compareCreneaux(jour.creneaux, jours2[i].creneaux, clef)
			#if
		#for
	#_faireLesMois
	
	
	def _compareCreneaux(self, creneaux1, creneaux2, clef):
		"""
		Lance la comparaison des créneaux de chaque jour.
		Si une différence est trouvée, elle sera mise au format str
		dans la liste située dans _differences[clef].
		@param self: L'argument implicite.
		@type creneaux1: list(L{Creneau})
		@param creneaux1: La liste des créneaux du jour1.
		@type creneaux2: list(L{Creneau})
		@param creneaux2: La liste des créneaux du jour2.
		@type clef: str
		@param clef: la clef qu'il faudra rentrer si au moins une différence est trouvée.
		"""
		liste1 = convertitListe(creneaux1)
		liste2 = convertitListe(creneaux2)
		inserer = False
		compteur = 0
		while compteur < len(liste1):
			if liste1[compteur] is None and liste2[compteur] is None:
				compteur += 1
			elif liste1[compteur] is not None and liste2[compteur] is None:
				compteur = self._faireCasComplexe(clef, compteur, liste1, liste2)
			elif liste1[compteur] is None and liste2[compteur] is not None:
				compteur = self._faireCasComplexe(clef, compteur, liste1, liste2)
			else:
				compteur = self._faireCasDebutIdentique(clef, compteur, liste1, liste2)
			#if
		#while
	#_compareCreneaux
	
	
	def _faireCasSimple(self, liste1, liste2, clef):
		"""
		Gère le cas ou un jour est vide et pas l'autre.
		Il suffit donc de relever tous les creneaux du plein en faisant
		remarquer que l'autre est vide.
		@param self: L'argument implicite
		@type liste1: list
		@param liste1: la liste des L{Creneau}x 1, potentiellement vide
		@type liste2: list
		@param liste2: la liste des L{Creneau}x 2, potentiellement vide
		@type clef: str
		@param clef: la clef permettant de relever la différence.
		"""
		self._moments.append(clef)
		texte = "-----------------------------\n"
		if len(liste1) == 0:
			texte += str(self.agenda1.nom) + " ne contient rien !\n"
		else:
			texte += str(self.agenda1.nom) + " contient :\n" + decrireContenu(liste1)
		#if
		texte += "Alors que\n"
		if len(liste2) == 0:
			texte += str(self.agenda2.nom) + " ne contient rien !\n"
		else:
			texte += str(self.agenda2.nom) + " contient :\n" + decrireContenu(liste2)
		#if
		texte += "-----------------------------\n"
		self._differences[clef] = [texte]
	#_faireCasSimple
	
	
	def _faireCasDebutIdentique(self, clef, compteur, liste1, liste2):
		"""
		Traite le cas où il y a 2 créneaux qui commence au meme moment.
		Elle dumpera les erreurs dans les attributs de cette classe
		@precondition: on doit pouvoir comparer les L{Creneau}x (__eq__) sans toucher aux horaires
		@todo: Gérer les cas où il y a plusieurs créneaux simultanement.
		@param self: L'argument implicite
		@type clef: str
		@param clef: la clef permettant de relever la différence.
		@type compteur: int
		@param compteur: là ou l'analyse en est
		@type liste1: list
		@param liste1: une liste issue de la fonction convertitListe !
		@type liste2: list
		@param liste2: une liste issue de la fonction convertitListe !
		@rtype: int
		@return: la valeur ou il faut continuer avec le compteur
		"""
		texte = None
		resultat = compteur
		if liste1[compteur][0].horaire == liste2[compteur][0].horaire:
			if not liste1[compteur][0] == liste2[compteur][0]:
				texte = ""
			#if
			resultat = liste1[compteur][0].horaire.fin + 1
		else:
			fin1 = liste1[compteur][0].horaire.fin
			fin2 = liste2[compteur][0].horaire.fin
			texte = ""
			resultat = fin1 if fin1 < fin2 else fin2
			resultat += 1
		#if
		if texte is not None:
			if clef not in self._moments:
				self._moments.append(clef)
				self._differences[clef] = list()
			#if
			texte = "-----------------------------\n"
			texte += str(self.agenda1.nom) + " prévoit : \n" + str(liste1[compteur][0].versChaine())
			texte += "\nalors que \n"
			texte += str(self.agenda2.nom) + " prévoit : \n" + str(liste2[compteur][0].versChaine())
			texte += "\n-----------------------------\n"
			self._differences[clef].append(texte)
		#if
		return resultat
	#_faireCasDebutIdentique
	
	
	def _faireCasComplexe(self, clef, compteur, liste1, liste2):
		"""
		Traite le cas où il y a 2 créneaux qui commence au meme moment.
		Elle dumpera les erreurs dans les attributs de cette classe
		@precondition: on doit pouvoir comparer les L{Creneau}x (__eq__) sans toucher aux horaires
		@todo: Gérer les cas où il y a plusieurs créneaux simultanement.
		@param self: L'argument implicite
		@type clef: str
		@param clef: la clef permettant de relever la différence.
		@type compteur: int
		@param compteur: là ou l'analyse en est
		@type liste1: list
		@param liste1: une liste issue de la fonction convertitListe !
		@type liste2: list
		@param liste2: une liste issue de la fonction convertitListe !
		@rtype: int
		@return: la valeur ou il faut continuer avec le compteur
		"""
		resultat = compteur
		texte = ""
		if liste1[compteur] is not None:
			#rajout d'un +1 ici !
			resultat = liste1[compteur][0].horaire.fin + 1
			texte = "-----------------------------\n"
			texte += str(self.agenda1.nom) + " prévoit : \n\t" + str(liste1[compteur][0].versChaine())
			texte += "\nalors que \n"
			ite = compteur
			texte += str(self.agenda2.nom) + " prévoit :\n"
			while ite < liste1[compteur][0].horaire.fin:
				if liste2[ite] is not None:
					texte += "\t" + liste2[ite][0].versChaine() + "\n"
					ite = liste2[ite][0].horaire.fin
				else:
					ite += 1
				#if
			#while
			texte += "-----------------------------\n"
		else:
			#rajout d'un +1 ici !
			resultat = liste2[compteur][0].horaire.fin + 1
			texte = "-----------------------------\n"
			texte += str(self.agenda1.nom) + " prévoit :\n"
			ite = compteur
			while ite < liste2[compteur][0].horaire.fin:
				if liste1[ite] is not None:
					texte += "\t" + liste1[ite][0].versChaine() + "\n"
					ite = liste1[ite][0].horaire.fin
				else:
					ite += 1
				#if
			#while
			texte += "\nalors que \n"
			texte += str(self.agenda2.nom) + " prévoit :\n\t" + str(liste2[compteur][0].versChaine())
			texte += "\n-----------------------------\n"
		#if
		if clef not in self._moments and texte is not None:
			self._moments.append(clef)
			self._differences[clef] = list()
		#if
		self._differences[clef].append(texte)
		return resultat
	#_faireCasComplexe
	
	
	def _assembleListesAComparer(self):
		"""
		Assemble 2 listes  pour pouvoir effectuer les comparaisons par boucle for.
		Les listes renvoyées contiennent les L{Annee}s comparables.
		Ie avec au moins un L{Creneau} dans chaque L{Annee}
		si liste1[0] est l'année 2016, alors liste2[0] aussi, et chacune a
		au moins 1 créneau.
		@param self: L'argument implicite.
		@rtype : tuple
		@return: un tuple contenant (Annee1, Annee2)
		@precondition: annees contient les années communes entre les 2 agendas !
		"""
		liste1, liste2 = list(), list()
		for a1 in self._agenda1.listeAnnees:
			if a1.nbCreneaux > 0:
				for a2 in self._agenda2.listeAnnees:
					if a1.an == a2.an and a2.nbCreneaux > 0:
						liste1.append(a1)
						liste2.append(a2)
					#if
				#for
			#if
		#for
		return (liste1, liste2)
	#_assembleListesAComparer
	
	
	@property
	def agenda1(self):
		"""Un accesseur pour le premier agenda"""
		return self._agenda1
	#agenda1
	
	
	@property
	def agenda2(self):
		"""Un accesseur pour le second agenda"""
		return self._agenda2
	#agenda2
	
	
	@property
	def differences(self):
		"""Renvoie la liste des différences obtenue lors de la comparaison."""
		return self._differences
	#differences
	
	
	@property
	def moments(self):
		"""Renvoie la liste des différences obtenue lors de la comparaison."""
		return self._moments
	#differences
	
#Diff
