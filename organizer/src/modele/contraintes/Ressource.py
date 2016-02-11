#!/usr/bin/python3
# -*-coding:utf-8 -*

import os, sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/")
import Contrainte

class Ressource(Contrainte.Contrainte):
	"""
	La classe qui gère la notion de ressource.
	Par exemple pas plus de 3 heures de CM par semaine dans une UE
	Elle embarque donc (fermeture) sa limite
	
	@ivar liste_id: la liste des Elements liés à cette ressource
	"""
	
#fin Ressource
