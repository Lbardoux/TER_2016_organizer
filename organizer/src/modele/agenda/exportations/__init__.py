#!/usr/bin/python3
# -*-coding:utf-8 -*
"""
Le package suivant utilise sans l'importer l'API Agenda.
Ainsi, il ne faut pas changer les méthodes, au risque de tout casser.

Pour créer un nouvel Exporteur, il suffit de :
Créer une classe hériant de Exporteur
définir un bon constructeur (prenant une str en parametre, et appellant le
super constructeur avec ce nom).
et redéfinir _ecrireEntete(), _ecrirePied(), _faireJour().

C'est tout, enjoy !
@author: Laurent Bardoux p1108365
@version: 1.0

########################################################################
TODO
########################################################################
On pense exporter/importer une formation modélisée en se bsant également
sur le format ICS
En effet, puisque modifier/créer des composants dans ce format ne pose
aucun problème aux autres logiciels, on va pas se priver.

exemple d'ICS
BEGIN:VCALENDAR
BEGIN:CSP_FORMATION <--- formations
NOM:
ID:
RESPONSABLE:
NIVEAU:
BEGIN:CSP_UE <--- pour chaque UE
TITRE:
HEURES:
RESPONSABLE:
END:CSP_UE
END:CSP_FORMATION
END:VCALENDAR

Il manque actuellement le binding des Seances vers les VEVENT
########################################################################
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/")
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/..")
