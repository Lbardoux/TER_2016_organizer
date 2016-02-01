#!/bin/sh

# Lancement :
# sh installation_epydoc.sh
# ou
# ./installation_epydoc.sh
# Une connexion internet est requise pour wget

clear
printf "Debut de l'installation d'Epydoc......\n"
wget -q http://prdownloads.sourceforge.net/epydoc/epydoc-3.0.1.tar.gz
gunzip epydoc-3.0.1.tar.gz
tar -xvf epydoc-3.0.1.tar
rm -f epydoc-3.0.1.tar
cd epydoc-3.0.1
sudo make install
cd ..
rm -rf epydoc-3.0.1 
printf "Installation terminée !\n"

exit 0
