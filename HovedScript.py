# Importere libraries
import numpy as np
from displayMenu import *
import os.path
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from EndeligKarakterFunktion import computeFinalGrades
import pandas as pd

colorama_init()

# Denne kode er skrevet af Kasper Mejer Lærche Laursen, s224196

# Definere menu muligheder
menuItems0 =np.array(['\x1b[;30;47m' + "Indlæs data" + '\x1b[0m'])
menuItems = np.array([ '\x1b[0;30;47m' + "Check for datafejl" + '\x1b[0m', '\x1b[0;30;47m' + "Generer diagrammer" + '\x1b[0m', '\x1b[0;30;47m' + "Vis karaterliste" + '\x1b[0m', '\x1b[0;30;47m' + "Afslut" + '\x1b[0m'])

# Under menu til 'Filtrer data'.
menuItems2 = np.array(['\x1b[;37;44m' + "Type af bakterie" + '\x1b[0m', 
                       '\x1b[;37;44m' + "Interval for Vækstrate" + '\x1b[0m'])

# Under menu til 'Vis statistik'.
menuItems3 = np.array(['\x1b[;37;44m' + "Gennemsnits temperatur" + '\x1b[0m', '\x1b[0;37;44m' + "Gennemsnits vækstrate" + '\x1b[0m', '\x1b[0;37;44m' + "Std temperatur" + '\x1b[0m', '\x1b[0;37;44m' + "Std vækstrate" + '\x1b[0m', '\x1b[0;37;44m' + "Rækker" + '\x1b[0m', '\x1b[0;37;44m' + "Gennemsnit af kold vækstrate" + '\x1b[0m', '\x1b[0;37;44m' + "Gennemsnit af varm vækstrate" + '\x1b[0m'])

# Denne kode er skrevet af Anders Enrico Krog Petersen, s224076

# Start
while True:
# Viser menu valgmuligheder og beder bruger om at vælge en
    choice = displayMenu(menuItems0)
# Menu valgmulighed er valgt
# ------------------------------------------------------------------
# 1. Indlæs data
    if choice == 1:
# Beder bruger om at skrive filnavn
        filNavn = input("Indsæt filnavn: ")
# Checker om filen findes        
        check_file = os.path.isfile(filNavn)
        
# Laver csv filen om til en NxM matrice, hvor N er antale elever og M er antal opgaver,
# Og indeholder kun karakterer
        dataFile = pd.read_csv(filNavn)
        gradesMatrix = np.array(dataFile)
        gradesMatrix = np.delete(gradesMatrix,slice(0,2),1)
        
# Antal elever og opgaver.
        studentCount = len(gradesMatrix[:,0])
        assignCount = len(gradesMatrix[0,:])
        
        if check_file == True:
            print('\x1b[6;30;42m' + f'{filNavn} er indlæst korrekt.' + '\x1b[0m')
            print('\x1b[6;30;42m' + f'Der er indlæst {studentCount} elever og {assignCount} opgaver' + '\x1b[0m')
           
            while True:
# ------------------------------------------------------------------

# Denne kode er skrevet af Kasper Mejer Lærche Laursen, s224196
                 choice = displayMenu(menuItems)
# 2. Filtrer data
                 if choice == 1:
# under choice 2 laves en ny meny
                     while True:
                         
                        choice2 = displayMenu(menuItems2)
                        
                
                 elif choice2 == 2:
                     
                     break
            

# Hvis filen ikke eksistere giver den fejlbesked og sender retur til hoved menu.        
        elif check_file == False:
            print('\x1b[0;30;41m' + f"{filNavn} eksistere ikke i mappen, eller er der tastefejl, prøv igen." + '\x1b[0m')
            pass
            
            
