####################################################################
# Toutes ces commandes doivent etre lancée depuis le répertoire    #
# contenant le fichier Makefile !                                  #
####################################################################
# Variables du makefile
TEST_DIR=tests/
SRC_DIR=src/
MAIN_FILE=main.py
NAME=CSP_Organizer

# Recuperation du python local pour l'execution
PYTHON=$(shell which python)


all :
	

# Pour executer notre application
exec :
	$(PYTHON) $(SRC_DIR)$(MAIN_FILE)

package : clean
	@echo "Mis en paquetage du projet :"
	@tar cvf $(NAME).tar.gz src/
	@echo $(NAME)".tar.gz créé"

# Pour lancer les tests unitaires
test :
	@clear
	@echo "Lancement des tests unitaires situés dans " $(TEST_DIR)
	$(PYTHON) -m unittest discover -s $(TEST_DIR)

# Nettoyage des binaires
clean :
	@echo "Nettoyage des fichiers *.pyc de l'architecture"
	find . -name "*.pyc" -type f -delete
	@echo "Nettoyage terminé !"

# Appel à ce monsieur musculeux et chauve
mrproper : clean
	
