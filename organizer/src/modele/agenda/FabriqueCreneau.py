#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys, os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../formation")
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../contraintes")
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../../outils")
import Creneau, Seance, Td, Tp, Cm, Examen, Autre
import Blocage
import Fabrique, enum


# enum des valeurs de clefs possible pour cette fabrique.
CreneauxPossible = enum.enum('CRENEAU', 'SEANCE', 'AUTRE', 'EXAMEN', 'TD', 'TP', 'CM', 'BLOCAGE')


class FabriqueCreneau(Fabrique.Fabrique):
	"""
	La fabrique qui va construire des L{Creneau} (ou des classes plus
	spécialisées, comme une L{Seance}, un L{Cm}, etc.
	USAGE :
	Si on veut quelque chose de particulier, il suffit de renseigner
	un des enum situé plus haut (CreneauxPossible).
	Il faudra néanmoins fournir un identifiant et un Horaire en tant qu'arguments.
	@author: Laurent Bardoux p1108365
	@version: 1.0
	"""
	
	def __init__(self):
		"""
		Le constructeur de cette fabrique de L{Creneau}.
		Il va initialiser le dictionnaire pour la création d'une Fabrique.
		@param self: L'argument implicite.
		"""
		# il faudra tenir ce dictionnaire à jour si on veut créer d'autre choses.
		# mais également l'enum situé plus haut
		monDico = {
			CreneauxPossible.CRENEAU : _assembleCreneau,
			CreneauxPossible.SEANCE : _assembleSeance,
			CreneauxPossible.CM : _assembleCm,
			CreneauxPossible.TD : _assembleTd,
			CreneauxPossible.EXAMEN : _assembleExamen,
			CreneauxPossible.TP : _assembleTp,
			CreneauxPossible.AUTRE : _assembleAutre,
			CreneauxPossible.BLOCAGE : _assembleBlocage
		}
		super(FabriqueCreneau, self).__init__(monDico)
	#__init__
	
#FabriqueCreneau


def _assembleCreneau(ident, horaire):
	"""
	Fonction qui assemble un Creneau correctement.
	@type ident: object
	@param ident: l'identifiant que l'on veut.
	@type horaire: L{Horaire}
	@param horaire: L'horaire que l'on veut pour le créneau.
	@rtype: L{Creneau}
	@return: Un créneau tout neuf
	"""
	resultat = Creneau.Creneau(ident, horaire)
	resultat.typeCreneau = CreneauxPossible.CRENEAU
	return resultat
#_assembleCreneau


def _assembleTd(ident, horaire):
	"""
	Fonction qui assemble un Creneau correctement.
	@type ident: object
	@param ident: l'identifiant que l'on veut.
	@type horaire: L{Horaire}
	@param horaire: L'horaire que l'on veut pour le créneau.
	@rtype: L{Td}
	@return: Un créneau tout neuf
	"""
	resultat = Td.Td(ident, horaire)
	resultat.typeCreneau = CreneauxPossible.TD
	return resultat
#_assembleTd


def _assembleSeance(ident, horaire):
	"""
	Fonction qui assemble un Creneau correctement.
	@type ident: object
	@param ident: l'identifiant que l'on veut.
	@type horaire: L{Horaire}
	@param horaire: L'horaire que l'on veut pour le créneau.
	@rtype: L{Seance}
	@return: Un créneau tout neuf
	"""
	resultat = Seance.Seance(ident, horaire)
	resultat.typeCreneau = CreneauxPossible.SEANCE
	return resultat
#_assembleSeance


def _assembleCm(ident, horaire):
	"""
	Fonction qui assemble un Creneau correctement.
	@type ident: object
	@param ident: l'identifiant que l'on veut.
	@type horaire: L{Horaire}
	@param horaire: L'horaire que l'on veut pour le créneau.
	@rtype: L{Cm}
	@return: Un créneau tout neuf
	"""
	resultat = Cm.Cm(ident, horaire)
	resultat.typeCreneau = CreneauxPossible.CM
	return resultat
#_assembleCm


def _assembleTp(ident, horaire):
	"""
	Fonction qui assemble un Creneau correctement.
	@type ident: object
	@param ident: l'identifiant que l'on veut.
	@type horaire: L{Horaire}
	@param horaire: L'horaire que l'on veut pour le créneau.
	@rtype: L{Tp}
	@return: Un créneau tout neuf
	"""
	resultat = Tp.Tp(ident, horaire)
	resultat.typeCreneau = CreneauxPossible.TP
	return resultat
#_assembleTp


def _assembleExamen(ident, horaire):
	"""
	Fonction qui assemble un Creneau correctement.
	@type ident: object
	@param ident: l'identifiant que l'on veut.
	@type horaire: L{Horaire}
	@param horaire: L'horaire que l'on veut pour le créneau.
	@rtype: L{Examen}
	@return: Un créneau tout neuf
	"""
	resultat = Examen.Examen(ident, horaire)
	resultat.typeCreneau = CreneauxPossible.EXAMEN
	return resultat
#_assembleExamen


def _assembleAutre(ident, horaire):
	"""
	Fonction qui assemble un Creneau correctement.
	@type ident: object
	@param ident: l'identifiant que l'on veut.
	@type horaire: L{Horaire}
	@param horaire: L'horaire que l'on veut pour le créneau.
	@rtype: L{Autre}
	@return: Un créneau tout neuf
	"""
	resultat = Autre.Autre(ident, horaire)
	resultat.typeCreneau = CreneauxPossible.AUTRE
	return resultat
#_assembleAutre


def _assembleBlocage(ident, horaire):
	"""
	Fonction qui assemble un Creneau correctement.
	@type ident: object
	@param ident: l'identifiant que l'on veut.
	@type horaire: L{Horaire}
	@param horaire: L'horaire que l'on veut pour le créneau.
	@rtype: L{Blocage}
	@return: Un créneau tout neuf
	"""
	resultat = Blocage.Blocage(ident, horaire)
	resultat.typeCreneau = CreneauxPossible.BLOCAGE
	return resultat
#_assembleBlocage

