#!/usr/bin/python
# -*-coding:utf-8 -*

def calcul(nbJour, nbHeure):
	"""
	Effectue le calcul du nombre de quart d'heure par semaine pour nous
	Le résultat est alors disponible via TOTAL_PAR_SEMAINE
	@param nbJour: le nombre de jour à compter dans la semaine
	@type nbJour: entier naturel non nul
	@param nbHeure: le nombre d'heures à compter dans la journée
	@type nbHeure: entier naturel non nul compris entre 1 et 24
	@return: un entier représentant le nombre de quart d'heures total;
	"""
	return (nbJour * nbHeure * 4)
#fin calcul

TOTAL_PAR_JOUR = calcul(1, 12)
