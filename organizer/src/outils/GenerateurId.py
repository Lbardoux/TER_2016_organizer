#!/usr/bin/python
# -*-coding:utf-8 -*



class GenerateurId(object):
	"""
	Une classe qui va se charger de générer des identifiants.
	Ces identifiants devant etre unique, un générateur comme celui-ci
	sera communs à tous les L{Agenda}s lors du déroulement.
	Son role est donc d'assurer l'unicité des identifiants produits.
	@ivar _idDepart : l'identifiant de départ, celui que l'on va utiliser
		comme base.
	@ivar _idActuel : Celui que l'on va donner lors de la prochaine
		demande d'identifiant.
	@ivar _increment : Une lambda donnant le ++ d'un élément.
	@author : Laurent Bardoux p1108365
	@version : 1.0
	"""
	
	def __init__(self, pointDeDepart, lambdaIncrement):
		"""
		Initialise ce générateur avec comme valeur initiale M{pointDeDepart}.
		L'incrément de cette valeur initiale sera réalisé par la M{lambdaIncrement}.
		Cette lambda doit prendre un argument et renvoyer le suivant en fonction
		de celui-ci.
		@param self : L'argument implicite.
		@type pointDeDepart : ce qu'on veut.
		@param pointDeDepart : le commencement de l'incrément.
		@type lambdaIncrement : lambda expression renvoyant le meme type que pointDeDepart.
		@param lambdaIncrement : une fonction qui sera utilisé pour réalisé l'incrément.
		"""
		self._idDepart = pointDeDepart
		self._idActuel = pointDeDepart
		self._increment = lambdaIncrement
	#__init__
	
	
	def suivant(self):
		"""
		Renvoi la valeur suivante via la lambda expression.
		@param self : L'argument implicite.
		@rtype : meme type que l'élément configurer au départ.
		@return : l'élément suivant.
		"""
		valeur = self._idActuel
		self._idActuel = self._increment(self._idActuel)
		return valeur
	#suivant

#GenerateurId
