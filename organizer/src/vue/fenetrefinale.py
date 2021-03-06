#!/usr/bin/python
# -*-coding:utf-8 -*

import sys,os
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__))+"/../modele/formation/")
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__))+"/../../tests/integration/")
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__))+"/../modele/agenda/")
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__))+"/../modele/")
import integration_agenda
import Jour
import Agenda
import modele_API
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
from drag6 import *
from agenda.diff import Diff
from affichageDiff import *


ma = modele_API.ModeleAgenda()

#agenda = ma.chargerAgenda(os.path.dirname(os.path.realpath(__file__)) + "/../../tests/ADECal.ics")
agenda = None

listeFrame = []

base = Base.Base()

app = QApplication(sys.argv)
w = QMainWindow(None)
ui = Ui_MainWindow()
ui.setupUi(w)
for i in range(base.formations.taille):
	ui.formations.addItem("")
	ui.formations.setItemText(i,base.formations.liste[i].chaine)
"""	
creneaux = agenda.recupererJour(2016,2,9)
for i in creneaux:
	f = monFrame(ui.un,"seance1")
	f.setUpMonFrame(i.horaire.debut,i.horaire.fin,"code",i.informations["SUMMARY"],i.informations["LOCATION"],"prof")
"""
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
	
	for i in listeFrame:
		i.close()
	
	jour = s.toPyDate()
	jourAvant = jour
	jourApres = jour
	listeJours = []
	listeJours.append(s.toString("dd/MM/yyyy"))
	listeCreneaux = []
	if agenda is not None:
			listeCreneaux.append(agenda.recupererJour(jour.year,jour.month,jour.day))
	
	for i in range(s.dayOfWeek()-1):
		jourAvant = jourAvant - datetime.timedelta(days=1)
		listeJours.insert(0,jourAvant.strftime('%d/%m/%Y'))
		if agenda is not None:
			listeCreneaux.insert(0,agenda.recupererJour(jourAvant.year,jourAvant.month,jourAvant.day))
	#fin for
	
	for i in range(7-s.dayOfWeek()):
		jourApres = jourApres + datetime.timedelta(days=1)
		listeJours.append(jourApres.strftime('%d/%m/%Y'))
		if agenda is not None:
			listeCreneaux.append(agenda.recupererJour(jourApres.year,jourApres.month,jourApres.day))
	#fin for
	
	ui.lundi.setText(listeJours[0]+" Lundi")
	ui.mardi.setText(listeJours[1]+" Mardi")
	ui.mercredi.setText(listeJours[2]+" Mercredi")
	ui.jeudi.setText(listeJours[3]+" Jeudi")
	ui.vendredi.setText(listeJours[4]+" Vendredi")
	
	
	if agenda is not None:
		for i in listeCreneaux[0]:
			f = monFrame(ui.un,"seance1")
			f.setUpMonFrame(i.horaire.debut,i.horaire.fin,"code",i.informations.get("SUMMARY", ""),i.informations.get("LOCATION", ""),"prof")
			f.show()
			listeFrame.append(f)
			
		for i in listeCreneaux[1]:
			f = monFrame(ui.deux,"seance1")
			f.setUpMonFrame(i.horaire.debut,i.horaire.fin,"code",i.informations.get("SUMMARY", ""),i.informations.get("LOCATION", ""),"prof")
			f.show()
			listeFrame.append(f)
			
		for i in listeCreneaux[2]:
			f = monFrame(ui.trois,"seance1")
			f.setUpMonFrame(i.horaire.debut,i.horaire.fin,"code",i.informations.get("SUMMARY", ""),i.informations.get("LOCATION", ""),"prof")
			f.show()
			listeFrame.append(f)
			
		for i in listeCreneaux[3]:
			f = monFrame(ui.quatre,"seance1")
			f.setUpMonFrame(i.horaire.debut,i.horaire.fin,"code",i.informations.get("SUMMARY", ""),i.informations.get("LOCATION", ""),"prof")
			f.show()
			listeFrame.append(f)
			
		for i in listeCreneaux[4]:
			f = monFrame(ui.cinq,"seance1")
			f.setUpMonFrame(i.horaire.debut,i.horaire.fin,"code",i.informations.get("SUMMARY", ""),i.informations.get("LOCATION", ""),"prof")
			f.show()
			listeFrame.append(f)
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

def quitter():
	# demander confirmation, gniagniagnia
	app.quit()
#quitter

def fermer():
	global agenda
	if agenda is not None:
		# demander à confirmer fermeture, blablabla
		ma.dechargerAgenda(agenda)
		agenda = None
		w.setWindowTitle("Organiseur")
		setDateStr()
	#if

def ouvrir():
	global agenda
	f = QtGui.QFileDialog.getOpenFileName(None, 'Ouvrir un fichier .ics', '', 'Fichiers (*.ics)')
	try:
		agenda = ma.chargerAgenda(f)
		w.setWindowTitle("Organiseur : " + agenda.nom)
		setDateStr()
	except ValueError:
		print("Il faut un fichier .ics")
	except IOError:
		print("Problème de lecture du fichier")
	#try
#ouvrir

def exporterTxt():
	if agenda is not None:
		f = QtGui.QFileDialog.getOpenFileName(None, 'Enregistrer au format texte', '', '')
		if not f == "":
			try:
				ma.exporterAuFormatTxt(agenda, f)
			except IOError:
				print("erreur avec le fichier " + str(f))
			#try
		#if
	#if
#exporterTxt

def nouveau():
	print("pas encore fait")
#nouveau

def enregistrerSous():
	if agenda is not None:
		f = QtGui.QFileDialog.getOpenFileName(None, 'Enregistrer sous...', '', '')
		if not f == "":
			try:
				ma.sauvegarderAgenda(agenda, f)
			except IOError:
				print("erreur avec le fichier " + str(f))
			#try
		#if
	#if
#enregistrerSous

def lancerFenetreDiff():
	fenetreDiff = MyWindow()
	fenetreDiff.show()
	
	def faireDiff():
		l = fenetreDiff.liste.files
		if len(l) != 2:
			#crier !
			fenetreDiff.close()
			return
		#if
		try:
			agenda1 = ma.chargerAgenda(fenetreDiff.liste.files[0])
			agenda2 = ma.chargerAgenda(fenetreDiff.liste.files[1])
		except ValueError:
			print("il faut des fichiers .ics")
		except IOError:
			print("erreur de lecture")
		#try
		d = Diff.Diff(agenda1, agenda2)
		d.comparer()
		ui.resultat = FenetreDiff(d)
		ui.resultat.show()
		ma.dechargerAgenda(agenda1)
		ma.dechargerAgenda(agenda2)
		fenetreDiff.close()
	#faireDiff
	
	fenetreDiff.ok.connect(fenetreDiff.ok,QtCore.SIGNAL("clicked()"), faireDiff)
	fenetreDiff.annuler.connect(fenetreDiff.annuler, QtCore.SIGNAL("clicked()"), fenetreDiff.close)
#lancerFenetreDiff

ui.actionDiff.triggered.connect(lancerFenetreDiff)


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
ui.actionQuitter.triggered.connect(quitter)
ui.actionOuvrir.triggered.connect(ouvrir)
ui.actionFermer.triggered.connect(fermer)
ui.actionNouveau.triggered.connect(nouveau)
ui.actionExporterTxt.triggered.connect(exporterTxt)
ui.actionEnregistrerSous.triggered.connect(enregistrerSous)
#ui.obligation.hide()
sys.exit(app.exec_())
