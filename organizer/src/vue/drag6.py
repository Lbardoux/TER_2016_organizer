#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui

class MyListWidget(QListWidget):
	def __init__(self, parent):
		super(MyListWidget, self).__init__(parent)
		self.setAcceptDrops(True)
		self.setDragDropMode(QAbstractItemView.InternalMove)
		self.files = []
		self.count = 0
		self.parent = parent
	
	def dragEnterEvent(self, event):
		if event.mimeData().hasUrls():
			event.acceptProposedAction()
		else:
			super(MyListWidget, self).dragEnterEvent(event)

	def dragMoveEvent(self, event):
		super(MyListWidget, self).dragMoveEvent(event)
	
	def dropEvent(self, event):
		if event.mimeData().hasUrls() and self.count<2:
			for url in event.mimeData().urls():
				if self.count<2:
					self.addItem(url.path())
					self.files.append(url.path())
					self.count += 1
					if self.count == 2:
						self.parent.update()
				else:
					break
			event.acceptProposedAction()
		else:
			super(MyListWidget,self).dropEvent(event)

class MyWindow(QWidget):
	def __init__(self):
		super(MyWindow,self).__init__()
		self.setGeometry(100,100,400,200)
		self.setWindowTitle("Choisir les fichiers")
		self.ok = QtGui.QPushButton(self)
		self.ok.setObjectName("ok")
		self.ok.setText("Chercher les différences")
		self.ok.setEnabled(False)
		self.liste = MyListWidget(self)
		layout = QVBoxLayout(self)
		self.explication = QtGui.QLabel("Glisser-déposer 2 fichiers ics dans le rectange blanc", self)
		layout.addWidget(self.explication)
		layout.addWidget(self.liste)
		
		self.setLayout(layout)
		
		
		layout.addWidget(self.ok)
		self.annuler = QtGui.QPushButton(self)
		self.annuler.setObjectName("annuler")
		self.annuler.setText("annuler")
		layout.addWidget(self.annuler)
		
	def update(self):
		self.ok.setEnabled(True)



if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MyWindow()
	bouton = QtGui.QPushButton(None)
	bouton.setText("tester")
	def start_test():
		window.show()
	bouton.connect(bouton, QtCore.SIGNAL("clicked()"), start_test)
	bouton.show()
	def showdiff():
		for url in window.liste.files:
			print(url)
		window.close()
		app.quit()
	window.ok.connect(window.ok,QtCore.SIGNAL("clicked()"), showdiff)
	sys.exit(app.exec_())
