#!/usr/bin/python3
# -*-coding:utf-8 -*

"""
Un module remplit de fonctionnalités communes à l'application.

Fonctionnalités
===============

Voici les fonctionnalités offertes :
	1. L{enum.enum} qui permet de créer des valeurs énumérées.
		
		Cela permet de créer un enum comme dans d'autre langages.
		Merci à Alec Thomas de StackOverflow pour la solution.
		
		http://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python
		
		>>> variable = enum("VALEUR1", 'VALEUR2', 'VALEUR3')
		# on a alors variable.VALEUR1, variable.VALEUR2, etc
		
	2. L{extension.nomFichier} qui permet de récupérer l'extension d'un nom de fichier.
		
		>>> nomFichier("/home/lol/fichier.drole.ics")
		ics
		
	3. L{Fabrique} est une classe générique qui encapsule les fonctions essentielles d'une fabrique.
		
		Il suffit d'en dériver en fournissant un dictionnaire lors de la construction.
		Et pour plus de simplicité, mixer les clefs avec un L{enum} !
		
		>>> class MaFabrique(Fabrique):
		... 	def __init__(self):
		... 		dico = {
		... 			monEnum.CLEF1 : lambda x : x,
		... 			monEnum.CLEF2 : fonction
		... 		}
		... 		Fabrique.__init__(self, dico)
		
		Il suffit ensuite d'appeler la méthode L{Fabrique.Fabrique.fabrique} avec les bons arguments.
		
		>>> mf = MaFabrique()
		>>> mf.fabrique(argument_voulu)
		# résultat de la construction
	
	4. L{GenerateurId} qui est un générateur générique d'objet.
		
		Il suffit de lui préciser lors de la construction le point de départ,
		B{inclus dans la génération} et une fonction/lambda qui se chargera de l'opération
		d'incrément.
		
		>>> monGenerateur = GenerateurId(0, lambda x : x+2)
		>>> monGenerateur.suivant()
		0
		>>> monGenerateur.suivant()
		2
	
	5. L{VerifierContenuListe.verifier} qui permet de vérifier le contenu d'une liste.
		
		Il suffit de lui préciser un conteneur itérable (qui accepte le format B{for element in conteneur:},
		et une fonction/lambda qui effectuera les tests sur chaque élément.
		La fonction renvoie True si tous les tests passent, False sinon.
		
		>>> verifier([1, 2, 3, "oups", 4], lambda x : type(x) is int)
		False
		
	6. L{observateur} qui est un package contenant le I{design pattern} Observateur.

@author: Laurent Bardoux p1108365
@version: 1.0
"""
