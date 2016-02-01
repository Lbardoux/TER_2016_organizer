#!/usr/bin/python
# -*-coding:utf-8 -*

class Ue(object):
	"""
	La classe qui représente une unité d'enseignement.
	@ivar _code : le code UE, par exemple : MIF18, LIF15
	@ivar _nom : le nom de UE, par exemple : Base de données avancée
	@ivar _idEnseignant : l'identifiant du responsable de l'Ue
	@ivar _nombreInscrit : le nombre d'etudiants inscrits dans cette Ue
	@ivar _nombreGroupe : le nombre de groupes de cette Ue 
	@ivar _nombreCm : Le nombre de Cms que contient cette Ue
	@ivar _nombreTd : Le nombre de Tds que contient cette Ue
	@ivar _nombreTp : Le nombre de Tps que contient cette Ue
	@ivar _nombreExamen : Le nombre de Examens que contient cette Ue
	@ivar _nombreAutre : Le nombre de séances autre que CM TD TP Examen
	@ivar _listeSeance : La liste des seances que cette Ue contient
	@version : 1.0
	@author : Liu Zhuying
	"""
	def __init__(self, code, nom, id_enseignant):
		"""
		Le constructeur de la classe Enseignant.
		@param self : L'argument implicite
		@param code : l'identifiant que cet enseignant aura
		@type code : str
		@param nom : le nom que cet enseignant aura
		@type nom : str
		@param id_enseignant : le prenom que cet enseignant aura
		@type id_enseignant : entier naturel non nul
		"""
		if bool(code.strip()):
			self._code = code
		else:
			self._code = "Code Null"
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
		
		self._nombreInscrit = 1
		self._nombreGroupe = 1
		self._nombreCm = 0
		self._nombreTd = 0
		self._nombreTp = 0
		self._nombreExamen = 0
		self._nombreAutre = 0
		self._listeSeance = []
	#fin __init__
	
	@property
	def code(self):
		"""
		L'accesseur pour le code de cette Ue
		@param self : L'argument implicite
		@return : le code
		"""
		return self._code
	#fin code
	
	@property
	def nom(self):
		"""
		L'accesseur pour le nom de cette Ue
		@param self : L'argument implicite
		@return : son nom
		"""
		return self._nom
	#fin nom
	
	@property
	def idEnseignant(self):
		"""
		L'accesseur pour l'identifiant de l'enseignant
		@param self : L'argument implicite
		@return : l'identifiant de l'enseignant
		"""
		return self._idEnseignant
	#fin idEnseignant
	
	@property
	def nombreIscrit(self):
		"""
		L'accesseur pour le nombre d'inscrits de cette Ue
		@param self : L'argument implicite
		@return : le nombre d'inscrits
		"""
		return self._nombreInscrit
	#fin nombreIscrit
	
	@property
	def nombreGroupe(self):
		"""
		L'accesseur pour le nombre de Groupes de cette Ue
		@param self : L'argument implicite
		@return : le nombre de Groupes
		"""
		return self._nombreGroupe
	#fin nombreGroupe
	
	@property
	def nombreCm(self):
		"""
		L'accesseur pour le nombre de Cms de cette Ue
		@param self : L'argument implicite
		@return : le nombre de Cms
		"""
		return self._nombreCm
	#fin nombreCm
	
	@property
	def nombreTd(self):
		"""
		L'accesseur pour le nombre de Tds de cette Ue
		@param self : L'argument implicite
		@return : le nombre de Tds
		"""
		return self._nombreTd
	#fin nombreTd
	
	@property
	def nombreTp(self):
		"""
		L'accesseur pour le nombre de Tps de cette Ue
		@param self : L'argument implicite
		@return : le nombre de Tps
		"""
		return self._nombreTp
	#fin nombreTp
	
	@property
	def nombreExamen(self):
		"""
		L'accesseur pour le nombre d'Examens de cette Ue
		@param self : L'argument implicite
		@return : le nombre d'Examens
		"""
		return self._nombreExamen
	#fin nombreExamen
	
	@property
	def nombreAutre(self):
		"""
		L'accesseur pour le nombre d'Autres de cette Ue
		@param self : L'argument implicite
		@return : le nombre d'Autres
		"""
		return self._nombreAutre
	#fin nombreAutre
	
	@property
	def listeSeance(self):
		"""
		L'accesseur pour la liste de Seances de cette Ue
		@param self : L'argument implicite
		@return : la liste de Seances
		"""
		return self._listeSeance
	#fin listeSeance
	
	@property
	def listeCm(self):
		"""
		La fonction qui envoie que les Cms dans la liste de seances 
		@param self : L'argument implicite
		@return : une liste de Cms
		"""
		listeRetour = []
		for seance in self._listeSeance:
			
			if type(seance) is Cm:
				listeRetour.append(seance)
			#fin if
			
		#fin for
		return listeRetour
	#fin listCm
	
	@property
	def listeTd(self):
		"""
		La fonction qui envoie que les Tds dans la liste de seances 
		@param self : L'argument implicite
		@return : une liste de Tds
		"""
		listeRetour = []
		for seance in self._listeSeance:
			
			if type(seance) is Td:
				listeRetour.append(seance)
			#fin if
			
		#fin for
		return listeRetour
	#fin listTd
	
	@property
	def listeTp(self):
		"""
		La fonction qui envoie que les Tps dans la liste de seances 
		@param self : L'argument implicite
		@return : une liste de Tps
		"""
		listeRetour = []
		for seance in self._listeSeance:
			
			if type(seance) is Tp:
				listeRetour.append(seance)
			#fin if
			
		#fin for
		return listeRetour
	#fin listTp
	
	@property
	def listeExamen(self):
		"""
		La fonction qui envoie que les Examens dans la liste de seances 
		@param self : L'argument implicite
		@return : une liste de Examens
		"""
		listeRetour = []
		for seance in self._listeSeance:
			
			if type(seance) is Examen:
				listeRetour.append(seance)
			#fin if
			
		#fin for
		return listeRetour
	#fin listExamen
	
	@property
	def listeAutre(self):
		"""
		La fonction qui envoie que les Autres dans la liste de seances 
		@param self : L'argument implicite
		@return : une liste de Autres
		"""
		listeRetour = []
		for seance in self._listeSeance:
			
			if type(seance) is Autre:
				listeRetour.append(seance)
			#fin if
			
		#fin for
		return listeRetour
	#fin listAutre
	
	def ajouterSeance(self, nouvelleSeance):
		"""
		La méthode qui ajoute une nouvelle seance en fonction de son type dans la liste 
		@param self : L'argument implicite
		@param nouvelleSeance : la nouvelle Seance à ajouter
		@type idSeance : entier naturel non nul
		"""
		if isinstance(nouvelleSeance, Seance):
			
			self._listeSeance.insert(nouvelleSeance)
			if type(nouvelleSeance) is Cm:
				self._nombreCm += 1
			elif type(nouvelleSeance) is Td:
				self._nombreTd +=1
			elif type(nouvelleSeance) is Tp:
				self._nombreTp +=1
			elif type(nouvelleSeance) is Examen:
				self._nombreExamen +=1
			elif type(nouvelleSeance) is Autre:
				self._nombreAutre +=1
			#fin if
			    
		#fin if
		
	#fin ajouterSeance

#fin Ue
