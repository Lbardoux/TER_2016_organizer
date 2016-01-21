#!/bin/sh
# Ce script lance les tests de python une fois qu'il a été configuré
# A l'aide de la built-in unittest

# on trouve le python local, meme s'il n'est pas dans le PATH
# On lance la récupération des tests
# on supprime les binaires (.pyc) générés par la commande précédentes

TEST_DIR=tests
PYTHON="$(which python)"

$PYTHON -m unittest discover -s "$TEST_DIR"
rm -f "$TEST_DIR"/*.pyc

exit 0
