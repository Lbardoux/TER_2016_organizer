#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Check Constraints Calendar
# Author: Yves Caniou
# Date: 07/07/2015
# Mail: yves.caniou@univ-lyon1.fr

# Récup de l'EdT
# http://adelb.univ-lyon1.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources=13686&projectId=1&calType=ical&firstDate=2015-09-28&lastDate=2016-09-10

import sys # for exit()
import time
import inspect
import icalendar
import datetime
import argparse
import pytz
from pytz import timezone
# datetime a des soucis pour le numéro de la semaine en fct de la date
import isoweek
# pour les stats
from numpy import *

from icalendar import Calendar, Event
# from datetime import datetime
#from icalendar import UTC # timezone

# Si EXAMEN=0, CC intégral
# Ajouter HETD théorique, i.e., en fonction crédit UE
# _CM, _TD et _TP sont les heures à placer dans l'EdT
RM   = {'TITLE' : "RMob",
        'RESP' : "DUPONT",
        '_CM': 25, '_TD' : 5, '_TP' : 0, '_EXAMEN' : 0,
        'CREDIT' : 3,
        'SEM' : 3
}
RSF  = {'TITLE' : "RSF",
        'RESP' : "DUPONT",
        '_CM': 15, '_TD' : 3, '_TP' : 12, '_EXAMEN' : 0,
        'CREDIT' : 3,
        'SEM' : 3
}
SPAI = {'TITLE' : "SPAI",
        'RESP' : "GLUCK",
        '_CM': 25, '_TD' : 0, '_TP' : 6, '_EXAMEN' : 0.75,
        'CREDIT' : 3,
        'SEM' : 3
}
RA   = {'TITLE' : "RA",
        'RESP' : "BEGIN",
        '_CM': 19.5, '_TD' : 4.5, '_TP' : 18, '_EXAMEN' : 1.5,
        'CREDIT' : 3,
        'SEM' : 3
}
QSM  = {'TITLE' : "QSM",
        'RESP' : "IGL",
        '_CM': 18, '_TD' : 4, '_TP' : 8, '_EXAMEN' : 1.5,
        'CREDIT' : 3,
        'SEM' : 3
}
TER  = {'TITLE' : "TER",
        'RESP' : "CANIOU",
        '_CM': 0, '_TD' : 90, '_TP' : 0, '_EXAMEN' : 5,
        'CREDIT' : 3,
        'SEM' : 3
}
AdminSR = {'TITLE' : "AdminSR",
           'RESP' : "GLUCK",
           '_CM': 12, '_TD' : 0, '_TP' : 34, '_EXAMEN' : 0,
           'CREDIT' : 3,
           'SEM' : 3
}
AR  = {'TITLE' : "AR",
       'RESP' : "GELAS",
       '_CM': 21, '_TD' : 0, '_TP' : 18, '_EXAMEN' : 1.5,
       'CREDIT' : 3,
       'SEM' : 3
}      
ASR = {'TITLE' : "ASR",
       'RESP' : "CANIOU",
       '_CM': 15, '_TD' : 0, '_TP' : 15, '_EXAMEN' : 2,
       'CREDIT' : 3,
       'SEM' : 3
}
NT  = {'TITLE' : "NT",
       'RESP' : "GELAS",
       '_CM' : 12, '_TD' : 0, '_TP' : 25, '_EXAMEN' : 0,
       'CREDIT' : 3,
       'SEM' : 3
}
DROIT = {'TITLE' : "Droit informatique",
         'RESP' : "BERGHEAUD",
         '_CM' : 30, '_TD' : 0, '_TP' : 0, '_EXAMEN' : 1.5,
         'CREDIT' : 3,
         'SEM' : 4
}
CoM = {'TITLE' : "CoMétier",
       'RESP' : "LALLIARD",
       '_CM' : 0, '_TD' : 30, '_TP' : 0, '_EXAMEN' : 0,
       'CREDIT' : 3,
       'SEM' : 4
}
Anglais = {'TITLE' : "Anglais",
       'RESP' : "DUCREUX",
       '_CM' : 0, '_TD' : 30, '_TP' : 0, '_EXAMEN' : 0,
       'CREDIT' : 3,
       'SEM' : 4
}
RE = {'TITLE' : "Retour Entreprise",
      'RESP' : "NON",
      '_CM' : 0, '_TD' : 30, '_TP' : 0, '_EXAMEN' : -1,
      'CREDIT' : 3,
      'SEM' : 4
}     
CCNA = {'TITLE' : "CCNA",
        'RESP' : "RICO",
        '_CM' : 0, '_TD' : 0, '_TP' : 30, '_EXAMEN' : 0,
        'CREDIT' : 0,
        'SEM' : 4
}

