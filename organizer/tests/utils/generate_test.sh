#!/bin/sh
# genere un template de test pour python automatique
# prend le nom du fichier en argument pour pouvoir le créer
# Le fichier est créé dans le répertoire d'execution du script !

if [ ! $# -eq 1 ]
then
    printf "\033[1;31mIssue with the argument number,"
    printf "we need 1 argument (test filename)\033[0m\n"
    exit 1
fi

FILENAME="test_${1}.py"
>"$FILENAME"

PRINT () {
    TEXT="$1"
    printf "$1" >>"$FILENAME"
    return 0
}

PRINT "#!"
PRINT "`which python`""\n"
PRINT "# -*-coding:utf-8 -*\n\n"
PRINT "import unittest\n\n"
PRINT "class Test_${1}(unittest.TestCase):\n"
PRINT "\tdef setUp(self):\n"
PRINT "\t\t\n\n"
PRINT "\tdef tearDown(self):\n"
PRINT "\t\t\n\n"
PRINT "\tdef test_nothing(self):\n"
PRINT "\t\t\n\n"
PRINT "\n"
PRINT "if __name__ == \"__main__\":\n"
PRINT "\tunittest.main()\n"


exit 0

