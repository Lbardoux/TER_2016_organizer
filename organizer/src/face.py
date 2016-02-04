#!/usr/bin/python
# -*-coding:utf-8 -*

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from mainwindow import *
from dialog import *
from seanceVue import *



app = QApplication(sys.argv)
w = QMainWindow(None)
ui = Ui_MainWindow()
ui.setupUi(w)

f = monFrame(ui.un,"seance1")
f.setUpMonFrame(0,9,"MIF15 Calculabilité","CM Recursivité","Nautibus C1","S.BRANDEL", "red")

f2 = monFrame(ui.deux,"seance2")
f2.setUpMonFrame(30,40,"MIF16 Compilation","TP Recursivité","Nautibus TP9","E.GUILLOT")
w.show()

d = QDialog(None)
dialog = Ui_Dialog()
dialog.setupUi(d)

def showDialog():
	d.show()
#fin showDialog

def closeDialog():
	d.close()
#fin showDialog

def setDateStr():
	s = ui.dateEdit.date()
	ui.lundi.setText(s.toString("dd/MM/yyyy"))
	ui.mardi.setText(s.toString("dd/MM/yyyy"))
	ui.mercredi.setText(s.toString("dd/MM/yyyy"))
	ui.jeudi.setText(s.toString("dd/MM/yyyy"))
	ui.vendredi.setText(s.toString("dd/MM/yyyy"))
#fin setDateStr

ui.dateEdit.setDate(QDate.currentDate())
ui.buttonCalendrier.connect(ui.buttonCalendrier,QtCore.SIGNAL("clicked()"),showDialog)
dialog.calendar.connect(dialog.calendar,QtCore.SIGNAL("clicked(QDate)"),ui.dateEdit,SLOT("setDate(QDate)") )
dialog.calendar.connect(dialog.calendar,QtCore.SIGNAL("clicked(QDate)"),closeDialog)
dialog.calendar.connect(dialog.calendar,QtCore.SIGNAL("clicked(QDate)"),setDateStr)

sys.exit(app.exec_())


