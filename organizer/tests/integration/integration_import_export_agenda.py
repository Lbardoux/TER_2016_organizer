#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys, os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../../src")

from modele.agenda.Agenda import *
from modele.agenda.exportations.ExporteurIcs import *
from modele.agenda.importations.AgendaDepuisIcs import *

if __name__ == "__main__":
	print("Lancement du test import/export")
	agenda = Agenda("test.ics", 2011)
	importeur = importer(agenda, "tests/integration/simple.ics")
	dumpeur = ExporteurIcs("tests/integration/resultat.ics")
	dumpeur.exporter(agenda)
#if
