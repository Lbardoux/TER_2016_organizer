#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Voici le module chargé d'afficher un compte rendu à l'utilisateur lors de la
recherche des différences.

@author: Laurent Bardoux p1108365
@version: 1.0
"""

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui


class FenetreDiff(QWidget):
	"""
	Voici la classe qui, en se servant des propriétés de QWidget, va etre utilisée pour
	afficher le compte rendu à l'utilisateur.
	@ivar layout: la layout qui met en place la zone de texte et le bouton.
	@ivar scroll: La zone de texte qui affichera les différences.
	@ivar label: le texte qu'il va falloir afficher.
	@ivar boutonFermer: le bouton pour fermer cette fenetre.
	@author: Laurent Bardoux p1108365
	@version: 1.0
	"""
	
	def __init__(self, diff):
		"""
		Le constructeur de cette classe, qui initialise correctement cette fenetre.
		Il va se charger de charger la fenetre, mettre en place les QWidgets,
		et afficher les différences en lisant le I{diff} fourni.
		@param self: L'argument implicite.
		@type diff: L{Diff}
		@param diff: L'objet qui a effectué la comparaison
		"""
		super(FenetreDiff, self).__init__()
		self.setWindowTitle("Différences entre " + diff.agenda1.nom + " et " + diff.agenda2.nom)
		self.setGeometry(100, 100, 600, 400)
		
		self.layout = QVBoxLayout(self)
		self.setLayout(self.layout)
		
		self.scroll = QtGui.QScrollArea()
		self.scroll.setFixedHeight(350)
		self.scroll.setFixedWidth(600)
		self.layout.addWidget(self.scroll)
		
		# remplissage du texte
		texte = "Il n'y a pas de différence !" if len(diff.moments) == 0 else ""
		for moment in diff.moments:
			texte += str(moment) + "\n"
			for difference in diff.differences[moment]:
				texte += str(difference)
			#for
		#for
		self.label = QtGui.QLabel(texte, self.scroll)
		self.label.setWordWrap(True)
		self.scroll.setWidget(self.label)

		# bouton pour fermer la fenetre
		self.boutonFermer = QtGui.QPushButton(None)
		self.boutonFermer.setObjectName("Fermer")
		self.boutonFermer.setText("Fermer")
		self.layout.addWidget(self.boutonFermer)
		self.boutonFermer.connect(self.boutonFermer, QtCore.SIGNAL("clicked()"), self.fermer)
	#__init__
	
	
	def fermer(self):
		"""
		Permet de fermer la fenetre lorsque l'on clique sur le bouton.
		@param self: L'argument implicite.
		"""
		self.close()
	#fermer
	
#FenetreDiff
