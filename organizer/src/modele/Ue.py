#!/usr/bin/python
# -*-coding:utf-8 -*

class Ue:
	"""
	"""
	def __init__(self, nom = "defaut ", id_enseignant):
		"""
		"""
		self._nom = nom
		self._id_enseignant = id_enseignant
		self._nombreCm = 0
		self._nombreTd = 0
		self._nombreTp = 0
		self._nombreExamen = 0
		self._nombreAutre = 0
		self._listeElement = list()
	#fin __init__
	
	
	def setNombreCm(self, nombre):
		"""
		"""
		self._nombreCm = nombre	
	#fin setNombreCm
	
	
	def setNombreTd(self, nombre):
		"""
		"""
		self._nombreTd = nombre	
	#fin setNombreTd
	
	
	def setNombreTp(self, nombre):
		"""
		"""
		self._nombreTp = nombre	
	#fin setNombreTp
	
	
	def setNombreExamen(self, nombre):
		"""
		"""
		self._nombreExamen = nombre	
	#fin setNombreExamen
	
	
	def setNombreAutre(self, nombre):
		"""
		"""
		self._nombreAutre = nombre	
	#fin setNombreAutre
	
	def ajouterElement(self, element):
		"""
		"""
		if type(element) is Element:
			self._listeElement.insert(element)
		#fin if
		
	#fin ajouterElement
		
#fin Ue
	
