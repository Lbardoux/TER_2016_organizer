#!/usr/bin/python
# -*-coding:utf-8 -*

def verifier(conteneur, fonctionBooleenne):
	"""
	Cette fonction utilitaire va permettre de vérifier le contenu
	d'un conteneur supportant le for in.
	Sur chaque élément du conteneur, fonctionBooleenne ser appelée.
	@param conteneur : un conteneur supportant la boucle for
	@type : conteneur(__iter__), list, dict, tuple
	@param fonctionBooleenne : ce qui va tester.
	@type fonctionBooleenne : une fonction/lambda renvoyant true si l'élément est OK
	@return : true si tout est OK, false sinon
	@author : Laurent Bardoux p1108365
	"""
	for element in conteneur:
		if not fonctionBooleen(element):
			return False
		#if
	#for
	return True
#fin verifier