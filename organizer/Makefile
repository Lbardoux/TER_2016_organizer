####################################################################
# Toutes ces commandes doivent etre lancée depuis le répertoire    #
# contenant le fichier Makefile !                                  #
####################################################################
# Variables du makefile
TEST_DIR=tests/
SRC_DIR=src/
MAIN_FILE=main.py

# Recuperation du python local pour l'execution
PYTHON=$(shell which python)



# Pour executer notre application
exec : clean
	$(PYTHON) $(SRC_DIR)$(MAIN_FILE)

# Pour lancer les tests unitaires
test :
	$(PYTHON) -m unittest discover -s $(TEST_DIR)

# Nettoyage des binaires
clean :
	find . -name "*.pyc" -type f -delete

# Appel à ce monsieur musculeux et chauve
mrproper : clean
	
