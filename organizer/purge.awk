#!/usr/bin/awk -f

# A pour ambition de purger le code des lignes inutiles à l'execution (doc, commentaire, lignes vides, etc, print)
# pour récupérer la sortie, il suffit alors de faire ./purge.awk fname >monFichierPropre

BEGIN {
    c = 0;
    nbLigne = 0;
    for(i=1;i<ARGC;++i) {
	print ARGV[i]
    }
}

#doc monoligne
$0 ~ /^.*""".*""".*$/ || $0 ~ /^[ \t]*#.*$/ || $0 ~ /^[ \t]*$/{
    next;
}

#doc multiligne
$0 ~ /^.*""".*$/ {
    if (c == 1){
	c = 0
    }
    else{
	c = 1
    }
    next;
}

c == 0 {
    nbLigne++;
    print >>src_{FILENAME};
}
