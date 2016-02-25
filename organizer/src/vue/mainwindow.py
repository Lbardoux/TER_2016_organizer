# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oo.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1024, 768)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 768))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(400, 0, 221, 48))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setSpacing(150)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.fleche1 = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.fleche1.setMinimumSize(QtCore.QSize(30, 30))
        self.fleche1.setMaximumSize(QtCore.QSize(30, 30))
        self.fleche1.setStyleSheet(_fromUtf8("#fleche1{\n"
			"background-color: grey;\n"
			"font: 75 16pt \"Waree\";\n"
			"color: white;\n"
			"}\n"
			""
		))
        self.fleche1.setObjectName(_fromUtf8("fleche1"))
        self.horizontalLayout_2.addWidget(self.fleche1)
        self.fleche2 = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.fleche2.setMinimumSize(QtCore.QSize(30, 30))
        self.fleche2.setMaximumSize(QtCore.QSize(30, 30))
        self.fleche2.setStyleSheet(_fromUtf8("#fleche2{\n"
			"background-color: grey;\n"
			"font: 75 16pt \"Waree\";\n"
			"color: white;\n"
			"}\n"
			""
		))
        self.fleche2.setObjectName(_fromUtf8("fleche2"))
        self.horizontalLayout_2.addWidget(self.fleche2)
        self.buttonCalendrier = QtGui.QPushButton(self.centralwidget)
        self.buttonCalendrier.setGeometry(QtCore.QRect(300, 11, 21, 28))
        self.buttonCalendrier.setObjectName(_fromUtf8("buttonCalendrier"))
        self.jours = QtGui.QFrame(self.centralwidget)
        self.jours.setGeometry(QtCore.QRect(10, 40, 1001, 680))
        self.jours.setStyleSheet(_fromUtf8("#jours>.QFrame{\n"
			"        border-style: outset;\n"
			"        border-width: 2px;\n"
			"    border-color: black;\n"
			"    background-color: white;\n"
			"}\n"
			"#jours>.QFrame>.QLabel{\n"
			"    qproperty-alignment: AlignCenter;\n"
			"    font: 75 11pt \"Waree\";\n"
			"    background-color: black;\n"
			"    color:white;\n"
			"}"
		))
        self.jours.setObjectName(_fromUtf8("jours"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.jours)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.un = QtGui.QFrame(self.jours)
        self.un.setStyleSheet(_fromUtf8(""))
        self.un.setFrameShape(QtGui.QFrame.StyledPanel)
        self.un.setFrameShadow(QtGui.QFrame.Raised)
        self.un.setObjectName(_fromUtf8("un"))
        self.lundi = QtGui.QLabel(self.un)
        self.lundi.setGeometry(QtCore.QRect(0, 0, 191, 30))
        self.lundi.setObjectName(_fromUtf8("lundi"))
        self.lundi.raise_()
        self.horizontalLayout.addWidget(self.un)
        self.deux = QtGui.QFrame(self.jours)
        self.deux.setStyleSheet(_fromUtf8(""))
        self.deux.setFrameShape(QtGui.QFrame.StyledPanel)
        self.deux.setFrameShadow(QtGui.QFrame.Raised)
        self.deux.setObjectName(_fromUtf8("deux"))
        self.mardi = QtGui.QLabel(self.deux)
        self.mardi.setGeometry(QtCore.QRect(0, 0, 191, 30))
        self.mardi.setObjectName(_fromUtf8("mardi"))
        self.mardi.raise_()
        self.horizontalLayout.addWidget(self.deux)
        self.trois = QtGui.QFrame(self.jours)
        self.trois.setStyleSheet(_fromUtf8(""))
        self.trois.setFrameShape(QtGui.QFrame.StyledPanel)
        self.trois.setFrameShadow(QtGui.QFrame.Raised)
        self.trois.setObjectName(_fromUtf8("trois"))
        self.mercredi = QtGui.QLabel(self.trois)
        self.mercredi.setGeometry(QtCore.QRect(0, 0, 191, 30))
        self.mercredi.setObjectName(_fromUtf8("mercredi"))
        self.mercredi.raise_()
        self.deux.raise_()
        self.deux.raise_()
        self.horizontalLayout.addWidget(self.trois)
        self.quatre = QtGui.QFrame(self.jours)
        self.quatre.setStyleSheet(_fromUtf8(""))
        self.quatre.setFrameShape(QtGui.QFrame.StyledPanel)
        self.quatre.setFrameShadow(QtGui.QFrame.Raised)
        self.quatre.setObjectName(_fromUtf8("quatre"))
        self.jeudi = QtGui.QLabel(self.quatre)
        self.jeudi.setGeometry(QtCore.QRect(0, -1, 191, 31))
        self.jeudi.setObjectName(_fromUtf8("jeudi"))
        self.jeudi.raise_()
        self.horizontalLayout.addWidget(self.quatre)
        self.cinq = QtGui.QFrame(self.jours)
        self.cinq.setStyleSheet(_fromUtf8(""))
        self.cinq.setFrameShape(QtGui.QFrame.StyledPanel)
        self.cinq.setFrameShadow(QtGui.QFrame.Raised)
        self.cinq.setObjectName(_fromUtf8("cinq"))
        self.vendredi = QtGui.QLabel(self.cinq)
        self.vendredi.setGeometry(QtCore.QRect(0, 0, 191, 31))
        self.vendredi.setObjectName(_fromUtf8("vendredi"))
        self.horizontalLayout.addWidget(self.cinq)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, 0, 271, 51))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.dateEdit = QtGui.QDateEdit(self.widget)
        self.dateEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.dateEdit.setMouseTracking(False)
        self.dateEdit.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.horizontalLayout_3.addWidget(self.dateEdit)
        self.un.raise_()
        self.deux.raise_()
        self.quatre.raise_()
        self.cinq.raise_()
        self.trois.raise_()
        self.deux.raise_()
        self.un.raise_()
        self.fleche1.raise_()
        self.horizontalLayoutWidget.raise_()
        self.label_6.raise_()
        self.dateEdit.raise_()
        self.buttonCalendrier.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        MainWindow.menuBar().show()
        #self.menubar = QtGui.QMenuBar(MainWindow)
        #self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 25))
        ##self.menuCoucou = QtGui.QMenu(self.menubar)
        #self.menuCoucou = self.menubar.addMenu("&Fichier")
        #self.menuCoucou.setObjectName(_fromUtf8("&Fichier"))
        #self.menubar.setObjectName(_fromUtf8("menubar"))
        #self.menuKlklk = QtGui.QMenu(self.menubar)
        #self.menuKlklk.setObjectName(_fromUtf8("menuKlklk"))
        #self.menuHklhlhkl = QtGui.QMenu(self.menubar)
        #self.menuHklhlhkl.setObjectName(_fromUtf8("menuHklhlhkl"))
        #self.menuGjhg = QtGui.QMenu(self.menubar)
        #self.menuGjhg.setObjectName(_fromUtf8("menuGjhg"))
        #MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionImporter = QtGui.QAction(MainWindow)
        self.actionImporter.setObjectName(_fromUtf8("actionImporter"))
        self.actionExporter = QtGui.QAction(MainWindow)
        self.actionExporter.setObjectName(_fromUtf8("actionExporter"))
        self.actionModifier = QtGui.QAction(MainWindow)
        self.actionModifier.setObjectName(_fromUtf8("actionModifier"))
        #self.menuKlklk.addAction(self.actionImporter)
        #self.menuKlklk.addAction(self.actionExporter)
        #self.menuHklhlhkl.addAction(self.actionModifier)
        #self.menubar.addAction(self.menuKlklk.menuAction())
        #self.menubar.addAction(self.menuHklhlhkl.menuAction())
        #self.menubar.addAction(self.menuGjhg.menuAction())

        #self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Organizer", "Organizer", None))
        self.fleche1.setText(_translate("MainWindow", "<", None))
        self.fleche2.setText(_translate("MainWindow", ">", None))
        self.buttonCalendrier.setText(_translate("MainWindow", "#", None))
        self.lundi.setText(_translate("MainWindow", "DATE", None))
        self.mardi.setText(_translate("MainWindow", "DATE", None))
        self.mercredi.setText(_translate("MainWindow", "DATE", None))
        self.jeudi.setText(_translate("MainWindow", "DATE", None))
        self.vendredi.setText(_translate("MainWindow", "DATE", None))
        self.label_6.setText(_translate("MainWindow", "Selectionnez date : ", None))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy", None))
        #self.menuKlklk.setTitle(_translate("MainWindow", "Fichier", None))
        #self.menuHklhlhkl.setTitle(_translate("MainWindow", "Editer", None))
        #self.menuGjhg.setTitle(_translate("MainWindow", "gjhg", None))
        self.actionImporter.setText(_translate("MainWindow", "Importer", None))
        self.actionExporter.setText(_translate("MainWindow", "Exporter", None))
        self.actionModifier.setText(_translate("MainWindow", "Modifier", None))