SIR = [RM, RSF, SPAI, RA, QSM, TER, AdminSR, AR, ASR, NT,
       DROIT, CoM, RE, Anglais, CCNA]
COMMON = [RSF, SPAI, RA, QSM]

# Semaine où les étudiants sont à l'Université, dont session septembre
SEMAINES_UNIV = [ "2015W40", "2015W42", "2015W43", "2015W46", "2015W47",
                  "2015W50", "2015W51",
                  "2016W01", "2016W02", "2016W05", "2016W06",
                  "2016W09", "2016W10", "2016W14", "2016W15", "2016W19",
                  "2016W20", "2016W23" ]
#, "2016W36"
RTS_deadline = datetime.date(2016, 2, 5)

def ict( t, fmt ):
    """ gives the time in calendar timezone. Assumes cal_timezone is defined."""
    # TODO : là, calendrier dans le même fuseau horaire que local
    #        On doit se mettre dans le fuseau du calendrier, dc utiliser
    #        cal_timezone!
    return( t.astimezone().strftime(fmt) )

def checkRTS( a, i ):
    """ a défini si le test est final (vérification terminaison UE avt
    date buttoir, ou test continu, i.e., pas certaines UEs à certains créneaux
    horaires
    """
    # Contraintes RTS
    # pas d'UEs communes
    #  - les mardi 9h-12h ou 10h-13h -> Simplification 9h-13h
    #  - les vendredi 8h-10h
    #  - les vendredi 13h15-16h15
    # UEs communes doivent finir avant le 5/02, exam compris
    if a == "final":
        ok=1
        for i in COMMON:
#            print(str(i))
            if i['LAST'] > RTS_deadline:
                ok=0
                print("UE " + i['TITLE'] + " termine le "
                      + str(i['LAST']) + " après " + str(RTS_deadline) )
        if ok == 1:
            str_common=""
            for common_ue in COMMON:
                str_common+=common_ue['TITLE']+" "
            print("La dernière occurence programmée de [" + str_common + "]"+
                  "a lieu le " + str(i['LAST']) + ", avant " + str(RTS_deadline))
    elif a == "in":
        UE_jour = UE_start.strftime("%A")
        if UE_jour == "Mardi" or UE_jour == "Tuesday":
            if ict(UE_start,"%H:%M") >= "08:00" and ict(UE_end,"%H:%M") <= "13:00":
                print("Contraintes RTS non respectées pour UE "
                      + i['TITLE'] + " du " + ict(UE_start,"%d/%m/%y à %H:%M") )
        if UE_jour == "Vendredi" or UE_jour == "Friday":
            if not( ict(UE_start, "%H:%M") >= "10:00" and ict(UE_end,"%H:%M") <= "13:00"):
                print("Contraintes RTS non respectées pour UE "
                      + i['TITLE'] + " du " + ict(UE_start,"%d/%m/%y à %H:%M") )
    else:
        print("EROR")
        
def checkSIRapp():    
    # Contraintes SIRapp
    # Faire test sur les semaines de présence
    print("To implement")

############################################################## PARSE CMDLINE
# https://docs.python.org/3/howto/argparse.html
parser = argparse.ArgumentParser(description="Analyze calendar")
parser.add_argument("calendar", help="the calendar.ics to analyze")
args = parser.parse_args()
cal_name = args.calendar
# TODO: Vérifier que l'argument est bien un .ics
# TODO: use ATTENDEE (first: see if export from ADE manage that!)

######## Init structures and variables
for i in SIR:
    # Ajout compteurs pour les heures en place
    i['CM'] = datetime.timedelta(0)
    i['TD'] = datetime.timedelta(0)
    i['TP'] = datetime.timedelta(0)
    i['EXAMEN'] = datetime.timedelta(0)
    i['INTERVENANT'] = []
