#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys, os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../src/icalendar-3.9.2/src/")

import icalendar
from icalendar import Calendar, Event

fichier_test = "tests/simple.ics"

class Test_ICalendar(unittest.TestCase):
	"""
	Mes premiers pas avec ICalendar.
	@author : Laurent Bardoux p1108365
	"""
	def test_import(self):
		"""Premiers tests sur l'import d'un ICS"""
		f = open(fichier_test)
		contenu = f.read()
		calendrier = Calendar.from_ical(contenu)
		# un composant est un BEGIN:quelquechose
		#for composant in calendrier.walk():
		#	if composant.name == "VEVENT":
		#		for i,e in composant.items():
		#			print(str(i))
		#			print(composant.decoded(i))
		#		#for
		#	#if
		#for
		f.close()
	#test_import
	
	
#Test_ICalendar

if __name__ == "__main__":
	unittest.main()
