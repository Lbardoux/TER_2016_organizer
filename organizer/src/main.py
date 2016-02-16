#!/usr/bin/python3
# -*-coding:utf-8 -*

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from vue.mainwindow import *

class CSP_organizer:
	"""
	La classe principale du programme
	@author: Laurent Bardoux p1108365
	@author: Zhuying Liu     p1306849
	"""
	
	def __init__(self):
		"""
		Cette fonction prépare l'application
		"""
	#fin __init__
	
	
	def start(self):
		"""
		Lancement de l'application via l'interface graphique
		"""
		
	#fin start
	
#fin CSP_organizer



if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = QMainWindow(None)
	ui = Ui_MainWindow()
	ui.setupUi(w)
	w.show()
	sys.exit(app.exec_())
#fin if
