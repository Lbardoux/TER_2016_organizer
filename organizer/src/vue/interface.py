#!/usr/bin/python
# -*-coding:utf-8 -*

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from trololo import *

app = QApplication(sys.argv)
w = QMainWindow(None)
ui = Ui_MainWindow()
ui.setupUi(w)
w.show()
sys.exit(app.exec_())
