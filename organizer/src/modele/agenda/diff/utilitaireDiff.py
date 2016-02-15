#!/usr/bin/python3
# -*-coding:utf-8 -*

# Définition de fonctions utilitaires ici, pour ne pas encombrer le
# corps de la classe Diff.
# elles sont donc intrinsèquements liées à Diff, et ne doivent pas etre
# utilisée en dehors de celui-ci.
# attention toutefois, ceci va manipuler des Creneau

import Creneau
from Horaire import transformeHoraire, traiteChiffre

def avoirPremierCreneauDepuis(liste, depart):
	"""
	Cette fonction permet de récupérer le premier "creneau" au format
	numérique pour avoir un point de départ.
	L'idée est de chercher le premier creneau occupé (en ignorant les
	blancs dans la liste) à partir de départ.
	@type liste: list 
	@param liste: Une liste de L{Creneau}.
	@type depart: int
	@param depart: le point de départ de la recherche
	@rtype: tuple
	@return: la valeur de debut et de fin tel que debut >= depart
	@raise IndexError: Si aucun Creneau n'a été trouvé.
	"""
	for creneau in liste:
		debut = creneau.horaire.debut
		if debut >= depart:
			return (debut, creneau.horaire.fin)
		#if
	#for
	raise IndexError()
#avoirPremierCreneauDepuis


def definirBornes(debut1, fin1, debut2, fin2):
	"""
	Cette fonction va définir les 2 bornes de l'intervalle quel'on veut
	capturer, elle cache donc la foret d'ifs pour la définition de ces bornes.
	@type debut1: int
	@param debut1: le nombre de départ du premier creneau
	@type fin1: int
	@param fin1: le nombre de fin du premier creneau
	@type debut2: int
	@param debut2: le nombre de départ du second creneau
	@type fin2: int
	@param fin2: le nombre de fin du second creneau
	@rtype: tuple
	@return: le debut et la fin de l'intervalle a capturer.
	"""
	# le "debut" est le creneau qui commence le plus tot.
	debut = debut1 if debut1 < debut2 else debut2
	fin = 0
	if debut1 == debut2:
		# si le depart est le meme, le plus long gagne.
		fin = fin1 if fin1 > fin2 else fin2
	elif debut1 < debut2:
		# si l'un commence avant l'autre, c'est sa fin qui compte
		fin = fin1
	else:
		fin = fin2
	#if
	return (debut, fin)
#definirBornes


def decrireContenu(liste, borneSup=255):
	"""
	Décrit le contenu d'une liste de L{Creneau}x.
	@type liste: list
	@param liste: la liste de créneaux à décrire
	@type borneSup: int
	@param borneSup: Un seuil à ne pas dépasser lors de la description.
	@rtype: str
	@return: la description de la liste
	"""
	resultat = ""
	for elt in liste:
		if elt.horaire.fin < borneSup:
			resultat += "\t" + elt.versChaine() + "\n"
		else:
			temp = elt.versChaine()
			temp = split(" à ", temp)
			i = 0
			resultat += "\t"
			while i < len(temp)-1:
				resultat += temp[i] + " à "
			#while
			h, m = transformeHoraire(borneSup)
			h, m = traiteChiffre(h), traiteChiffre(m)
			resultat += h + "h" + m + "\n"
			break
		#if
	#for
	return resultat
#decrireContenu


def convertitListe(liste):
	"""
	On apporte un peu de connaissance (oui c'est mal ><).
	on transforme une liste de L{Creneau}x en une liste de 49
	éléments contenant soit un créneau, soit None.
	On pourra alors parcourir séquentiellement cette liste,
	avec None = pas de créneau, et une liste de référence = un/des Creneau(x).
	@todo: La gestion de multiples créneaux à un meme moment.
	@type liste: list(L{Creneau})
	@param liste: La liste des Creneaux à convertir.
	@rtype: list
	@return: la liste convertit.
	"""
	resultat = [None]*49
	for creneau in liste:
		debut = creneau.horaire.debut
		fin = creneau.horaire.fin
		i = debut
		while i <= fin and i < len(resultat):
			if resultat[i] is None:
				resultat[i] = list()
			#if
			resultat[i].append(creneau)
			i += 1
		#while
	#for
	return resultat
#convertitListe
