#!/usr/bin/python3
# -*-coding:utf-8 -*

"""
Voici l'API qui implémente le I{design pattern} Observateur/Observable.


Description
===========
Elle fournit 2 classes essentielles:
	1. L{Observable} : Cette classe, via héritage, permet de rendre observable des objets.
		
		B{Méthodes offertes :}
		
			- L{Observable.Observable.ajouterObserveur}
			- L{Observable.Observable.enleverObserveur}
			- L{Observable.Observable.notifierObserveurs}
		
		B{Exemple :}
		
		>>> class MonObservable(Observable):
		... 	def __init__(self):
		... 		Observable.__init__(self) # <--- IMPORTANT !
		... 	
		... 	@notifier # <--- cette décoration fait la notification à votre place
		... 	def modifierObjet(self):
		... 		#faire des modifications
		... 	
		... 	def autreModification(self):
		... 		self.notifierObserveurs() # fonctionne aussi
		... 		# Cela permet également de passer des paramètres.
	
	
	2. L{Observeur} : Cette classe permet par dérivation d'observer des objets observables.
		
		B{Méthodes offertes :}
		
			- L{Observeur.Observeur.miseAJour}
		
		B{Exemple :}
		
		>>> class MonObserveur(Observeur):
		... 	def __init__(self):
		... 		Observeur.__init__(self)
		... 	
		... 	def miseAJour(self, observable, *arguments):
		... 		# Il faut redéfinir cette méthode, pour pouvoir
		... 		# réagir à la notification de l'objet observé

@author: Laurent Bardoux p1108365
@version: 1.0
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/")
