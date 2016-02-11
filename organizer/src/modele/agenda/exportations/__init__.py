#!/usr/bin/python
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
"""
