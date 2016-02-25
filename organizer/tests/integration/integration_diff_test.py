#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys, os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../../src")

from modele.agenda.Agenda import *
from modele.agenda.exportations.ExporteurIcs import *
from modele.agenda.exportations.ExporteurTxt import *
from modele.agenda.importations.AgendaDepuisIcs import *
from modele.agenda.diff.Diff import *

if __name__ == "__main__":
	agenda1 = Agenda.Agenda("ADE.ics", 2016)
	agenda2 = Agenda.Agenda("ADE2.ics", 2016)
	importer(agenda1, "tests/integration/ADECal.ics")
	importer(agenda2, "tests/integration/ADECal_2.ics")
	monDiff = Diff(agenda1, agenda2)
	monDiff.comparer()
	for i in monDiff.moments:
		print(i)
		for txt in monDiff.differences[i]:
			print(txt)
#if
