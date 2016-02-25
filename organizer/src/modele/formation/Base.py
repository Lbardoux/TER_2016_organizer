#!/usr/bin/python3
# -*-coding:utf-8 -*

from Salle import Salle
from Formation import Formation
from Enseignant import Enseignant
from listeSalle import ListeSalle
from listeFormation import ListeFormation
from listeEnseignant import ListeEnseignant
from FabriqueCreneau import FabriqueCreneau, CreneauxPossible as CP
from Ue import Ue
from Horaire import Horaire

#from urllib import urlopen
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
	#__init__
	
	def _parserXML(self):
		"""
		@raise IOError: en cas de problème avec ouverture/lecture de fichier.
		"""
		fichier = open(os.path.dirname(os.path.realpath(__file__))+"/../../../data/base.xml","r")
		tree = etree.parse(fichier)
		fichier.close()
		for i in tree.xpath("/base/enseignants/enseignant"):
			self._listeEnseignant.ajouterEnseignant(Enseignant(int(i.find("idEnseignant").text),i.find("nom").text, i.find("prenom").text)) 
		#for
		self._parseFormation(tree)
		for i in tree.xpath("/base/salles/salle"):
			self._listeSalle.ajouterSalle(Salle(int(i.find("idSalle").text),i.find("nom").text, int(i.find("taille").text)))
		#for
	#_parserXML
	
	
	def _parseFormation(self, tree):
		"""
		Va parser le fichier xml pour récupérer les informations sur les L{Formation}s
		Ces informations seront ensuite stockées dans self._listeFormation.
		@param self: L'argument implicite.
		@type tree: un arbre contenaut du xml
		@param tree: le xml completement parsé, racine incluse.
		"""
		for formation in tree.xpath("/base/formations/formation"):
			# on parse les attributs intéressants
			idFormation = int(formation.find("idFormation").text)
			niveau = int(formation.find("niveau").text)
			nom = formation.find("nom").text
			idEnseignant = int(formation.find("idEnseignant").text)
			
			# on crée la nouvelle formation et on l'ajoute
			nouvelleFormation = Formation(idFormation, niveau, nom, idEnseignant)
			self._listeFormation.ajouterFormation(nouvelleFormation)
			
			# on passe au parsing des Ues s'il y en a
			lesUes = formation.find("ues")
			if lesUes is not None:
				self._parseUe(nouvelleFormation, lesUes)
			#if
		#for
	#_parseFormation
	
	
	def _parseUe(self, formation, element):
		"""
		Va lire la suite d'un bout de xml contenant les informations sur les Ues
		Le but sera alors de remplir la listeUes de I{formation}.
		@param self: L'argument implicite.
		@type formation: L{Formation}
		@param formation: La formation dans laquelle écrire les données coolectées.
		@type element: Element
		@param element: le conteneur actuel dans lequel continuer à I{parser}.
		"""
		for fils in element:
			code = fils.find("code").text
			nom = fils.find("nom").text
			idEnseignant = int(fils.find("idEnseignant").text)
			
			nouvelleUe = Ue(code, nom, idEnseignant)
			formation.ajouterUe(nouvelleUe)
			lesSeances = fils.find("seances")
			if lesSeances is not None:
				self._parseSeances(nouvelleUe, lesSeances)
			#if
		#for
	#_parseUe
	
	
	def _parseSeances(self, ue, element):
		"""
		Etape finale, va parser le contenu de chaque Seance, quelque soit son type.
		Chaque Seance lue avec succès entrainera sa création dans le modèle avec
		ajout dans I{ue}.
		@param self: L'argument implicite
		@type ue: L{Ue}
		@param ue: L'ue que l'on veut remplir avec les Seances trouvées.
		@type element: Element(xml)
		@param element: La suite du xml que l'on veut parser.
		"""
		usine = FabriqueCreneau()
		fils = ["cms", "tds", "tps", "examens", "autres"]
		attribut = [CP.CM, CP.TD, CP.TP, CP.EXAMEN, CP.AUTRE]
		for i, typeSeance in enumerate(fils):
			cible = element.find(str(typeSeance))
			if cible is not None:
				for seance in cible:
					idSeance = seance.find("idSeance").text
					nom = seance.find("nom").text
					salle = seance.find("salle").text
					enseignant = ""
					test = seance.find("enseignant")
					if test is not None:
						enseignant = test.text
					#if
					h = seance.find("horaire")
					d = int(h.find("debut").text) + 1
					f = int(h.find("fin").text) + 1
					nouvelleSeance = usine.fabrique(attribut[i], idSeance, Horaire(d, f))
					nouvelleSeance.nom = nom
					nouvelleSeance.salle = salle
					nouvelleSeance.enseignant = enseignant
					ue.ajouterSeance(nouvelleSeance)
				#for
			#if
		#for
	#_parseSeances
	
	
	@property
	def salles(self):
		"""
		"""
		return self._listeSalle
	#salles
	
	@property
	def formations(self):
		"""
		"""
		return self._listeFormation
	#formations
	
	@property
	def enseignants(self):
		"""
		"""
		return self._listeEnseignant
	#enseignants
	
#Base
