#!/usr/bin/python
# -*-coding:utf-8 -*
from Salle import Salle
from Formation import Formation
from Enseignant import Enseignant
from listeSalle import ListeSalle
from listeFormation import ListeFormation
from listeEnseignant import ListeEnseignant
from urllib2 import urlopen
from lxml import etree
import sys,os

class Base(object):
	"""
	"""
	def __init__(self):
		"""
		"""
		self._listeSalle = ListeSalle()
		self._listeFormation = ListeFormation()
		self._listeEnseignant = ListeEnseignant()
		self._parserXML()
	#fin __init__
	
	def _parserXML(self):
		"""
		"""
		fichier = open(os.path.dirname(os.path.realpath(__file__))+"/base.xml","r")
		tree = etree.parse(fichier)
		for i in tree.xpath("/base/enseignants/enseignant"):
			self._listeEnseignant.ajouterEnseignant(Enseignant(int(i.find("idEnseignant").text),i.find("nom").text, i.find("prenom").text)) 
		for i in tree.xpath("/base/formations/formation"):
			self._listeFormation.ajouterFormation(Formation(int(i.find("idFormation").text), int(i.find("niveau").text), i.find("nom").text, i.find("idEnseignant").text))
		for i in tree.xpath("/base/salles/salle"):
			self._listeSalle.ajouterSalle(Salle(int(i.find("idSalle").text),i.find("nom").text,i.find("taille")))
	#fin _parserXML
	
	@property
	def salles(self):
		"""
		"""
		return self._listeSalle
	#fin salles
	
	@property
	def formations(self):
		"""
		"""
		return self._listeFormation
	#fin formations
	
	@property
	def enseignants(self):
		"""
		"""
		return self._listeEnseignant
	#fin enseignants
	
#fin Base