# UE = {'TITLE','RESP','_CM','_TD','_TP,'_EXAMEN', 'CM', 'TD', 'TP', 'EXAMEN'
#        'INTERVENANT' = ['CM':timedate, 'TD' : timedate, 'TP' : timedate,
#                         'EXAMEN' : timedate,
#                         'DATES' = ['2015S04' : [('type',debut,fin),()]] ]

heures_par_semaine = {}
# heures_par_semaine['2016W10']={'TOT': duree, 'CCNA':duree}
hours_bef_soutenance_TER = datetime.timedelta(0)

####################################################################### MAIN
f = open(cal_name)
poil=f.read()
cal = Calendar.from_ical(poil)
for component in cal.walk():
    if component.name == 'VTIMEZONE':
        cal_timezone = pytz.timezone(str(component.decoded('TZID'))[2:-1])
    if component.name == 'VEVENT':
        UE_summary = component.get('SUMMARY')
        # TODO: tester si DURATION existe et sa valeur le cas échéant
        UE_start = component.decoded('DTSTART')
        UE_end = component.decoded('DTEND')
        UE_duration = UE_end - UE_start
        
        # Test que l'évènement est dans les semaines Univ
        # ATTENTION : UE_semaine est de type isoweek.Week !
        # TODO : test holidays et jours fériés.
        UE_semaine = isoweek.Week.withdate(UE_start)
        UE_semaine_str=str(UE_semaine)
        if UE_semaine_str not in SEMAINES_UNIV:
            print("Erreur : l'évènement " + UE_summary + " du " + str(UE_start)
                  + " n'est pas dans une semaine Université ("
                  + UE_semaine_str + ")" )
            print("-> les semaines Université : " + str(SEMAINES_UNIV))
            
        # À partir de SUMMARY ~ TITLE -- intervenant -- CM
        if TER['TITLE'] in UE_summary:
            if "--" in UE_summary:
                if "--" in UE_summary[UE_summary.find("--")+3:]:
                    intervenant = UE_summary[UE_summary.find("--")+3:UE_summary.rfind("--")-1]
                else:
                    intervenant = UE_summary[UE_summary.find("--")+3:]
            else:
                intervenant = "SANS"
            # update info for TER
            if hours_bef_soutenance_TER >= datetime.timedelta(0):
                hours_bef_soutenance_TER += UE_duration

        elif RE['TITLE'] in UE_summary:
            intervenant = "SANS"
        elif Anglais['TITLE'] in UE_summary:
            intervenant = Anglais['RESP']
        elif CCNA['TITLE'] in UE_summary:
            intervenant = "RICO+BONNEVILLE"
        elif CoM["TITLE"] in UE_summary:
            intervenant = CoM['RESP']
        elif DROIT['TITLE'] in UE_summary:
            intervenant = DROIT['RESP']
        elif SPAI['TITLE'] in UE_summary:
            intervenant = SPAI['RESP']
        elif QSM['TITLE'] in UE_summary:
            intervenant = QSM['RESP']
        else:
            intervenant = UE_summary[UE_summary.find("--")+3:UE_summary.rfind("--")-1]
        if intervenant == "":
            intervenant = "Non-précisé"

        # Compte les heures en les répartissant par UE
        for i in SIR:
            if UE_summary.startswith(i['TITLE']):
                # Check requirements for RTS
                if i in COMMON:
                    checkRTS("in",i)

                # Ajoute la durée à la semaine
                # CCNA n'est pas compté dans la valeur TOT
                # WARNING: modifier ici si on veut un résumé nbh UE par semaine
                if CCNA['TITLE'] not in UE_summary:
                    key_tot_hours='TOT'
                else:
                    key_tot_hours='CCNA'
                if UE_semaine_str not in heures_par_semaine.keys():
                    heures_par_semaine[UE_semaine_str] = {}
                if key_tot_hours not in heures_par_semaine[UE_semaine_str].keys():
                    heures_par_semaine[UE_semaine_str][key_tot_hours] = UE_duration
                else:
                    heures_par_semaine[UE_semaine_str][key_tot_hours] += UE_duration
                # Calcul nbh pour TER par semaine.
                if TER['TITLE'] in UE_summary:
                    if 'TER' not in heures_par_semaine[UE_semaine_str].keys():
                        heures_par_semaine[UE_semaine_str]['TER'] = UE_duration
                    else:
                        heures_par_semaine[UE_semaine_str]['TER'] += UE_duration
                                 
                # -> vérifier quelles demi-journées sont libres et faire stats
                # TODO!
                   
                # Mise-à-jour du LAST évènement pour l'UE
                if 'LAST' not in i.keys():
                    i['LAST'] = UE_end.date()
                elif i['LAST'] < UE_end.date():
                    i['LAST'] = UE_end.date()

                # intervenant may contain '+'. Manage it?
                # pb being hours count once only...
                # if "+" in intervenant:
                # SUPPOSE 1 SEUL INTERVENANT MAIS DANS LISTE (au cas où)

                # DEBUG
                newi=0
                if intervenant not in i['INTERVENANT']:
                    i['INTERVENANT'].append( str(intervenant) )
                    i[intervenant] = { 'CM' : datetime.timedelta(0),
                                       'TD' : datetime.timedelta(0),
                                       'TP' : datetime.timedelta(0),
                                       'EXAMEN' : datetime.timedelta(0),
                                       'DATES' : {}}
                    # DEBUG
                    print("NEW:   "+str(intervenant)+"======"+str(i[intervenant]))
                    newi=1
                if UE_semaine_str not in i[intervenant]['DATES']:
                    i[intervenant]['DATES'][UE_semaine_str] = []

                if 'EXAMEN' in UE_summary or 'EXAM' in UE_summary or 'Exam' in UE_summary:
                    type_hours='EXAMEN'
                    if hours_bef_soutenance_TER >= datetime.timedelta(0):
                        hours_bef_soutenance_TER = -hours_bef_soutenance_TER
                elif 'CM' in UE_summary:
                    type_hours='CM'
                elif 'TD' in UE_summary:
                    type_hours='TD'
                elif 'TP' in UE_summary:
                    type_hours='TP'
                elif 'TER' in UE_summary:
                    type_hours='TD'
                elif 'Anglais' in UE_summary:
                    type_hours='TD'
                elif CoM['TITLE'] in UE_summary:
                    type_hours='TD'
                elif DROIT['TITLE'] in UE_summary:
                    type_hours='CM'                    
                else:
                    print(UE_summary + " does not contain its type on "
                          + str(UE_start) )
                # Update total info of UE
                i[type_hours] += UE_duration
                # Update info for intervenant
                i[intervenant][type_hours] += UE_duration
                i[intervenant]['DATES'][UE_semaine_str].append([type_hours, UE_start, UE_end])
                # DEBUG
                if newi == 1:
                    print(".. "+UE_summary+":::"+UE_semaine_str+"  "+str([type_hours, UE_start, UE_end]))

