 # -*- coding: utf-8 -*-


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


class monFrame(QtGui.QFrame):
	def __init__(self, superieur, nom):
		super(monFrame,self).__init__(superieur)
		self._nom = nom 
		self._disposition = QtGui.QVBoxLayout(self)
		self._disposition.setMargin(0)
		self._disposition.setSpacing(0)
		self._disposition.setObjectName(_fromUtf8("disposition"+nom))
		self._couleur = "grey"
	#fin __init__
	
	def _transformerHeure(self, debut, fin):
		heureDebut = debut//4 + 8
		minuteDebut = debut%4 * 15
		heureFin = fin//4 + 8 
		minuteFin = fin%4 * 15
		if minuteDebut is 0:
			minuteDebut = "00"
		#fin if
		
		if minuteFin is 0:
			minuteFin = "00"
		#fin if
		
		return str(heureDebut) + "H" +str(minuteDebut) + "-" +str(heureFin) + "H" +str(minuteFin)
	#fin _transformerHeure
	
	def _calculerPixelDebut(self,debut):
		return debut*13+42
	#fin _CalculerPixelDebut
	
	def _calculerHauteur(self, debut, fin):
		return (fin-debut)*13
	#fin _CalculerHauteur
	
	def _configurerLabel(self, nomLabel, chaineLabel):
		retour = QtGui.QLabel(self)
		retour.setAlignment(QtCore.Qt.AlignCenter)
		retour.setObjectName(_fromUtf8(nomLabel))
		self._disposition.addWidget(retour)
		retour.raise_()
		retour.setText(_fromUtf8(chaineLabel))
		return retour
	#fin _configurerLabel
	
	def setUpMonFrame(self, debut, fin, code, seance, salle, enseignant, couleur="grey"):
		
		self._couleur = couleur
		self.setGeometry(QtCore.QRect(2, self._calculerPixelDebut(debut), 188, self._calculerHauteur(debut,fin)))
		self.setStyleSheet(_fromUtf8("#" + self._nom + ">.QLabel{background-color:"+self._couleur+";}"))
		self.setObjectName(_fromUtf8(self._nom))
		chaineInfo = self._transformerHeure(debut, fin)+"<br>"+code+"<br>"+seance+"<br>"+salle+"<br>"+enseignant
		info = self._configurerLabel("info"+self._nom,chaineInfo)

		self.setToolTip(_fromUtf8(chaineInfo))
		
	#fin setUpMonFrame
	
