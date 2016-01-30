#!/usr/bin/python
# -*-coding:utf-8 -*

class Formation:
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
	
#fin Formation
