#!/usr/bin/python3
# -*-coding:utf-8 -*



class Observeur(object):
	"""
	La partie extérieur du design pattern observateur.
	En effet, elle définit les méthodes à surcharger pour réagir lorsque
	l'objet que l'on surveille nous notifie.
	Cette classe va donc de pair avec la classe L{Observable}.
	Rien de plus à en dire.
	@author: Laurent Bardoux p1108365
	@version: 1.0
	"""
	
	def __init__(self):
		"""
		Ne fais rien dans notre cas
		@param self: L'argument implicite
		"""
		pass
	#__init__
	
	
	def miseAJour(self, observable, *arguments):
		"""
		Il va falloir redéfinir cette méthode pour en profiter !
		Pour l'instant elle ne fait rien.
		@param self: L'argument implicite
		@type observable: L{Observable}
		@param observable: L'objet qui nous notifie du changement.
		@type arguments: list
		@param arguments: les éventuels arguments supplémentaires fournis lors de l'appel.
		"""
		pass
	#misAJour
	
#Observeur
