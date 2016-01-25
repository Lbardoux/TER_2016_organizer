TEST_DIR=tests/
SRC_DIR=src/
PYTHON=$(shell which python)

all :

test :
	$(PYTHON) -m unittest discover -s $(TEST_DIR)

clean :
	find . -name "*.pyc" -type f -delete

mrproper : clean
	
