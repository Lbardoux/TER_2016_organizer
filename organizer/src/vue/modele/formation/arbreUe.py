 # -*- coding: utf-8 -*-
 
import sys, os
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__))+"/../modele/formation/")
import Ue, Seance, Cm, Td, Tp, Examen, Autre 
from PyQt4 import QtCore, QtGui


try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)
		
class arbreUe(QtGui.QTreeWidget):
	def __init__(self, superieur, nom):
		super(arbreUe,self).__init__(superieur)
		self._nom = nom
		self.setGeometry(QtCore.QRect(10, 50, 291, 641))
		self.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.setFrameShape(QtGui.QFrame.StyledPanel)
		self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
		self.setTextElideMode(QtCore.Qt.ElideMiddle)
		self.setObjectName(_fromUtf8(nom))
		self._pile = [0,1,2,3,4]
	#fin __init__
	
	def premiereConfiguration(self, listeUe):
		for i in listeUe:
			item_0 = QtGui.QTreeWidgetItem(self)
			
			if not i.nombreCm == 0:
				item_1 = QtGui.QTreeWidgetItem(item_0)
				for j in i.listeCm:
					item_2 = QtGui.QTreeWidgetItem(item_1)
				#fin for
				self._cm = self._pile.pop(0)
			#fin if
			
			if not i.nombreTd == 0:
				item_1 = QtGui.QTreeWidgetItem(item_0)
				for j in i.listeTd:
					item_2 = QtGui.QTreeWidgetItem(item_1)
				#fin for
				self._td = self._pile.pop(0)
			#fin if
			
			if not i.nombreTp == 0:
				item_1 = QtGui.QTreeWidgetItem(item_0)
				for j in i.listeTp:
					item_2 = QtGui.QTreeWidgetItem(item_1)
				#fin for
				self._tp = self._pile.pop(0)
			#fin if
			
			if not i.nombreExamen == 0:
				item_1 = QtGui.QTreeWidgetItem(item_0)
				for j in i.listeExamen:
					item_2 = QtGui.QTreeWidgetItem(item_1)
				#fin for
				self._examen = self._pile.pop(0)
			#fin if
			
			if not i.nombreAutre == 0:
				item_1 = QtGui.QTreeWidgetItem(item_0)
				for j in i.listeAutre:
					item_2 = QtGui.QTreeWidgetItem(item_1)
				#fin for
				self._autre = self._pile.pop(0)
			#fin if
			
		#fin for
		self.raise_()
	#fin premiereConfiguration
	
	def secondeConfiguration(self, listeUe):
		self.headerItem().setText(0,"Liste des UEs")
		__sortingEnabled = self.isSortingEnabled()
		self.setSortingEnabled(False)
		compteur = 0
		for i in listeUe:
			self.topLevelItem(compteur).setText(0,_fromUtf8(i.code +" "+i.nom))
			
			if not i.nombreCm == 0:
				self.topLevelItem(compteur).child(self._cm).setText(0,"CMs")
				compteur2 = 0
				for j in i.listeCm:
					self.topLevelItem(compteur).child(self._cm).child(compteur2).setText(0,_fromUtf8("CM"+str(compteur2+1)))
					compteur2 += 1
				#fin for
			#fin if
			
			if not i.nombreTd == 0:
				self.topLevelItem(compteur).child(self._td).setText(0,"TDs")
				compteur2 = 0
				for j in i.listeTd:
					self.topLevelItem(compteur).child(self._td).child(compteur2).setText(0,_fromUtf8("TD"+str(compteur2+1)))
					compteur2 += 1
				#fin for
			#fin if
			
			if not i.nombreTp == 0:
				self.topLevelItem(compteur).child(self._tp).setText(0,"TPs")
				compteur2 = 0
				for j in i.listeTp:
					self.topLevelItem(compteur).child(self._tp).child(compteur2).setText(0,_fromUtf8("TP"+str(compteur2+1)))
					compteur2 += 1
				#fin for
			#fin if
			
			if not i.nombreExamen == 0:
				self.topLevelItem(compteur).child(self._examen).setText(0,"Examens")
				compteur2 = 0
				for j in i.listeExamen:
					self.topLevelItem(compteur).child(self._examen).child(compteur2).setText(0,_fromUtf8("Examen"+str(compteur2+1)))
					compteur2 += 1
				#fin for
			#fin if
			
			if not i.nombreAutre == 0:
				self.topLevelItem(compteur).child(self._autre).setText(0,"Autres")
				compteur2 = 0
				for j in i.listeAutre:
					self.topLevelItem(compteur).child(self._autre).child(compteur2).setText(0,_fromUtf8("Autre"+str(compteur2+1)))
					compteur2 += 1
				#fin for
			#fin if
			
			compteur += 1
		#fin for
		self.setSortingEnabled(__sortingEnabled)
	#fin secondeConfiguration	
#fin arbreUe
