#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
# Created by: PyQt4 UI code generator 4.11.4
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s
	#_fromUtf8

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
	
	def viderColonnes(self):
		"""
		Va vider les colonnes afin de pouvoir actualiser l'affichage.
		@todo: trouver mieux que cette rustine.
		@param self: L'argument implicite.
		"""
		colonnes = (self.un, self.deux, self.trois, self.quatre, self.cinq)
		for c in colonnes:
			for i in [elt for elt in range(len(c.children())) if elt > 0]:
				c.children()[i].close()
			#for
		#for
	#viderColonnes
	
	
	def _initialiserMenuFichier(self, MainWindow):
		"""
		Effectue toutes les actions pour initialiser le menu déroulant "Fichier".
		@param self: L'argument implicite.
		@type MainWindow: QApplication
		@param MainWindow: La fenetre parente de Ui_MainWindow
		"""
		self.menuFichier = self.menubar.addMenu("&Fichier")
		self.menuFichier.setTitle(_translate("MainWindow", "&Fichier", None))
		# menu Fichier -> Nouveau
		self.actionNouveau = QtGui.QAction(MainWindow)
		self.actionNouveau.setObjectName(_fromUtf8("actionNouveau"))
		self.actionNouveau.setText(_translate("MainWindow", "Nouveau", None))
		self.actionNouveau.setShortcut("Ctrl+N")
		self.actionNouveau.setStatusTip("Créer un nouveau calendrier")
		self.menuFichier.addAction(self.actionNouveau)
		self.actionNouveau.setEnabled(False)
		# menu Fichier -> Ouvrir
		self.actionOuvrir = QtGui.QAction(MainWindow)
		self.actionOuvrir.setObjectName(_fromUtf8("actionOuvrir"))
		self.actionOuvrir.setText(_translate("MainWindow", "Ouvrir...", None))
		self.menuFichier.addAction(self.actionOuvrir)

		# menu Fichier -> ------
		self.menuFichier.addSeparator()

		# menu Fichier -> Enregistrer
		self.actionEnregistrer = QtGui.QAction(MainWindow)
		self.actionEnregistrer.setObjectName(_fromUtf8("actionEnregistrer"))
		self.actionEnregistrer.setText(_translate("MainWindow", "Enregistrer", None))
		self.menuFichier.addAction(self.actionEnregistrer)
		self.actionEnregistrer.setEnabled(False)
		
		# menu Fichier -> Enregistrer sous
		self.actionEnregistrerSous = QtGui.QAction(MainWindow)
		self.actionEnregistrerSous.setObjectName(_fromUtf8("actionEnregistrerSous"))
		self.actionEnregistrerSous.setText(_translate("MainWindow", "Enregistrer sous...", None))
		self.menuFichier.addAction(self.actionEnregistrerSous)
		
		# menu Fichier -> Exporter ->
		self.menuExporter = self.menuFichier.addMenu("Exporter")

		# menu Fichier -> Exporter -> au format txt
		self.actionExporterTxt = QtGui.QAction(MainWindow)
		self.actionExporterTxt.setObjectName(_fromUtf8("actionExporterTxt"))
		self.actionExporterTxt.setText(_translate("MainWindow", "Au format texte...", None))
		self.menuExporter.addAction(self.actionExporterTxt)
		
		# menu Fichier -> ------
		self.menuFichier.addSeparator()
		
		# menu Fichier -> Fermer
		self.actionFermer = QtGui.QAction(MainWindow)
		self.actionFermer.setObjectName(_fromUtf8("actionFermer"))
		self.actionFermer.setText(_translate("MainWindow", "Fermer", None))
		self.menuFichier.addAction(self.actionFermer)

		# menu Fichier -> Quitter
		self.actionQuitter = QtGui.QAction(MainWindow)
		self.actionQuitter.setObjectName(_fromUtf8("actionQuitter"))
		self.actionQuitter.setText(_translate("MainWindow", "Quitter", None))
		self.actionQuitter.setShortcut("Ctrl+Q")
		self.actionQuitter.setStatusTip("Quitter l'application")
		self.menuFichier.addAction(self.actionQuitter)
	#_initialiserMenuFichier
	
	
	def _initialiserMenuEdition(self, MainWindow):
		"""
		Effectue toutes les actions pour initialiser le menu déroulant "Edition".
		@param self: L'argument implicite.
		@type MainWindow: QApplication
		@param MainWindow: La fenetre parente de Ui_MainWindow
		"""
		self.menuEdition = self.menubar.addMenu("&Edition")
		self.menuEdition.setTitle(_translate("MainWindow", "&Edition", None))
		# menu Edition -> annuler
		self.actionAnnuler = QtGui.QAction(MainWindow)
		self.actionAnnuler.setObjectName(_fromUtf8("actionAnnuler"))
		self.actionAnnuler.setText(_translate("MainWindow", "Annuler", None))
		self.actionAnnuler.setShortcut("Ctrl+Z")
		self.actionAnnuler.setStatusTip("Annuler la précédente action")
		self.menuEdition.addAction(self.actionAnnuler)
		# A retirer quand ça sera pret
		self.actionAnnuler.setEnabled(False)
		# menu Edition -> refaire
		self.actionRefaire = QtGui.QAction(MainWindow)
		self.actionRefaire.setObjectName(_fromUtf8("actionRefaire"))
		self.actionRefaire.setText(_translate("MainWindow", "Refaire", None))
		self.actionRefaire.setShortcut("Ctrl+Y")
		self.actionRefaire.setStatusTip("refaire la précédente action")
		self.menuEdition.addAction(self.actionRefaire)
		# A retirer quand ça sera pret
		self.actionRefaire.setEnabled(False)
	#_initialiserMenuEdition
	
	
	def _initialiserMenuOutils(self, MainWindow):
		"""
		Effectue toutes les actions pour initialiser le menu déroulant "Outils".
		@param self: L'argument implicite.
		@type MainWindow: QApplication
		@param MainWindow: La fenetre parente de Ui_MainWindow
		"""
		self.menuOutils = self.menubar.addMenu("&Outils")
		self.menuOutils.setTitle(_translate("MainWindow", "&Outils", None))

		# menu Outils -> diff
		self.actionDiff = QtGui.QAction(MainWindow)
		self.actionDiff.setObjectName(_fromUtf8("actionDiff"))
		self.actionDiff.setText(_translate("MainWindow", "Diff...", None))
		self.actionDiff.setStatusTip("Recherche des différences entre deux agendas")
		self.menuOutils.addAction(self.actionDiff)
	#_initialiserMenuOutils
	
	
	def _initialiserMenuAide(self, MainWindow):
		"""
		Effectue toutes les actions pour initialiser le menu déroulant "Aide".
		@param self: L'argument implicite.
		@type MainWindow: QApplication
		@param MainWindow: La fenetre parente de Ui_MainWindow
		"""
	#_initialiserMenuAide
	
	def _initialiserColonnes(self):
		"""
		Permet d'initialiser les colonees de l'affichage.
		@param self: L'argument implicite.
		"""
		self.jours = QtGui.QFrame(self.Visualisation)
		self.jours.setGeometry(QtCore.QRect(10, 30, 1001, 680))
		self.jours.setStyleSheet(_fromUtf8("#jours>.QFrame{\n"
			"	border-style: outset;\n"
			"	border-width: 2px;\n"
			"	border-color: black;\n"
			"	background-color: white;\n"
			"}\n"
			"#jours>.QFrame>.QLabel{\n"
			"	qproperty-alignment: AlignCenter;\n"
			"	font: 75 11pt \"Waree\";\n"
			"	background-color: black;\n"
			"	color:white;\n"
			"}"
		))
		self.jours.setObjectName(_fromUtf8("jours"))
		self.horizontalLayout_5 = QtGui.QHBoxLayout(self.jours)
		self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
		self.un = QtGui.QFrame(self.jours)
		self.un.setStyleSheet(_fromUtf8(""))
		self.un.setFrameShape(QtGui.QFrame.StyledPanel)
		self.un.setFrameShadow(QtGui.QFrame.Raised)
		self.un.setObjectName(_fromUtf8("un"))
		self.lundi = QtGui.QLabel(self.un)
		self.lundi.setGeometry(QtCore.QRect(0, 0, 191, 30))
		self.lundi.setObjectName(_fromUtf8("lundi"))
		self.horizontalLayout_5.addWidget(self.un)
		self.deux = QtGui.QFrame(self.jours)
		self.deux.setStyleSheet(_fromUtf8(""))
		self.deux.setFrameShape(QtGui.QFrame.StyledPanel)
		self.deux.setFrameShadow(QtGui.QFrame.Raised)
		self.deux.setObjectName(_fromUtf8("deux"))
		self.mardi = QtGui.QLabel(self.deux)
		self.mardi.setGeometry(QtCore.QRect(0, 0, 191, 30))
		self.mardi.setObjectName(_fromUtf8("mardi"))
		self.horizontalLayout_5.addWidget(self.deux)
		self.trois = QtGui.QFrame(self.jours)
		self.trois.setStyleSheet(_fromUtf8(""))
		self.trois.setFrameShape(QtGui.QFrame.StyledPanel)
		self.trois.setFrameShadow(QtGui.QFrame.Raised)
		self.trois.setObjectName(_fromUtf8("trois"))
		self.mercredi = QtGui.QLabel(self.trois)
		self.mercredi.setGeometry(QtCore.QRect(0, 0, 191, 30))
		self.mercredi.setObjectName(_fromUtf8("mercredi"))
		self.horizontalLayout_5.addWidget(self.trois)
		self.quatre = QtGui.QFrame(self.jours)
		self.quatre.setStyleSheet(_fromUtf8(""))
		self.quatre.setFrameShape(QtGui.QFrame.StyledPanel)
		self.quatre.setFrameShadow(QtGui.QFrame.Raised)
		self.quatre.setObjectName(_fromUtf8("quatre"))
		self.jeudi = QtGui.QLabel(self.quatre)
		self.jeudi.setGeometry(QtCore.QRect(0, -1, 191, 31))
		self.jeudi.setObjectName(_fromUtf8("jeudi"))
		self.horizontalLayout_5.addWidget(self.quatre)
		self.cinq = QtGui.QFrame(self.jours)
		self.cinq.setStyleSheet(_fromUtf8(""))
		self.cinq.setFrameShape(QtGui.QFrame.StyledPanel)
		self.cinq.setFrameShadow(QtGui.QFrame.Raised)
		self.cinq.setObjectName(_fromUtf8("cinq"))
		self.vendredi = QtGui.QLabel(self.cinq)
		self.vendredi.setGeometry(QtCore.QRect(0, 0, 191, 31))
		self.vendredi.setObjectName(_fromUtf8("vendredi"))
		self.horizontalLayout_5.addWidget(self.cinq)
	#_initialiserColonnes
		


	def setupUi(self, MainWindow):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(1024, 768)
		MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
		MainWindow.setMaximumSize(QtCore.QSize(1024, 768))
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.tabWidget = QtGui.QTabWidget(self.centralwidget)
		self.tabWidget.setGeometry(QtCore.QRect(0, 10, 1024, 751))
		self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
		self.listeUe = QtGui.QWidget()
		self.listeUe.setObjectName(_fromUtf8("listeUe"))
		self.formLayoutWidget_4 = QtGui.QWidget(self.listeUe)
		self.formLayoutWidget_4.setGeometry(QtCore.QRect(350, 140, 181, 136))
		self.formLayoutWidget_4.setObjectName(_fromUtf8("formLayoutWidget_4"))
		self.formLayout_4 = QtGui.QFormLayout(self.formLayoutWidget_4)
		self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
		self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
		self.nomTPLabel_3 = QtGui.QLabel(self.formLayoutWidget_4)
		self.nomTPLabel_3.setObjectName(_fromUtf8("nomTPLabel_3"))
		self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.nomTPLabel_3)
		self.nomTPLineEdit_3 = QtGui.QLineEdit(self.formLayoutWidget_4)
		self.nomTPLineEdit_3.setObjectName(_fromUtf8("nomTPLineEdit_3"))
		self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.nomTPLineEdit_3)
		self.durELabel_3 = QtGui.QLabel(self.formLayoutWidget_4)
		self.durELabel_3.setObjectName(_fromUtf8("durELabel_3"))
		self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.durELabel_3)
		self.durESpinBox_3 = QtGui.QSpinBox(self.formLayoutWidget_4)
		self.durESpinBox_3.setObjectName(_fromUtf8("durESpinBox_3"))
		self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.durESpinBox_3)
		self.pushButton_4 = QtGui.QPushButton(self.formLayoutWidget_4)
		self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
		self.formLayout_4.setWidget(3, QtGui.QFormLayout.FieldRole, self.pushButton_4)
		self.enseignantComboBox = QtGui.QComboBox(self.formLayoutWidget_4)
		self.enseignantComboBox.setObjectName(_fromUtf8("enseignantComboBox"))
		self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.enseignantComboBox)
		self.enseignantLabel = QtGui.QLabel(self.formLayoutWidget_4)
		self.enseignantLabel.setObjectName(_fromUtf8("enseignantLabel"))
		self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.enseignantLabel)
		self.ajout = QtGui.QPushButton(self.listeUe)
		self.ajout.setGeometry(QtCore.QRect(100, 10, 100, 29))
		self.ajout.setObjectName(_fromUtf8("ajout"))
		#self.tabWidget.addTab(self.listeUe, _fromUtf8(""))
		self.Contraintes = QtGui.QWidget()
		self.Contraintes.setObjectName(_fromUtf8("Contraintes"))
		self.horizontalLayoutWidget = QtGui.QWidget(self.Contraintes)
		self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1021, 61))
		self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
		self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
		self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
		self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
		self.horizontalLayout.setSpacing(0)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.obligation = QtGui.QToolButton(self.horizontalLayoutWidget)
		self.obligation.setMinimumSize(QtCore.QSize(100, 50))
		self.obligation.setObjectName(_fromUtf8("obligation"))
		self.horizontalLayout.addWidget(self.obligation)
		self.blocage = QtGui.QToolButton(self.horizontalLayoutWidget)
		self.blocage.setMinimumSize(QtCore.QSize(100, 50))
		self.blocage.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
		self.blocage.setObjectName(_fromUtf8("blocage"))
		self.horizontalLayout.addWidget(self.blocage)
		self.datelimite = QtGui.QToolButton(self.horizontalLayoutWidget)
		self.datelimite.setMinimumSize(QtCore.QSize(100, 50))
		self.datelimite.setObjectName(_fromUtf8("datelimite"))
		self.horizontalLayout.addWidget(self.datelimite)
		self.precedence = QtGui.QToolButton(self.horizontalLayoutWidget)
		self.precedence.setMinimumSize(QtCore.QSize(100, 50))
		self.precedence.setObjectName(_fromUtf8("precedence"))
		self.horizontalLayout.addWidget(self.precedence)
		self.frame = QtGui.QFrame(self.Contraintes)
		self.frame.setGeometry(QtCore.QRect(20, 80, 981, 101))
		self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtGui.QFrame.Raised)
		self.frame.setObjectName(_fromUtf8("frame"))
		self.pushButton = QtGui.QPushButton(self.frame)
		self.pushButton.setGeometry(QtCore.QRect(640, 40, 100, 29))
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.dateTimeEdit = QtGui.QDateTimeEdit(self.frame)
		self.dateTimeEdit.setGeometry(QtCore.QRect(30, 40, 194, 27))
		self.dateTimeEdit.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
		self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
		self.dateTimeEdit_2 = QtGui.QDateTimeEdit(self.frame)
		self.dateTimeEdit_2.setGeometry(QtCore.QRect(350, 40, 194, 27))
		self.dateTimeEdit_2.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
		self.dateTimeEdit_2.setObjectName(_fromUtf8("dateTimeEdit_2"))
		self.layoutWidget = QtGui.QWidget(self.Contraintes)
		self.layoutWidget.setGeometry(QtCore.QRect(-1, 660, 1021, 41))
		self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
		self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget)
		self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
		spacerItem = QtGui.QSpacerItem(58, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout_4.addItem(spacerItem)
		self.horizontalLayout_3 = QtGui.QHBoxLayout()
		self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
		self.pushButton_5 = QtGui.QPushButton(self.layoutWidget)
		self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
		self.horizontalLayout_3.addWidget(self.pushButton_5)
		self.pushButton_3 = QtGui.QPushButton(self.layoutWidget)
		self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
		self.horizontalLayout_3.addWidget(self.pushButton_3)
		self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
		spacerItem1 = QtGui.QSpacerItem(108, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout_4.addItem(spacerItem1)
		self.listWidget = QtGui.QListWidget(self.Contraintes)
		self.listWidget.setGeometry(QtCore.QRect(15, 191, 991, 461))
		self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.listWidget.setObjectName(_fromUtf8("listWidget"))
		item = QtGui.QListWidgetItem()
		self.listWidget.addItem(item)
		item = QtGui.QListWidgetItem()
		self.listWidget.addItem(item)
		item = QtGui.QListWidgetItem()
		self.listWidget.addItem(item)
		item = QtGui.QListWidgetItem()
		self.listWidget.addItem(item)
		item = QtGui.QListWidgetItem()
		self.listWidget.addItem(item)
		#self.tabWidget.addTab(self.Contraintes, _fromUtf8(""))
		self.Visualisation = QtGui.QWidget()
		self.Visualisation.setObjectName(_fromUtf8("Visualisation"))
		self._initialiserColonnes()
		self.buttonCalendrier = QtGui.QPushButton(self.Visualisation)
		self.buttonCalendrier.setGeometry(QtCore.QRect(250, 6, 21, 28))
		self.buttonCalendrier.setObjectName(_fromUtf8("buttonCalendrier"))
		self.layoutWidget_2 = QtGui.QWidget(self.Visualisation)
		self.layoutWidget_2.setGeometry(QtCore.QRect(20, -5, 601, 51))
		self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
		self.horizontalLayout_12 = QtGui.QHBoxLayout(self.layoutWidget_2)
		self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
		self.label_12 = QtGui.QLabel(self.layoutWidget_2)
		self.label_12.setObjectName(_fromUtf8("label_12"))
		self.horizontalLayout_12.addWidget(self.label_12)
		self.dateEdit = QtGui.QDateEdit(self.layoutWidget_2)
		self.dateEdit.setMinimumSize(QtCore.QSize(107, 30))
		self.dateEdit.setMouseTracking(False)
		self.dateEdit.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
		self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
		self.horizontalLayout_12.addWidget(self.dateEdit)
		spacerItem2 = QtGui.QSpacerItem(17, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout_12.addItem(spacerItem2)
		self.fleche1 = QtGui.QToolButton(self.layoutWidget_2)
		self.fleche1.setMinimumSize(QtCore.QSize(30, 30))
		self.fleche1.setMaximumSize(QtCore.QSize(30, 30))
		self.fleche1.setStyleSheet(_fromUtf8(""))
		self.fleche1.setObjectName(_fromUtf8("fleche1"))
		self.horizontalLayout_12.addWidget(self.fleche1)
		spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout_12.addItem(spacerItem3)
		self.fleche2 = QtGui.QToolButton(self.layoutWidget_2)
		self.fleche2.setMinimumSize(QtCore.QSize(30, 30))
		self.fleche2.setMaximumSize(QtCore.QSize(30, 30))
		self.fleche2.setStyleSheet(_fromUtf8(""))
		self.fleche2.setObjectName(_fromUtf8("fleche2"))
		self.horizontalLayout_12.addWidget(self.fleche2)
		self.jours.raise_()
		self.layoutWidget_2.raise_()
		self.buttonCalendrier.raise_()
		self.tabWidget.addTab(self.Visualisation, _fromUtf8(""))
		self.tabWidget.addTab(self.listeUe, _fromUtf8(""))
		self.tabWidget.addTab(self.Contraintes, _fromUtf8(""))
		
		self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
		self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(720, 0, 281, 41))
		self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
		self.horizontalLayout_7 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
		self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
		self.label_8 = QtGui.QLabel(self.horizontalLayoutWidget_2)
		self.label_8.setMaximumSize(QtCore.QSize(80, 16777215))
		self.label_8.setObjectName(_fromUtf8("label_8"))
		self.horizontalLayout_7.addWidget(self.label_8)
		self.formations = QtGui.QComboBox(self.horizontalLayoutWidget_2)
		self.formations.setObjectName(_fromUtf8("formations"))
		self.horizontalLayout_7.addWidget(self.formations)
		MainWindow.setCentralWidget(self.centralwidget)
		
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 25))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		
		#self.menuFichier = QtGui.QMenu(self.menubar)
		
		
		#self.menuFichier.setObjectName(_fromUtf8("menuFichier"))
		#self.menuEdition = QtGui.QMenu(self.menubar)
		#self.menuEdition.setObjectName(_fromUtf8("menuEdition"))
		self.menuAide = QtGui.QMenu(self.menubar)
		self.menuAide.setObjectName(_fromUtf8("menuAide"))
		
		
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)
		self.actionCsqck = QtGui.QAction(MainWindow)
		self.actionCsqck.setObjectName(_fromUtf8("actionCsqck"))
		self.actionSqdjkqd = QtGui.QAction(MainWindow)
		self.actionSqdjkqd.setObjectName(_fromUtf8("actionSqdjkqd"))
		self.actionSdqjkk = QtGui.QAction(MainWindow)
		self.actionSdqjkk.setObjectName(_fromUtf8("actionSdqjkk"))
		self.actionJhsdfcsjkqhf = QtGui.QAction(MainWindow)
		self.actionJhsdfcsjkqhf.setObjectName(_fromUtf8("actionJhsdfcsjkqhf"))
		self.actionSqjkfjqs = QtGui.QAction(MainWindow)
		self.actionSqjkfjqs.setObjectName(_fromUtf8("actionSqjkfjqs"))
		self.actionDlkqjfklqdf = QtGui.QAction(MainWindow)
		self.actionDlkqjfklqdf.setObjectName(_fromUtf8("actionDlkqjfklqdf"))
		self.actionSjqflkfnc = QtGui.QAction(MainWindow)
		self.actionSjqflkfnc.setObjectName(_fromUtf8("actionSjqflkfnc"))
		self.actionDdsnfn = QtGui.QAction(MainWindow)
		self.actionDdsnfn.setObjectName(_fromUtf8("actionDdsnfn"))
		
		MainWindow.setMenuBar(self.menubar)
		
		self._initialiserMenuFichier(MainWindow)
		self._initialiserMenuEdition(MainWindow)
		self._initialiserMenuOutils(MainWindow)
		self._initialiserMenuAide(MainWindow)
		
		#self.menubar.addAction(self.menuEdition.menuAction())
		self.menubar.addAction(self.menuAide.menuAction())

		self.retranslateUi(MainWindow)
		self.tabWidget.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "Organiseur", None))
		self.nomTPLabel_3.setText(_translate("MainWindow", "Nom TD", None))
		self.durELabel_3.setText(_translate("MainWindow", "Durée ", None))
		self.pushButton_4.setText(_translate("MainWindow", "Valider", None))
		self.enseignantLabel.setText(_translate("MainWindow", "Enseignant", None))
		self.ajout.setText(_translate("MainWindow", "Nouvelle Ue", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.listeUe), _translate("MainWindow", "Liste des UEs", None))
		self.obligation.setText(_translate("MainWindow", "Obligation", None))
		self.blocage.setText(_translate("MainWindow", "Blocage", None))
		self.datelimite.setText(_translate("MainWindow", "Date limite", None))
		self.precedence.setText(_translate("MainWindow", "Precedence", None))
		self.pushButton.setText(_translate("MainWindow", "PushButton", None))
		self.dateTimeEdit.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy HH:mm", None))
		self.dateTimeEdit_2.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy HH:mm", None))
		self.pushButton_5.setText(_translate("MainWindow", "Annuler", None))
		self.pushButton_3.setText(_translate("MainWindow", "Générer", None))
		__sortingEnabled = self.listWidget.isSortingEnabled()
		self.listWidget.setSortingEnabled(False)
		item = self.listWidget.item(0)
		item.setText(_translate("MainWindow", "gfdfsd", None))
		item = self.listWidget.item(1)
		item.setText(_translate("MainWindow", "cdcdc", None))
		item = self.listWidget.item(2)
		item.setText(_translate("MainWindow", "cdcdc", None))
		item = self.listWidget.item(3)
		item.setText(_translate("MainWindow", "gfdvdf", None))
		item = self.listWidget.item(4)
		item.setText(_translate("MainWindow", "vdsvsdvsv", None))
		self.listWidget.setSortingEnabled(__sortingEnabled)
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.Contraintes), _translate("MainWindow", "Contraintes", None))
		self.lundi.setText(_translate("MainWindow", "DATE", None))
		self.mardi.setText(_translate("MainWindow", "DATE", None))
		self.mercredi.setText(_translate("MainWindow", "DATE", None))
		self.jeudi.setText(_translate("MainWindow", "DATE", None))
		self.vendredi.setText(_translate("MainWindow", "DATE", None))
		self.buttonCalendrier.setToolTip(_translate("MainWindow", "<html><head/><body><p>Ouvrir le calendrier</p></body></html>", None))
		self.buttonCalendrier.setText(_translate("MainWindow", "#", None))
		self.label_12.setText(_translate("MainWindow", "Selectionnez date : ", None))
		self.dateEdit.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy", None))
		self.fleche1.setToolTip(_translate("MainWindow", "<html><head/><body><p>La semaine d\'avant</p></body></html>", None))
		self.fleche1.setText(_translate("MainWindow", "<", None))
		self.fleche2.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">La semaine d\'après</span></p></body></html>", None))
		self.fleche2.setText(_translate("MainWindow", ">", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.Visualisation), _translate("MainWindow", "Visualisation", None))
		self.label_8.setText(_translate("MainWindow", "Formation : ", None))
		self.menuFichier.setTitle(_translate("MainWindow", "&Fichier", None))
		self.menuEdition.setTitle(_translate("MainWindow", "&Edition", None))
		self.menuAide.setTitle(_translate("MainWindow", "&Aide", None))
		self.actionCsqck.setText(_translate("MainWindow", "csqck", None))
		self.actionSqdjkqd.setText(_translate("MainWindow", "sqdjkqd", None))
		self.actionSdqjkk.setText(_translate("MainWindow", "sdqjkk", None))
		self.actionJhsdfcsjkqhf.setText(_translate("MainWindow", "jhsdfcsjkqhf", None))
		self.actionSqjkfjqs.setText(_translate("MainWindow", "sqjkfjqs", None))
		self.actionDlkqjfklqdf.setText(_translate("MainWindow", "dlkqjfklqdf", None))
		self.actionSjqflkfnc.setText(_translate("MainWindow", "sjqflkfnc", None))
		self.actionDdsnfn.setText(_translate("MainWindow", "ddsnfn", None))
