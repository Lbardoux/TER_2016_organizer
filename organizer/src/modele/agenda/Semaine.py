﻿#!/usr/bin/python
# -*-coding:utf-8 -*

import Jour

###############################################################################
# Le nom des champs de l'argument de construction :
DEBUT = "_debut_"
FIN = "_fin_"
N_DEBUT = "_ndebut_"
N_FIN = "_nfin_"
# syntaxe générale :
# {DEBUT : jour_debut, N_DEBUT : numero_debut, FIN : jour_fin, N_FIN : numero_fin}
###############################################################################

def construireArgument(nomPremierJour, numeroPremierJour, nomDernierJour, numeroDernierJour):
	"""
	Permet de construire plus facilement un argument pour le __init__ de L{Semaine}.
	Cela autorise ainsi les semaines incomplètes lors des début ou des fins de mois.
	
	Il faut voir cette fonction comme : 
	Lundi x  --->  vendredi y
	
	@precondition : ^nom(Premier|Dernier)Jour$ doit appartenir à JOURS_LEGAUX dans L{Jour}.
	@precondition : ^numero(Premier|Dernier)Jour$ doit être compris entre 1 et 31.
	
	@type nomPremierJour : str
	@param nomPremierJour :
	@type numeroPremierJour : int
	@param numeroPremierJour :
	@type nomDernierJour : str
	@param nomDernierJour :
	@type numeroDernierJour : int
	@param numeroDernierJour :
	@rtype : dict.
	@return : Un argument valable pour le __init__ de L{Semaine}.
	"""
	resultat = dict()
	resultat[DEBUT] = nomPremierJour
	resultat[N_DEBUT] = numeroPremierJour
	resultat[FIN] = nomDernierJour
	resultat[N_FIN] = numeroDernierJour
	return resultat
#construireArgument


class Semaine(object):
	"""
	La classe qui va définir une Semaine.
	Il faut savoir qu'une semaine d'un mois peut très bien contenir moins de 7 jours.
	Par exemple, elle peut se finir un jeudi (passage au mois d'après, dont la première semaine
	commence un vendredi)
	
	@ivar _numero : le numéro de cette semaine dans le mois courant.
	@ivar _jours : un conteneur de L{Jour}, identifiés par leurs JOURS.
	@ivar _listeNomJours : une liste des jours connus.
	@author : Laurent Bardoux p1108365
	@version : 1.0
	"""
	
	def __init__(self, numero, intervalle):
		"""
		Le constructeur de cette classe.
		ATTENTION : I lest vivement recommandé d'utiliser la fonction
		construireArgument pour créer l'argument intervalle.
		@param self : L'argument implicite.
		@type numero : int.
		@param numero : Le numéro de la semaine dans le mois courant.
		@type intervalle : dict formaté.
		@param intervalle : Un dictionnaire contenant tout ce qu'il faut pour
			assembler correctement une Semaine.
		"""
		self._numero = numero
		self._jours = dict()
		self._listeNomJours = list()
		tempNum = intervalle[N_DEBUT]
		i = 0
		condition = False
		while i < len(Jour.JOURS_LEGAUX):
			nomActuel = Jour.JOURS_LEGAUX[i]
			if intervalle[DEBUT] == nomActuel:
				condition = True
			#if
			if condition == True:
				self._jours[nomActuel] = Jour.Jour(tempNum, nomActuel)
				self._listeNomJours.append(nomActuel)
				tempNum += 1
			#if
			if intervalle[FIN] == nomActuel:
				condition = False
				break
			#if
			i += 1
		#while
	#__init__
	
	
	@property
	def numero(self):
		"""
		L'accesseur pour le numéro de la semaine.
		@param self : L'argument implicite.
		@rtype : int
		@return : le numéro de la semaine dans le mois courant.
		"""
		return self._numero
	#numero
	
	
	@numero.setter
	def numero(self, nouveauNumero):
		"""
		Le mutateur associé, pour changer ce numéro.
		@param self : L'argument implicite.
		@type nouveauNumero : int.
		@param nouveauNumero : le nouveau numéro que l'on souhaite.
		"""
		self._numero = nouveauNumero
	#numero
	
	
	@property
	def jours(self):
		"""
		L'accesseur pour les jours que contient cette semaine.
		@param self : L'argument implicite.
		@rtype : dict.
		@return : un dictionnaire contenant les jours de cette semaine dans le
			mois courant.
		@postcondition : accès à ce dictionnaire en lecture seule.
		"""
		return self._jours
	#jours
	
	
	@property
	def listeNomJours(self):
		"""
		Un accesseur pour connaître les jours connus par cette Semaine, dans
		l'ordre officiel européen, permettant d'itérer plus facilement.
		@param self : l'argument implicite.
		@rtype : list
		@return : la liste des JOURS connus classée.
		"""
		return self._listeNomJours
	#listeNomJours
	
	
	def recupererJour(self, nomJour):
		"""
		Cette fonction permet de récupérer un L{Jour} dans la Semaine, 
		si il existe.
		@param self : l'argument implicite.
		@type nomJour : str
		@param nomJour : un nom de jour connu, appartenant à JOURS_LEGAUX.
		@rtype : Jour
		@return : le jour voulu, ou None si il n'est pas trouvé.
		"""
		if nomJour in self._listeNomJours:
			return self._jours[nomJour]
		#if
		return None
	#recupererJour
	
#Semaine