#print(RSF['IGL']['DATES']['2015W43'].items())
#sys.exit()
                
print("**************************** Analyse par UE :")
for i in SIR:
    if i == RE:
        print("RE gérée à part")
    else:
        print("UE " + i['TITLE'] + ", resp. " + i['RESP'] + " :")

        print(" - Heures à placer " +
              str(i['_CM'] + i['_TD'] + i['_TP'] + i['_EXAMEN']) + " ->"
              + " CM(" + str(i['_CM']) + ")"
              + " TD(" + str(i['_TD']) + ")"
              + " TP(" + str(i['_TP']) + ")"
              + " EXAMEN(" + str(i['_EXAMEN']) + ")")
              
        print(" - Heures placées " +
              str(i['CM'].total_seconds()/3600
                  + i['TD'].total_seconds()/3600
                  + i['TP'].total_seconds()/3600
                  + i['EXAMEN'].total_seconds()/3600) + " ->"
              + " CM(" + str(i['CM'].total_seconds()/3600) + ")"
              + " TD(" + str(i['TD'].total_seconds()/3600) + ")"
              + " TP(" + str(i['TP'].total_seconds()/3600) + ")"
              + " EXAMEN(" + str(i['EXAMEN'].total_seconds()/3600) + ")")
        ecart_heure = []
        for type_heure in ['CM', 'TD', 'TP']:
            ecart_heure.append( i["_"+type_heure] - i[type_heure].total_seconds()/3600)
        if ecart_heure != [0,0,0]:
            print("   ******************* ECART : " + str(ecart_heure))

        print(" - Interventions placées :")
        for intervenant in sorted(i['INTERVENANT']):
            if i[intervenant]['EXAMEN'].total_seconds()/3600 != 0:
                print("    * " + intervenant + " :"
                      + " CM(" + str(i[intervenant]['CM'].total_seconds()/3600) + ")"
                      + " TD(" + str(i[intervenant]['TD'].total_seconds()/3600) + ")"
                      + " TP(" + str(i[intervenant]['TP'].total_seconds()/3600) + ")"
                      + " EXAMEN(" + str(i[intervenant]['EXAMEN'].total_seconds()/3600) + ")")
            else:
                print("    * " + intervenant + " :"
                      + " CM(" + str(i[intervenant]['CM'].total_seconds()/3600) + ")"
                      + " TD(" + str(i[intervenant]['TD'].total_seconds()/3600) + ")"
                      + " TP(" + str(i[intervenant]['TP'].total_seconds()/3600) + ")")

