#!/usr/bin/python
# -*-coding:utf-8 -*

import sys, os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../../src")

from modele.agenda.Agenda import *
from modele.agenda.exportations.ExporteurIcs import *

if __name__ == "__main__":
	agenda = Agenda("test.ics", 2011)
	agenda.importeDepuisIcs("simple.ics")
	dumpeur = ExporteurIcs("resultat.ics")
	dumpeur.exporter(agenda)
#if
