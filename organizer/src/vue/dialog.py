# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog1.ui'
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

class Ui_DialogCalendrier(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QtCore.QSize(400, 300))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        self.calendar = QtGui.QCalendarWidget(Dialog)
        self.calendar.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.calendar.setMinimumSize(QtCore.QSize(400, 300))
        self.calendar.setMaximumSize(QtCore.QSize(400, 300))
        self.calendar.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendar.setHorizontalHeaderFormat(QtGui.QCalendarWidget.ShortDayNames)
        self.calendar.setVerticalHeaderFormat(QtGui.QCalendarWidget.NoVerticalHeader)
        self.calendar.setObjectName(_fromUtf8("calendar"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
