#!/usr/bin/python3
# -*-coding:utf-8 -*

def nomFichier(nom):
	"""
	Renvoie l'extension du fichier qui a pour nom M{nom}.
	@type nom : str
	@param nom : le nom du fichier
	@rtype : str
	@return : une chaine contenant l'extension privée du '.'
	"""
	morceaux = nom.split('.')
	taille = len(morceaux)
	if taille == 1 or taille == 0:
		return ""
	#if
	return morceaux[-1]
#nomFichier
