#!/bin/sh

# Lancement :
# sh installation_epydoc.sh
# ou
# ./installation_epydoc.sh
# Une connexion internet est requise pour wget

if [ "$(id -u)" -ne "0" ]
then
	printf "\033[1;31mIl faut etre en root pour lancer ce script !\033[0m\n"
	printf "Donc prière de lire ce script, puis de l'executer en root (sudo ou autre)\n"
	exit 1 
fi
clear
printf "Debut de l'installation d'Epydoc......\n"
wget -q http://prdownloads.sourceforge.net/epydoc/epydoc-3.0.1.tar.gz
gunzip epydoc-3.0.1.tar.gz
tar -xvf epydoc-3.0.1.tar
rm -f epydoc-3.0.1.tar
cd epydoc-3.0.1
make install
cd ..
rm -rf epydoc-3.0.1 
printf "Installation terminée !\n"

exit 0
