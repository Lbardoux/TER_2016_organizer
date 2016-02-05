#!/usr/bin/python
# -*-coding:utf-8 -*

import sys, os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../formation")
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../../outils")
import Creneau, Seance, Td, Tp, Cm, Examen, Autre
import Fabrique, enum


# enum des valeurs de clefs possible pour cette fabrique.
CreneauxPossible = enum.enum('CRENEAU', 'SEANCE', 'AUTRE', 'EXAMEN', 'TD', 'TP', 'CM')


class FabriqueCreneau(Fabrique.Fabrique):
	"""
	La fabrique qui va construire des L{Creneau} (ou des classes plus
	spécialisées, comme une L{Seance}, un L{Cm}, etc.
	
	USAGE :
		Si on veut quelque chose de particulier, il suffit de renseigner
		un des enum situé plus haut (CreneauxPossible).
		Il faudra néanmoins fournir un Horaire en tant qu'unique argument.
	
	@author : Laurent Bardoux p1108365
	@version : 1.0
	"""
	
	def __init__(self):
		"""
		Le constructeur de cette fabrique de L{Creneau}.
		Il va initialiser le dictionnaire pour la création d'une Fabrique.
		@param self : L'argument implicite.
		"""
		# ilfaudra tenir ce dictionnaire à jour si on veut créer d'autre choses.
		# mais également l'enul situé plus haut
		monDico = {
			CreneauxPossible.CRENEAU : lambda ident, horaire : Creneau.Creneau(ident, horaire),
			CreneauxPossible.SEANCE : lambda ident, horaire : Seance.Seance(ident, horaire),
			CreneauxPossible.CM : lambda ident, horaire : Cm.Cm(ident, horaire),
			CreneauxPossible.TD : lambda ident, horaire : Td.Td(ident, horaire),
			CreneauxPossible.EXAMEN : lambda ident, horaire : Examen.Examen(ident, horaire),
			CreneauxPossible.TP : lambda ident, horaire : Tp.Tp(ident, horaire),
			CreneauxPossible.AUTRE : lambda ident, horaire : Autre.Autre(ident, horaire)
		}
		super(FabriqueCreneau, self).__init__(monDico)
	#__init__
	
#FabriqueCreneau
