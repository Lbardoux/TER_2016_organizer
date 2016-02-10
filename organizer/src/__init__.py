#!/usr/bin/python
# -*-coding:utf-8 -*
"""
Ce package est le plus général qui soit dans l'application, il contient en son sein
tous les fichiers sources pour l'application.

/!\ Attention /!\
certains de ces packages vont surement devoir etre installé, pour d'obscures
histoires de dépendances, i lest donc vivement recommandé de lancer un M{make install}
en ayant le programme : "setuptools" d'installer
Pour plus d'informations, voir le readme de l'application.
On retrouve ici une arborescence de packages et modules orienté MVC
src
|
|
+---vue
+---modele
|     |
|     +---agenda
|     |      |
|     |      `---importations
|     +---formation
|     `---contraintes
+---controleur
|
+---outils
|
`---lib externes (pas plus de détails ici)
"""
