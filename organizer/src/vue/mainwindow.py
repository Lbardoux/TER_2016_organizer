# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'organizer/src/vue/test.ui'
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
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 800, 580))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.listeUe = QtGui.QWidget()
        self.listeUe.setObjectName(_fromUtf8("listeUe"))
        self.scrollArea_2 = QtGui.QScrollArea(self.listeUe)
        self.scrollArea_2.setGeometry(QtCore.QRect(9, 10, 251, 521))
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 238, 519))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.formLayoutWidget_4 = QtGui.QWidget(self.listeUe)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(580, 10, 191, 151))
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
        self.descriptionLabel_3 = QtGui.QLabel(self.formLayoutWidget_4)
        self.descriptionLabel_3.setObjectName(_fromUtf8("descriptionLabel_3"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.descriptionLabel_3)
        self.descriptionLineEdit_3 = QtGui.QLineEdit(self.formLayoutWidget_4)
        self.descriptionLineEdit_3.setObjectName(_fromUtf8("descriptionLineEdit_3"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.descriptionLineEdit_3)
        self.durELabel_3 = QtGui.QLabel(self.formLayoutWidget_4)
        self.durELabel_3.setObjectName(_fromUtf8("durELabel_3"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.durELabel_3)
        self.durESpinBox_3 = QtGui.QSpinBox(self.formLayoutWidget_4)
        self.durESpinBox_3.setObjectName(_fromUtf8("durESpinBox_3"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.durESpinBox_3)
        self.nombreDePersonnesLabel_3 = QtGui.QLabel(self.formLayoutWidget_4)
        self.nombreDePersonnesLabel_3.setObjectName(_fromUtf8("nombreDePersonnesLabel_3"))
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.LabelRole, self.nombreDePersonnesLabel_3)
        self.nombreDePersonnesSpinBox_2 = QtGui.QSpinBox(self.formLayoutWidget_4)
        self.nombreDePersonnesSpinBox_2.setObjectName(_fromUtf8("nombreDePersonnesSpinBox_2"))
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.FieldRole, self.nombreDePersonnesSpinBox_2)
        self.pushButton_4 = QtGui.QPushButton(self.formLayoutWidget_4)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.formLayout_4.setWidget(4, QtGui.QFormLayout.FieldRole, self.pushButton_4)
        self.widget = QtGui.QWidget(self.listeUe)
        self.widget.setGeometry(QtCore.QRect(280, 70, 281, 361))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.couLabel = QtGui.QLabel(self.widget)
        self.couLabel.setObjectName(_fromUtf8("couLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.couLabel)
        self.couLineEdit = QtGui.QLineEdit(self.widget)
        self.couLineEdit.setObjectName(_fromUtf8("couLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.couLineEdit)
        self.ssLabel = QtGui.QLabel(self.widget)
        self.ssLabel.setObjectName(_fromUtf8("ssLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.ssLabel)
        self.ssLineEdit = QtGui.QLineEdit(self.widget)
        self.ssLineEdit.setObjectName(_fromUtf8("ssLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.ssLineEdit)
        self.responsableLabel = QtGui.QLabel(self.widget)
        self.responsableLabel.setObjectName(_fromUtf8("responsableLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.responsableLabel)
        self.responsableComboBox = QtGui.QComboBox(self.widget)
        self.responsableComboBox.setObjectName(_fromUtf8("responsableComboBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.responsableComboBox)
        self.nombreDePersonnesLabel_2 = QtGui.QLabel(self.widget)
        self.nombreDePersonnesLabel_2.setObjectName(_fromUtf8("nombreDePersonnesLabel_2"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.nombreDePersonnesLabel_2)
        self.nombreDeTdsSpinBox_2 = QtGui.QSpinBox(self.widget)
        self.nombreDeTdsSpinBox_2.setObjectName(_fromUtf8("nombreDeTdsSpinBox_2"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.nombreDeTdsSpinBox_2)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.tabWidget_2 = QtGui.QTabWidget(self.widget)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.CMs = QtGui.QWidget()
        self.CMs.setObjectName(_fromUtf8("CMs"))
        self.formLayoutWidget_2 = QtGui.QWidget(self.CMs)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(40, 30, 174, 80))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.nombreDeTdsLabel = QtGui.QLabel(self.formLayoutWidget_2)
        self.nombreDeTdsLabel.setObjectName(_fromUtf8("nombreDeTdsLabel"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.nombreDeTdsLabel)
        self.nombreDeTdsSpinBox = QtGui.QSpinBox(self.formLayoutWidget_2)
        self.nombreDeTdsSpinBox.setObjectName(_fromUtf8("nombreDeTdsSpinBox"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.nombreDeTdsSpinBox)
        self.nombreDeTdsLabel_2 = QtGui.QLabel(self.formLayoutWidget_2)
        self.nombreDeTdsLabel_2.setObjectName(_fromUtf8("nombreDeTdsLabel_2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.nombreDeTdsLabel_2)
        self.nombreDeTdsSpinBox_3 = QtGui.QSpinBox(self.formLayoutWidget_2)
        self.nombreDeTdsSpinBox_3.setObjectName(_fromUtf8("nombreDeTdsSpinBox_3"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.nombreDeTdsSpinBox_3)
        self.formLayoutWidget_2.raise_()
        self.tabWidget_2.addTab(self.CMs, _fromUtf8(""))
        self.TDs = QtGui.QWidget()
        self.TDs.setObjectName(_fromUtf8("TDs"))
        self.formLayoutWidget_7 = QtGui.QWidget(self.TDs)
        self.formLayoutWidget_7.setGeometry(QtCore.QRect(20, 30, 223, 95))
        self.formLayoutWidget_7.setObjectName(_fromUtf8("formLayoutWidget_7"))
        self.formLayout_7 = QtGui.QFormLayout(self.formLayoutWidget_7)
        self.formLayout_7.setObjectName(_fromUtf8("formLayout_7"))
        self.nombreDeTdsLabel_3 = QtGui.QLabel(self.formLayoutWidget_7)
        self.nombreDeTdsLabel_3.setObjectName(_fromUtf8("nombreDeTdsLabel_3"))
        self.formLayout_7.setWidget(0, QtGui.QFormLayout.LabelRole, self.nombreDeTdsLabel_3)
        self.nombreDeTdsSpinBox_4 = QtGui.QSpinBox(self.formLayoutWidget_7)
        self.nombreDeTdsSpinBox_4.setObjectName(_fromUtf8("nombreDeTdsSpinBox_4"))
        self.formLayout_7.setWidget(0, QtGui.QFormLayout.FieldRole, self.nombreDeTdsSpinBox_4)
        self.nombreDeTdsLabel_4 = QtGui.QLabel(self.formLayoutWidget_7)
        self.nombreDeTdsLabel_4.setObjectName(_fromUtf8("nombreDeTdsLabel_4"))
        self.formLayout_7.setWidget(1, QtGui.QFormLayout.LabelRole, self.nombreDeTdsLabel_4)
        self.nombreDeTdsSpinBox_5 = QtGui.QSpinBox(self.formLayoutWidget_7)
        self.nombreDeTdsSpinBox_5.setObjectName(_fromUtf8("nombreDeTdsSpinBox_5"))
        self.formLayout_7.setWidget(1, QtGui.QFormLayout.FieldRole, self.nombreDeTdsSpinBox_5)
        self.nombreDeGroupesTDLabel = QtGui.QLabel(self.formLayoutWidget_7)
        self.nombreDeGroupesTDLabel.setObjectName(_fromUtf8("nombreDeGroupesTDLabel"))
        self.formLayout_7.setWidget(2, QtGui.QFormLayout.LabelRole, self.nombreDeGroupesTDLabel)
        self.nombreDeTdsSpinBox_6 = QtGui.QSpinBox(self.formLayoutWidget_7)
        self.nombreDeTdsSpinBox_6.setProperty("value", 1)
        self.nombreDeTdsSpinBox_6.setObjectName(_fromUtf8("nombreDeTdsSpinBox_6"))
        self.formLayout_7.setWidget(2, QtGui.QFormLayout.FieldRole, self.nombreDeTdsSpinBox_6)
        self.tabWidget_2.addTab(self.TDs, _fromUtf8(""))
        self.TPs = QtGui.QWidget()
        self.TPs.setObjectName(_fromUtf8("TPs"))
        self.formLayoutWidget_8 = QtGui.QWidget(self.TPs)
        self.formLayoutWidget_8.setGeometry(QtCore.QRect(20, 30, 223, 95))
        self.formLayoutWidget_8.setObjectName(_fromUtf8("formLayoutWidget_8"))
        self.formLayout_8 = QtGui.QFormLayout(self.formLayoutWidget_8)
        self.formLayout_8.setObjectName(_fromUtf8("formLayout_8"))
        self.nombreDeTdsLabel_5 = QtGui.QLabel(self.formLayoutWidget_8)
        self.nombreDeTdsLabel_5.setObjectName(_fromUtf8("nombreDeTdsLabel_5"))
        self.formLayout_8.setWidget(0, QtGui.QFormLayout.LabelRole, self.nombreDeTdsLabel_5)
        self.nombreDeTdsSpinBox_7 = QtGui.QSpinBox(self.formLayoutWidget_8)
        self.nombreDeTdsSpinBox_7.setObjectName(_fromUtf8("nombreDeTdsSpinBox_7"))
        self.formLayout_8.setWidget(0, QtGui.QFormLayout.FieldRole, self.nombreDeTdsSpinBox_7)
        self.nombreDeTdsLabel_6 = QtGui.QLabel(self.formLayoutWidget_8)
        self.nombreDeTdsLabel_6.setObjectName(_fromUtf8("nombreDeTdsLabel_6"))
        self.formLayout_8.setWidget(1, QtGui.QFormLayout.LabelRole, self.nombreDeTdsLabel_6)
        self.nombreDeTdsSpinBox_8 = QtGui.QSpinBox(self.formLayoutWidget_8)
        self.nombreDeTdsSpinBox_8.setObjectName(_fromUtf8("nombreDeTdsSpinBox_8"))
        self.formLayout_8.setWidget(1, QtGui.QFormLayout.FieldRole, self.nombreDeTdsSpinBox_8)
        self.nombreDeGroupesTDLabel_2 = QtGui.QLabel(self.formLayoutWidget_8)
        self.nombreDeGroupesTDLabel_2.setObjectName(_fromUtf8("nombreDeGroupesTDLabel_2"))
        self.formLayout_8.setWidget(2, QtGui.QFormLayout.LabelRole, self.nombreDeGroupesTDLabel_2)
        self.nombreDeTdsSpinBox_9 = QtGui.QSpinBox(self.formLayoutWidget_8)
        self.nombreDeTdsSpinBox_9.setProperty("value", 1)
        self.nombreDeTdsSpinBox_9.setObjectName(_fromUtf8("nombreDeTdsSpinBox_9"))
        self.formLayout_8.setWidget(2, QtGui.QFormLayout.FieldRole, self.nombreDeTdsSpinBox_9)
        self.tabWidget_2.addTab(self.TPs, _fromUtf8(""))
        self.Examens = QtGui.QWidget()
        self.Examens.setObjectName(_fromUtf8("Examens"))
        self.formLayoutWidget_9 = QtGui.QWidget(self.Examens)
        self.formLayoutWidget_9.setGeometry(QtCore.QRect(30, 30, 223, 95))
        self.formLayoutWidget_9.setObjectName(_fromUtf8("formLayoutWidget_9"))
        self.formLayout_9 = QtGui.QFormLayout(self.formLayoutWidget_9)
        self.formLayout_9.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_9.setObjectName(_fromUtf8("formLayout_9"))
        self.nombreDeTdsLabel_7 = QtGui.QLabel(self.formLayoutWidget_9)
        self.nombreDeTdsLabel_7.setObjectName(_fromUtf8("nombreDeTdsLabel_7"))
        self.formLayout_9.setWidget(0, QtGui.QFormLayout.LabelRole, self.nombreDeTdsLabel_7)
        self.nombreDeTdsSpinBox_10 = QtGui.QSpinBox(self.formLayoutWidget_9)
        self.nombreDeTdsSpinBox_10.setObjectName(_fromUtf8("nombreDeTdsSpinBox_10"))
        self.formLayout_9.setWidget(0, QtGui.QFormLayout.FieldRole, self.nombreDeTdsSpinBox_10)
        self.nombreDeTdsLabel_8 = QtGui.QLabel(self.formLayoutWidget_9)
        self.nombreDeTdsLabel_8.setObjectName(_fromUtf8("nombreDeTdsLabel_8"))
        self.formLayout_9.setWidget(1, QtGui.QFormLayout.LabelRole, self.nombreDeTdsLabel_8)
        self.nombreDeTdsSpinBox_11 = QtGui.QSpinBox(self.formLayoutWidget_9)
        self.nombreDeTdsSpinBox_11.setObjectName(_fromUtf8("nombreDeTdsSpinBox_11"))
        self.formLayout_9.setWidget(1, QtGui.QFormLayout.FieldRole, self.nombreDeTdsSpinBox_11)
        self.tabWidget_2.addTab(self.Examens, _fromUtf8(""))
        self.Autres = QtGui.QWidget()
        self.Autres.setObjectName(_fromUtf8("Autres"))
        self.formLayoutWidget_10 = QtGui.QWidget(self.Autres)
        self.formLayoutWidget_10.setGeometry(QtCore.QRect(30, 40, 191, 61))
        self.formLayoutWidget_10.setObjectName(_fromUtf8("formLayoutWidget_10"))
        self.formLayout_10 = QtGui.QFormLayout(self.formLayoutWidget_10)
        self.formLayout_10.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_10.setObjectName(_fromUtf8("formLayout_10"))
        self.nombreDeTdsLabel_9 = QtGui.QLabel(self.formLayoutWidget_10)
        self.nombreDeTdsLabel_9.setObjectName(_fromUtf8("nombreDeTdsLabel_9"))
        self.formLayout_10.setWidget(0, QtGui.QFormLayout.LabelRole, self.nombreDeTdsLabel_9)
        self.nombreDeTdsSpinBox_12 = QtGui.QSpinBox(self.formLayoutWidget_10)
        self.nombreDeTdsSpinBox_12.setObjectName(_fromUtf8("nombreDeTdsSpinBox_12"))
        self.formLayout_10.setWidget(0, QtGui.QFormLayout.FieldRole, self.nombreDeTdsSpinBox_12)
        self.tabWidget_2.addTab(self.Autres, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabWidget_2)
        self.buttonBox_2 = QtGui.QDialogButtonBox(self.widget)
        self.buttonBox_2.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName(_fromUtf8("buttonBox_2"))
        self.verticalLayout_3.addWidget(self.buttonBox_2)
        self.tabWidget.addTab(self.listeUe, _fromUtf8(""))
        self.Contraintes = QtGui.QWidget()
        self.Contraintes.setObjectName(_fromUtf8("Contraintes"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.Contraintes)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 800, 61))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.toolButton_3 = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.toolButton_3.setMinimumSize(QtCore.QSize(100, 50))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.horizontalLayout.addWidget(self.toolButton_3)
        self.toolButton_2 = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.toolButton_2.setMinimumSize(QtCore.QSize(100, 50))
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.horizontalLayout.addWidget(self.toolButton_2)
        self.toolButton_4 = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.toolButton_4.setMinimumSize(QtCore.QSize(100, 50))
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.horizontalLayout.addWidget(self.toolButton_4)
        self.toolButton = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.toolButton.setMinimumSize(QtCore.QSize(100, 50))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout.addWidget(self.toolButton)
        self.scrollArea = QtGui.QScrollArea(self.Contraintes)
        self.scrollArea.setGeometry(QtCore.QRect(20, 200, 760, 281))
        self.scrollArea.setMinimumSize(QtCore.QSize(760, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(760, 16777215))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 747, 279))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayoutWidget = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 751, 281))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.buttonBox = QtGui.QDialogButtonBox(self.Contraintes)
        self.buttonBox.setGeometry(QtCore.QRect(320, 500, 176, 29))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.frame = QtGui.QFrame(self.Contraintes)
        self.frame.setGeometry(QtCore.QRect(20, 80, 760, 100))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(640, 40, 100, 29))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.tabWidget.addTab(self.Contraintes, _fromUtf8(""))
        self.Visualisation = QtGui.QWidget()
        self.Visualisation.setObjectName(_fromUtf8("Visualisation"))
        self.tabWidget.addTab(self.Visualisation, _fromUtf8(""))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(520, 0, 281, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.comboBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "CSP organiseur", None))
        self.nomTPLabel_3.setText(_translate("MainWindow", "Nom TD", None))
        self.descriptionLabel_3.setText(_translate("MainWindow", "Description", None))
        self.durELabel_3.setText(_translate("MainWindow", "Durée ", None))
        self.nombreDePersonnesLabel_3.setText(_translate("MainWindow", "Nombre de personnes", None))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton", None))
        self.couLabel.setText(_translate("MainWindow", "Code Ue", None))
        self.ssLabel.setText(_translate("MainWindow", "Nom", None))
        self.responsableLabel.setText(_translate("MainWindow", "Responsable", None))
        self.nombreDePersonnesLabel_2.setText(_translate("MainWindow", "Nombre de Personnes", None))
        self.nombreDeTdsLabel.setText(_translate("MainWindow", "Nombre de CMs", None))
        self.nombreDeTdsLabel_2.setText(_translate("MainWindow", "Durée de CMs", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.CMs), _translate("MainWindow", "CMs", None))
        self.nombreDeTdsLabel_3.setText(_translate("MainWindow", "Nombre de TDs", None))
        self.nombreDeTdsLabel_4.setText(_translate("MainWindow", "Durée de TDs", None))
        self.nombreDeGroupesTDLabel.setText(_translate("MainWindow", "Nombre de groupes TD", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.TDs), _translate("MainWindow", "TDs", None))
        self.nombreDeTdsLabel_5.setText(_translate("MainWindow", "Nombre de TPs", None))
        self.nombreDeTdsLabel_6.setText(_translate("MainWindow", "Durée de TPs", None))
        self.nombreDeGroupesTDLabel_2.setText(_translate("MainWindow", "Nombre de groupes TP", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.TPs), _translate("MainWindow", "TPs", None))
        self.nombreDeTdsLabel_7.setText(_translate("MainWindow", "Nombre d\'examens", None))
        self.nombreDeTdsLabel_8.setText(_translate("MainWindow", "Durée d\'examens", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Examens), _translate("MainWindow", "Examens", None))
        self.nombreDeTdsLabel_9.setText(_translate("MainWindow", "Nombre d\'autres", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Autres), _translate("MainWindow", "Autres", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.listeUe), _translate("MainWindow", "Liste des UEs", None))
        self.toolButton_3.setText(_translate("MainWindow", "Obligation", None))
        self.toolButton_2.setText(_translate("MainWindow", "Blocage", None))
        self.toolButton_4.setText(_translate("MainWindow", "Date limite", None))
        self.toolButton.setText(_translate("MainWindow", "Precedence", None))
        self.label_3.setText(_translate("MainWindow", "TextLabel", None))
        self.label_4.setText(_translate("MainWindow", "TextLabel", None))
        self.label_6.setText(_translate("MainWindow", "TextLabel", None))
        self.label_5.setText(_translate("MainWindow", "TextLabel", None))
        self.label_2.setText(_translate("MainWindow", "TextLabel", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Contraintes), _translate("MainWindow", "Contraintes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Visualisation), _translate("MainWindow", "Visualisation", None))
        self.label.setText(_translate("MainWindow", "Formation : ", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Master 1 Informatique", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Master 2 SIR", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "Master 2 DS", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "Master 2 TI", None))
        self.comboBox.setItemText(4, _translate("MainWindow", "Master 2 Image", None))