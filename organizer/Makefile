####################################################################
# Toutes ces commandes doivent etre lancée depuis le répertoire    #
# contenant le fichier Makefile !                                  #
####################################################################
# Variables du makefile
TEST_DIR=tests/
INTEGRATION_DIR=integration/
SRC_DIR=src/
LIB_DIR=src/
MAIN_FILE=vue/fenetrefinale.py
NAME=CSP_Organizer

# Recuperation du python local pour l'execution
PYTHON=$(shell which python3)


all :
	

doc : mrproper
	@epydoc --debug --html -o doc/html/ -v src/ >doc/report.txt
	@echo "Fin de la génération de la doc dans doc/html"
	@echo "Pour un compte-rendu, voir doc/report.txt"

exec :
	$(PYTHON) $(SRC_DIR)$(MAIN_FILE)

package : doc
	@echo "Mis en paquetage du projet :"
	@tar cvf $(NAME).tar.gz src/ doc/html/
	@echo $(NAME)".tar.gz créé"

# Pour lancer les tests unitaires
test :
	@clear
	@echo "Lancement des tests unitaires situés dans " $(TEST_DIR)
	$(PYTHON) -m unittest discover -s $(TEST_DIR)
	@echo "\nTests d'integrations :"
	find $(TEST_DIR)$(INTEGRATION_DIR) -name "integration_*.py" -exec $(PYTHON) {} \;

# Nettoyage des binaires
clean :
	@echo "Nettoyage des fichiers *.pyc de l'architecture"
	find . -name "*.pyc" -type f -delete
	@rm -f doc/report.txt
	@echo "Nettoyage terminé !"

# Appel à ce monsieur musculeux et chauve
mrproper : clean
	rm -Rf doc/html/*

install:
	# on fera un Readme exigeant d'avoir setuptools, etc
	#installation de icalendar
	$(PYTHON) $(LIB_DIR)icalendar-3.9.2/setup.py install --user
	#installation de pyconstraint
	$(PYTHON) $(LIB_DIR)pyconstraints-1.0.1/setup.py install --user
	#installation de pytz	
	$(PYTHON) $(LIB_DIR)pytz-2015.7/setup.py install --user
