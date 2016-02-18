#!/usr/bin/python3
# -*-coding:utf-8 -*
import Ue

class Formation(object):
	"""
	La classe Cm qui hérite la classe seance
	@ivar _idFormation: l'identifiant de la formation
	@ivar _niveau: le niveau de la formation 1->L1 2->L2 3->L3 4->M1 5->M2 6->D1 7->D2 8->D3 0->Autres
	@ivar _nom: le nom de la formation
	@ivar _idEnseignant: l'identifiant du responsable de la formation
	@ivar _listeUe: la liste des L{Ue}s de cette formation.
	@version: 1.0
	@author: Liu Zhuying
	"""
	
	def __init__(self, idFormation, niveau, nom, id_enseignant):
		"""
		Le constructeur de la classe Formation.
		@param self: L'argument implicite
		@param idFormation: l'identifiant que cette formation aura
		@type idFormation: entier naturel non nul
		@param niveau: le niveau que cette formation aura
		@type niveau: entier naturel
		@param nom:  le nom que cette formation aura
		@type nom: str
		@param id_enseignant: l'identifiant du responsable de cette formation
		@type id_enseignant: entier naturel non nul
		"""
		self._idFormation = idFormation if idFormation > 0 else 1
		self._niveau = niveau if niveau > 0 else 0
		self._nom = nom if bool(nom.strip()) else "Nom Par Defaut"
		self._idEnseignant = id_enseignant if int(id_enseignant) > 0 else 1
		self._listeUe = list()
	#__init__
	
	
	@property
	def idFormation(self):
		"""L'accesseur pour l'identifiant de cette Formation"""
		return self._idFormation
	#idFormation
	
	
	@idFormation.setter
	def idFormation(self, nouvelId):
		"""Le mutateur pour l'identifiant de cette Formation"""
		if nouvelId > 0:
			self._idFormation = nouvelId
		#if
	#idFormation
	
	
	@property
	def idEnseignant(self):
		"""L'accesseur pour l'identifiant du responsable de cette formation"""
		return self._idEnseignant
	#idEnseignant
	
	
	@idEnseignant.setter
	def idEnseignant(self, nouvelId):
		"""Le mutateur pour l'identifiant de l'enseignant"""
		if nouvelId > 0:
			self._idEnseignant = nouvelId
		#if
	#idEnseignant
	
	
	@property
	def niveau(self):
		"""L'accesseur pour le niveau de cette formation"""
		return self._niveau
	#niveau
	
	
	@niveau.setter
	def niveau(self, nouveauNiveau):
		"""Le mutateur pour le niveau de cette formation"""
		if nouveauNiveau > 0:
			self._niveau = nouveauNiveau
		#if
	#niveau
	
	
	@property
	def nom(self):
		"""L'accesseur pour le nom de cette formation"""
		return self._nom
	#nom
	
	
	@nom.setter
	def nom(self, nouveauNom):
		"""Le mutateur pour le nom de cette formation"""
		if bool(nouveauNom .strip()):
			self._nom = nouveauNom
		#if
	#nom
	
	
	@property
	def listeUe(self):
		"""L'accesseur pour la liste des Ues de cette formation"""
		return self._listeUe
	#listeUe
	
	
	@property
	def nombreUe(self):
		"""L'accesseur pour le nombre des Ue la liste des Ues"""
		return len(self._listeUe)
	#nombreUe
	
	
	def ajouterUe(self, nouvelleUe):
		"""La fonction qui ajoute une Ue dans la liste des Ues"""
		if nouvelleUe not in self._listeUe:
			self._listeUe.append(nouvelleUe)
		#if
	#ajouterUe
	
	
	def supprimerUe(self, uneUe):
		"""La fonction qui supprime une Ue dans la liste des Ues"""
		if uneUe in self._listeUe:
			self._listeUe.remove(uneUe)
		#if
	#supprimerUe
	
	
	@property
	def chaine(self):
		"""La fonction qui convertit une formation en une chaine de caractère(comme master 1 informatique)"""
		if self._niveau in [1,2,3]:
			diplome = "Licence"
			annee = self._niveau
		elif self._niveau in [4,5]:
			diplome = "Master"
			annee = self._niveau - 3
		elif self._niveau in [6,7,8]:
			diplome = "Doctorat"
			annee = self._niveau - 5
		else:
			diplome = ""
			annee = ""
		#if
		return diplome + " " + str(annee) + " " + self._nom
	#chaine
	
#Formation
