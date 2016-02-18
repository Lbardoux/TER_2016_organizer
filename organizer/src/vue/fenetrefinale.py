#!/usr/bin/python
# -*-coding:utf-8 -*

import sys,os
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__))+"/../modele/formation/")
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__))+"/../../tests/integration/")
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__))+"/../modele/agenda/")
import integration_agenda
import Jour
import Ue, Seance, Cm, Td, Tp, Examen, Autre 
import datetime
import Horaire
import Base
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from final import *
from dialog2 import *
from dialog import *
from arbreUe import *
from seanceVue import *


base = Base.Base()

app = QApplication(sys.argv)
w = QMainWindow(None)
ui = Ui_MainWindow()
ui.setupUi(w)
for i in range(base.formations.taille):
	ui.formations.addItem("")
	ui.formations.setItemText(i,base.formations.liste[i].chaine)

a = arbreUe(ui.listeUe,"arbre")
liste = []
a.premiereConfiguration(liste)
a.secondeConfiguration(liste)
"""
test = integration_agenda.IntegrationAgenda()
dic = test.choperDonnees()

f = monFrame(ui.un,"seance1")
f.setUpMonFrame(0,10,"MIF15 Calculabilité","CM Recursivité","Nautibus C1","S.BRANDEL", "red")


tab = ["pink","green"]
for i in dic.jours[Jour.MARDI].creneaux:
	f2 = monFrame(ui.deux,"creaneau"+str(i.identifiant))
	f2.setUpMonFrame(i.horaire.debut-1,i.horaire.fin-1,"MIF12 Compilation","TP3","Nautibus TP5","E.GUILLOT",tab[i.identifiant%2])
"""

w.show()

d = QDialog(None)
dialog = Ui_Dialog()
dialog.setupUi(d)
for i in range(base.enseignants.taille):
	dialog.responsableUe.addItem("")
	dialog.responsableUe.setItemText(i,base.enseignants.liste[i].nom +" "+ base.enseignants.liste[i].prenom)

def showDialog():
	d.show()
#fin showDialog

def closeDialog():
	d.close()
#fin showDialog

d2 = QDialog(None)
dialog2 = Ui_DialogCalendrier()
dialog2.setupUi(d2)

def showDialog2():
	d2.show()
#fin showDialog2

def closeDialog2():
	d2.close()
#fin showDialog

def reinitializerChamps():
	dialog.codeUe.setText("")
	dialog.nomUe.setText("")
	dialog.responsableUe.setCurrentIndex(-1)
#fin reinitializerChamps

def dessinerArbre():
	a.clear()
	a.premiereConfiguration(liste)
	a.secondeConfiguration(liste)
#fin def

def printInfo():
	enseignant = base.enseignants.trouverEnseignant(dialog.responsableUe.currentText())
	ue = Ue.Ue(str(dialog.codeUe.text()),str(dialog.nomUe.text()),1)
	ue.idEnseignant = enseignant.idEnseignant
	
	for i in range(dialog.nbCM.value()):
		horaire = Horaire.Horaire(1,dialog.dureeCM.value())
		cm = Cm.Cm(i+1,horaire)
		ue.ajouterSeance(cm)
	#fin for
	
	for i in range(dialog.nbTD.value()):
		horaire = Horaire.Horaire(1,dialog.dureeTD.value())
		td = Td.Td(i+1,horaire)
		ue.ajouterSeance(td)
	#fin for
	
	for i in range(dialog.nbTP.value()):
		horaire = Horaire.Horaire(1,dialog.dureeTP.value())
		tp = Tp.Tp(i+1,horaire)
		ue.ajouterSeance(tp)
	#fin for
	
	for i in range(dialog.nbExamen.value()):
		horaire = Horaire.Horaire(1,dialog.dureeExamen.value())
		examen = Examen.Examen(i+1,horaire)
		ue.ajouterSeance(examen)
	#fin for
	
	for i in range(dialog.nbAutre.value()):
		horaire = Horaire.Horaire(1,2)
		autre = Autre.Autre(i+1,horaire)
		ue.ajouterSeance(autre)
	#fin for
	
	liste.append(ue)
	dessinerArbre()
	reinitializerChamps()
	d.close()
#fin printInfo


def setDateStr():
	s = ui.dateEdit.date()
	
	jour = s.toPyDate()
	jourAvant = jour
	jourApres = jour
	listeJours = []
	listeJours.append(s.toString("dd/MM/yyyy"))
	
	for i in range(s.dayOfWeek()-1):
		jourAvant = jourAvant - datetime.timedelta(days=1)
		listeJours.insert(0,jourAvant.strftime('%d/%m/%Y'))
	#fin for
	
	for i in range(7-s.dayOfWeek()):
		jourApres = jourApres + datetime.timedelta(days=1)
		listeJours.append(jourApres.strftime('%d/%m/%Y'))
	#fin for
	
	ui.lundi.setText(listeJours[0]+" Lundi")
	ui.mardi.setText(listeJours[1]+" Mardi")
	ui.mercredi.setText(listeJours[2]+" Mercredi")
	ui.jeudi.setText(listeJours[3]+" Jeudi")
	ui.vendredi.setText(listeJours[4]+" Vendredi")
#fin setDateStr

def fleche1Clique():
	s = ui.dateEdit.date()
	jour = s.toPyDate()
	nouveau = jour - datetime.timedelta(days=7)
	ui.dateEdit.setDate(nouveau)
	setDateStr()
#fin flecheClique

def fleche2Clique():
	s = ui.dateEdit.date()
	jour = s.toPyDate()
	nouveau = jour + datetime.timedelta(days=7)
	ui.dateEdit.setDate(nouveau)
	setDateStr()
#fin flecheClique

ui.dateEdit.setDate(QDate.currentDate())
setDateStr()
ui.buttonCalendrier.connect(ui.buttonCalendrier,QtCore.SIGNAL("clicked()"),showDialog2)
dialog2.calendar.connect(dialog2.calendar,QtCore.SIGNAL("clicked(QDate)"),ui.dateEdit,SLOT("setDate(QDate)") )
dialog2.calendar.connect(dialog2.calendar,QtCore.SIGNAL("clicked(QDate)"),closeDialog2)
dialog2.calendar.connect(dialog2.calendar,QtCore.SIGNAL("clicked(QDate)"),setDateStr)
ui.fleche1.connect(ui.fleche1,QtCore.SIGNAL("clicked()"),fleche1Clique)
ui.fleche2.connect(ui.fleche2,QtCore.SIGNAL("clicked()"),fleche2Clique)

ui.ajout.connect(ui.ajout,QtCore.SIGNAL("clicked()"),showDialog)
dialog.annulerUe.connect(dialog.annulerUe,QtCore.SIGNAL("clicked()"),closeDialog)
dialog.ajouterUe.connect(dialog.ajouterUe,QtCore.SIGNAL("clicked()"),printInfo)
#ui.obligation.hide()
sys.exit(app.exec_())
