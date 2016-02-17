#!/usr/bin/python3
# -*-coding:utf-8 -*

"""
Gestion des importations d'un Agenda.

Le format ICS étant assez ... human infriendly, peu de gens s'amusent a aller
lire un fichier ICS, aussi dense soit-il.
De plus, I{so far}, les logiciels existants acceptent les champs étranges,
ou inhabituels.

Notes
=====

On va utiliser le format ICS (ICalendar), pour pouvoir I{dumper} tout un
calendrier avec tous les éléments qui lui sont liés, comme :
	1. B{Les creneaux}
		
		On va utiliser le format standard pour les créneaux.
		
		B{Format ics}
		::
			BEGIN:VEVENT
			DTSTART:YYYYMMDDThhmmssZ
			DTEND:YYYYMMDDThhmmssZ
			END:VEVENT
		
		Avec les champs optionnels suivants :
		::
			DTSTAMP:
			SUMMARY:
			LOCATION:
			DESCRIPTION:
			UID:
			CREATED:
			LAST-MODIFIED:
			SEQUENCE:
	
	2. B{Une formation}
		
		Cela permettra d'embarquer la formation avec le calendrier.
		
		B{Format ics}
		::
			BEGIN:CSP_FORMATION
			informations(nom, responsable, id)
			...
			END:CSP_FORMATION
			
			BEGIN:CSP_UE
			...
			END:CSP_UE
		
		En liant gentiment les créneaux aux morceaux d'une formations.
		
	3. B{Les dépendances}
		
		On pourra lier les dépendances également, en les chargeant si elles
		sont trouvées (une dépendance introuvable ne devra pas empecher le chargement).
		
		B{Format ics}
		::
			BEGIN:CSP_DEPENDANCE
			NOM:
			END:CSP_DEPENDANCE
		
	4. B{Les contraintes}
		
		Les contraintes liées au calendrier principal.
		
		B{Format ics}
		::
			BEGIN:CSP_CONTRAINTE
			TYPE:
			DOMAINE:
			END:CSP_CONTRAINTE

Toutes ces informations sont susceptibles de changer, et sont données à titre de document.

"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/")
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../../outils")

