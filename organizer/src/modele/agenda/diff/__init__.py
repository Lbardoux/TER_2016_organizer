#!/usr/bin/python3
# -*-coding:utf-8 -*

"""
Le package qui offre un moyen de comparer 2 Agendas.

Introduction
============
La classe L{Diff} proposée par le package permet de comparer 2 L{Agenda}s et
d'en fournir un retour textuel.
Par exemple ::
	Pour le lundi 10 aout 2015:
	-----------------------------
	agenda 1 ne contient rien !
	Alors que
	agenda 2 contient :
		Un CM nommé "" est prévu de 13h15 à 14h45
	-----------------------------

	Pour le jeudi 10 decembre 2015:
	-----------------------------
	agenda 1 contient :
		Un CM nommé "" est prévu de 13h15 à 14h45
	Alors que
	agenda 2 ne contient rien !
	-----------------------------

Usage
=====
Pour pouvoir utiliser cette différence, il y a deux temps essentiels.
	1. B{Lancer la comparaison.}
		
		Pour lancer la comparaison, il suffit d'executer les instructions suivantes :
		
		>>> monDiff = Diff(agenda1, agenda2) # où agenda[12] sont des Agenda
		>>> monDiff.comparer()
		
		A partir de là, les agendas sont comparés.
	2. B{Obtenir le compte rendu.}
		
		Il faut savoir 2 choses sur le "compte-rendu" :
			- les différences sont rangées dans B{monDiff.differences}, dans un dictionnaire, sous la forme B{"clef" -> list(difference)}
			- les clefs de ce dictionnaires sont rangées dans l'ordre chronologique dans B{monDiff.moments}.
		
		Il suffit alors, par exemple, de procéder comme ceci :
		
		>>> for clef in monDiff.moments:
		... 	print(clef)
		... 	for difference in monDiff.differences[clef]:
		... 		print(difference)
		
		Et voilà le travail.

Notes
=====
Il reste beaucoup de cas à tester pour valider entièrement cette fonctionnalités.
On pourrait aussi traiter les cas de multiples créneaux.

Algorithmes
===========
::
	trouverLesAnneesComparable()
	Pour chaque année comparable faire
	 |  Pour chaque mois dans ces années faire
	 |   |  Si au moins un des deux à des créneaux d'enregistrés
	 |   |   |  comparerMois()--+
	 |   |  FinSi               |
	 |  FinPour                 |
	FinPour                     |
                                    |
                                    |
	Pour chaque jour dans ce mois faire
	 |  Si un seul des jours est vide
	 |   |  on indique qu'un des jours est vide, et on décrit le contenu de l'autre
	 |  SinonSi aucun n'est vide
	 |   |  comparaisonPlusFine()-----+
	 |  FinSi                         |
	FinPour                           |
                                          |
                                          |
	tableau1 <- transformerListeCreneauxEnTableauDeQuartsHeure(liste1)
	tableau2 <- transformerListeCreneauxEnTableauDeQuartsHeure(liste2)
	TantQue i est inférieur à tableau1.dimension faire
	 |  Si il y a None dans tableau1[i] et tableau2[i] alors
	 |   |  incrementer i
	 |  SinonSi tableau1[i] ou tableau2[i] est vide faire
	 |   |  i <- casComplexe(tableau1, tableau2) [1]
	 |  Sinon si tableau1[i] et tableau2[i] sont plein faire
	 |   |  i <- casDebutIdentique(tableau1, tableau2) [2]
	 |  FinSi
	FinTantQue

	[1]
	on décrit le premier creneau non vide
	puis pendant la durée de ce premier creneau, on décrit ce qu'il y a dans l'autre agenda
	renvoyer durée la plus courte + 1

	[2]
	Si les 2 créneaux ont la meme durée, mais sont différents
	 |  reporter
	 |  renvoyer durée+1
	Sinon
	 |  on garde la durée la plus courte pour évaluer la suite
	 |  on reporte
	 |  renvoyer durée conservée + 1
	FinSi

Voilà
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/..")
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/")