print("**************************** Statistiques par semaine :")
heures= []
for semaine in SEMAINES_UNIV:
    chaine_print=""
#    print(heures_par_semaine[semaine].keys())
    if 'TER' in heures_par_semaine[semaine].keys():
        chaine_print+=", dont "+ str(heures_par_semaine[semaine]['TER'].total_seconds()/3600) + " de TER"
    if 'CCNA' not in heures_par_semaine[semaine].keys():
        chaine_print+=" + si CCNA : 0"
    else:
        chaine_print+=" + si CCNA " + str(heures_par_semaine[semaine]['CCNA'].total_seconds()/3600)

    print("S" + semaine + " : "
          + str(heures_par_semaine[semaine]['TOT'].total_seconds()/3600)
          + " heures présentielles" + chaine_print)
        
    heures.append( heures_par_semaine[semaine]['TOT'].total_seconds()/3600 )
    
print("**************************** Statistiques sur l'année :")
h_p_s = array( heures[1:len(heures)-1])
print("- Moyenne travaillée par semaine : " + str(h_p_s.mean()))
print("- Minimum travaillé : " + str(h_p_s.min())
      + " pour la semaine S" + SEMAINES_UNIV[ heures.index(h_p_s.min()) ] )
print("- Maximim travaillé : " + str(h_p_s.max())
      + " pour la semaine S" + SEMAINES_UNIV[ heures.index(h_p_s.max()) ] )
print("- Heures totales sur l'année : " + str(h_p_s.sum()))
print("- Heures préparation avant soutenance TER : " + str(-hours_bef_soutenance_TER.total_seconds()/3600))


print("**************************** Contraintes RTS :")
checkRTS("final", None)

print("**************************** Résumé par intervenant :")
intervenant_list = []
for i in SIR:
    for intervenant in i['INTERVENANT']:
        if intervenant not in intervenant_list:
            intervenant_list.append( intervenant )
for intervenant in sorted(intervenant_list):
#    if intervenant != 'SANS':
    if intervenant != 'mlkio':
        print(intervenant)
        for i in SIR:
            if intervenant in i['INTERVENANT']:
                if i[intervenant]['EXAMEN'].total_seconds()/3600 != 0:
                    str_exam=" EXAMEN(" + str(i[intervenant]['EXAMEN'].total_seconds()/3600) + ")"
                else:
                    str_exam=""
                
                print("  * " + i['TITLE'] + " :" +
                      " CM(" + str(i[intervenant]['CM'].total_seconds()/3600) + ")"+
                      " TD(" + str(i[intervenant]['TD'].total_seconds()/3600) + ")"+
                      " TP(" + str(i[intervenant]['TP'].total_seconds()/3600) + ")"+
                      str_exam)
                print("  Créneaux :")

                for semaine in sorted(i[intervenant]['DATES'].keys()):
                    cps=i[intervenant]['DATES'][semaine]
                    for occurrence in sorted(cps, key=lambda lesson: lesson[1]):
                        print("      " +
                          str(occurrence[0]) + ", "
                          + str((occurrence[2]-occurrence[1]).total_seconds()/3600) + ", "
                          + " le " + ict(occurrence[1],"%a") + " " + ict(occurrence[1],"%d/%m/%y") + " de " + ict(occurrence[1],"%H:%M") + " à " + ict(occurrence[2],"%H:%M"))

f.close()

