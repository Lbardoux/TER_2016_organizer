#!/usr/bin/python3
# -*-coding:utf-8 -*

"""
Module d'execution en ligne de commande uniquement.
Si vous souhaitez une interface, il va falloir passer par B{make exec} dans le répertoire organizer/
Ici, tout se passe en ligne de commande, donc l'option -h|--help est de rigueur.
@author: Laurent Bardoux p1108365
@version: 1.0
"""

import sys
import argparse
from modele.modele_API import *


if __name__ == "__main__":
	arguments = argparse.ArgumentParser()
	arguments.add_argument("-d", "--diff", help="Seek for the differences between 2 agendas")


	arguments.parse_args()
	modele = ModeleAgenda()
	
#if
