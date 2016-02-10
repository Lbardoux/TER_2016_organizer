#!/usr/bin/python
# -*-coding:utf-8 -*
import Ue

class Formation(object):
	"""
	La classe Cm qui hérite la classe seance
	@ivar _idFormation : l'identifiant de la formation
	@ivar _niveau : le niveau de la formation 1->L1 2->L2 3->L3 4->M1 5->M2 6->D1 7->D2 8->D3 0->Autres
	@ivar _nom : le nom de la formation
	@ivar _idEnseignant : l'identifiant du responsable de la formation
	@ivar _listeUe
	@version : 1.0
	@author : Liu Zhuying
	"""
	def __init__(self, idFormation, niveau, nom, id_enseignant):
		"""
		Le constructeur de la classe Formation.
		@param self : L'argument implicite
		@param idFormation : l'identifiant que cette formation aura
		@type idFormation : entier naturel non nul
		@param niveau : le niveau que cette formation aura
		@type niveau : entier naturel
		@param nom :  le nom que cette formation aura
		@type nom : str
		@param id_enseignant : l'identifiant du responsable de cette formation
		@type id_enseignant : entier naturel non nul
		"""
		if idFormation > 0:
			self._idFormation = idFormation
		else:
			self._idFormation = 1
		#fin if
		
		if niveau > 0:
			self._niveau = niveau
		else:
			self._niveau = 0
		#fin if
		
		if bool(nom.strip()):
			self._nom = nom
		else:
			self._nom = "Nom Par Defaut"
		#fin if
		
		if id_enseignant > 0:
			self._idEnseignant = id_enseignant
		else:
			self._idEnseignant = 1
		#fin if
		
		self._listeUe = []	
	#fin __init__
	
	@property
	def idFormation(self):
		"""
		L'accesseur pour l'identifiant de cette Formation
		@param self : L'argument implicite
		@return : son id
		"""
		return self._idFormation
	#fin idFormation
	
	@idFormation.setter
	def idFormation(self, nouvelId):
		"""
		Le mutateur pour l'identifiant de cette Formation
		@param self : L'argument implicite
		@param nouvelId : le nouvel identifiant voulu
		@type nouvelId : entier naturel non nul
		"""
		if nouvelId > 0:
			self._idFormation = nouvelId
	#fin idFormation
	
	@property
	def idEnseignant(self):
		"""
		L'accesseur pour l'identifiant du responsable de cette formation
		@param self : L'argument implicite
		@return : l'identifiant du groupe
		"""
		return self._idEnseignant
	#fin idEnseignant
	
	@idEnseignant.setter
	def idEnseignant(self, nouvelId):
		"""
		Le mutateur pour l'identifiant de l'enseignant
		@param self : L'argument implicite
		@param nouvelId : le nouvel identifiant voulu
		@type nouvelId : entier naturel non nul
		"""
		if nouvelId > 0:
			self._idEnseignant = nouvelId
	#fin idEnseignant
	
	@property
	def niveau(self):
		"""
		L'accesseur pour le niveau de cette formation
		@param self : L'argument implicite
		@return : le niveau
		"""
		return self._niveau
	#fin niveau
	
	@niveau.setter
	def niveau(self, nouveauNiveau):
		"""
		Le mutateur pour le niveau de cette formation
		@param self : L'argument implicite
		@param nouveauNiveau : le nouveau niveau voulu
		@type nouveauNiveau : entier naturel
		"""
		if nouveauNiveau > 0:
			self._niveau = nouveauNiveau
	#fin niveau
	
	@property
	def nom(self):
		"""
		L'accesseur pour le nom de cette formation
		@param self : L'argument implicite
		@return : le nom
		"""
		return self._nom
	#fin nom
	
	@nom.setter
	def nom(self, nouveauNom):
		"""
		Le mutateur pour le nom de cette formation
		@param self : L'argument implicite
		@param nouveauNom : le nouveau nom voulu
		@type nouveauNom : str
		"""
		if bool(nouveauNom .strip()):
			self._nom = nouveauNom
	#fin nom
	
	@property
	def listeUe(self):
		"""
		L'accesseur pour la liste des Ues de cette formation
		@param self : L'argument implicite
		@return : la liste des Ues
		"""
		return self._listeUe
	#fin listeUe
	
	@property
	def nombreUe(self):
		"""
		L'accesseur pour le nombre des Ue la liste des Ues 
		@param self : L'argument implicite
		@return : le nombre des Ue
		"""
		return len(self._listeUe)
	#fin nombreUe
	
	def ajouterUe(self, nouvelleUe):
		"""
		 La fonction qui ajoute une Ue dans la liste des Ues
		 @param self : L'argument implicite
		 @param nouvelleUe : la nouvelle à ajouter
		 @type nouvelleUe : Ue
		"""
		if nouvelleUe not in self._listeUe:
			self._listeUe.append(nouvelleUe)
	#ajouterUe
	
	def supprimerUe(self, uneUe):
		"""
		 La fonction qui supprime une Ue dans la liste des Ues
		 @param self : L'argument implicite
		 @param uneUe : l'Ue à supprimer
		 @type uneUe : Ue
		"""
		if uneUe in self._listeUe:
			self._listeUe.remove(uneUe)
	#supprimerUe
	
	@property
	def chaine(self):
		"""
		La fonction qui convertit une formation en une chaine de caractère(comme master 1 informatique)
		@param self : L'argument implicite
		@return : une chaine de caractère qui décrit la formation
		"""
		
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
		#fin if
		 
		return diplome + " " + str(annee) + " " + self._nom
	#fin chaine
		
#fin Formation

