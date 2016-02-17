#!/usr/bin/python3
# -*-coding:utf-8 -*

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from vue.mainwindow import *
from modele.modele_API import *


if __name__ == "__main__":
	#instanciation du modèle
	modele = ModeleAgenda()
	
	# liens entre Vue/Modele
	
	#lancement de la vue
	app = QApplication(sys.argv)
	w = QMainWindow(None)
	ui = Ui_MainWindow()
	ui.setupUi(w)
	w.show()
	sys.exit(app.exec_())
#if
