TEST_DIR=tests/
SRC_DIR=src/
MAIN_FILE=main.py
PYTHON=$(shell which python)

all :


exec :
	$(PYTHON) $(SRC_DIR)$(MAIN_FILE)

test :
	$(PYTHON) -m unittest discover -s $(TEST_DIR)

clean :
	find . -name "*.pyc" -type f -delete

mrproper : clean
	
