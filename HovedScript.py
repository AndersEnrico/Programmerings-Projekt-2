# Importere libraries
import numpy as np
from displayMenu import *
import os.path
from DataStatistik import dataStatistics
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from BakterieAnalyse import dataLoad
from DataPlot import dataPlot
colorama_init()

# Denne kode er skrevet af Kasper Mejer Lærche Laursen, s224196

# Definere menu muligheder
menuItems = np.array(['\x1b[;30;47m' + "Indlæs data" + '\x1b[0m', '\x1b[0;30;47m' + "Filtrer data" + '\x1b[0m', '\x1b[0;30;47m' + "Vis statistik" + '\x1b[0m', '\x1b[0;30;47m' + "Generer diagrammer" + '\x1b[0m', '\x1b[0;30;47m' + "Afslut" + '\x1b[0m'])

# Under menu til 'Filtrer data'.
menuItems2 = np.array(['\x1b[;37;44m' + "Type af bakterie" + '\x1b[0m', 
                       '\x1b[;37;44m' + "Interval for Vækstrate" + '\x1b[0m'])

# Under menu til 'Vis statistik'.
menuItems3 = np.array(['\x1b[;37;44m' + "Gennemsnits temperatur" + '\x1b[0m', '\x1b[0;37;44m' + "Gennemsnits vækstrate" + '\x1b[0m', '\x1b[0;37;44m' + "Std temperatur" + '\x1b[0m', '\x1b[0;37;44m' + "Std vækstrate" + '\x1b[0m', '\x1b[0;37;44m' + "Rækker" + '\x1b[0m', '\x1b[0;37;44m' + "Gennemsnit af kold vækstrate" + '\x1b[0m', '\x1b[0;37;44m' + "Gennemsnit af varm vækstrate" + '\x1b[0m'])

# Denne kode er skrevet af Anders Enrico Krog Petersen, s224076

# Start
while True:
# Viser menu valgmuligheder og beder bruger om at vælge en
    choice = displayMenu(menuItems)
# Menu valgmulighed er valgt
# ------------------------------------------------------------------
# 1. Indlæs data
    if choice == 1:
# Beder bruger om at skrive filnavn
        filNavn = input("Indsæt filnavn: ")
        
# Checker om filen findes        
        check_file = os.path.isfile(filNavn)
        
        if check_file == True:
            print('\x1b[6;30;42m' + f'{filNavn} er indlæst korrekt.' + '\x1b[0m')
            
# Køre funktionen dataLoad og giver fejlbeskeder på fejlagtigt data            
            data = dataLoad(filNavn)
            
            pass

# Hvis filen ikke eksistere giver den fejlbesked og sender retur til hoved menu.        
        elif check_file == False:
            print('\x1b[0;30;41m' + f"{filNavn} eksistere ikke i mappen, eller er der tastefejl, prøv igen." + '\x1b[0m')
        
# ------------------------------------------------------------------

# Denne kode er skrevet af Kasper Mejer Lærche Laursen, s224196

# 2. Filtrer data
    elif choice == 2:
# under choice 2 laves en ny meny
     while True:
        choice2 = displayMenu(menuItems2)
        type1 = []
        type2 = []
        if choice2 == 1:
            Bakteriatype = input("Indsæt bakterie type:")
# Hvis bakterie typen defineres specificeres dataen til kun at tage den værdi som svare til bakterien
# denne nye data appends herefter i data
            if Bakteriatype == 'Salmonella enterica':
                for i in range(len(data)):
                    if data[i,2] == 1:
                        type1.append(data[i])
                data = np.array(type1)
            if Bakteriatype == 'Bacillus cereus':
                for i in range(len(data)):
                    if data[i,2] == 2:
                        type1.append(data[i])
                data = np.array(type1)
            if Bakteriatype == 'Listeria':
                for i in range(len(data)):
                    if data[i,2] == 3:
                        type1.append(data[i])
                data = np.array(type1)       
            if Bakteriatype == 'Brocgothrix thermosphacta':
                for i in range(len(data)):
                    if data[i,2] == 4:
                        type1.append(data[i])
                data = np.array(type1)
# hvis en af de 4 bakterier bliver skrevet forkert eller en forkert bakterie opgives opstår en fejlbesked
            if Bakteriatype not in ("Salmonella enterica", "Bacillus cereus", "Listeria", "Brocgothrix thermosphacta"):
                print('\x1b[0;30;41m' + "Bakterie ikke i dataen prøv igen." + '\x1b[0m')
                data = np.array(type1)
                
        elif choice2 == 2:
# Der sættes en øvre on en nedre grænse for vækstraten og daten appendes i data
            Upperlimit = float(input("Indsæt øvre grænse for Growthrate:"))
            Lowerlimit = float(input("Indsæt nedre grænse for Growthrate:"))
            
# Giver fejlbesked, hvis den nedre grænse er mindre end 0.
            if Lowerlimit <= 0:
                print('\x1b[0;30;41m' + "Den nedre grænse skal være større end 0." + '\x1b[0m')
                
            for i in range(len(data)):
                if (Upperlimit >= data[i,1]) and (Lowerlimit <= data[i,1]):
                    type2.append(data[i])
            data = np.array(type2)
                    
        break

# ------------------------------------------------------------------

# Denne kode er skrevet af Anders Enrico Krog Petersen, s224076

# 3. Vis statistik
    elif choice == 3:
        
        while True:
            choice3 = displayMenu(menuItems3)
            
            if choice3 == 1:
                print('\x1b[6;30;42m' + 'Gennemsnits temperaturen for dataen er: {:0.3f} Grader'.format(dataStatistics(data, 'Mean Temperature')) + '\x1b[0m')
            
            elif choice3 == 2:
                print('\x1b[6;30;42m' + 'Gennemsnits vækstraten for dataen er: {:0.3f}'.format(dataStatistics(data, 'Mean Growth rate')) + '\x1b[0m')
            
            elif choice3 == 3:
                print('\x1b[6;30;42m' + 'Standardafvigelsen af temperaturen er: {:0.3f}'.format(dataStatistics(data, 'Std Temperature')) + '\x1b[0m')
            
            elif choice3 == 4:
                print('\x1b[6;30;42m' + 'Standardafvigelsen af vækstraten er: {:0.3f}'.format(dataStatistics(data, 'Std Growth rate')) + '\x1b[0m')
            
            elif choice3 == 5:
                print('\x1b[6;30;42m' + 'Der er {0:d} rækker i dataen'.format(dataStatistics(data, 'Rows')) + '\x1b[0m')
            
            elif choice3 == 6:
                print('\x1b[6;30;42m' + 'Gennemsnitten af vækstraten for temperature mindre end 20 grader er: {:0.3f} rækker i dataen'.format(dataStatistics(data, 'Mean Cold Growth rate')) + '\x1b[0m')
            
            elif choice3 == 7:
                print('\x1b[6;30;42m' + 'Gennemsnitten af vækstraten for temperature større end 50 grader er: {:0.3f} rækker i dataen'.format(dataStatistics(data, 'Mean Hot Growth rate')) + '\x1b[0m')

            break
# ------------------------------------------------------------------

# Denne kode er skrevet af Kasper Mejer Lærche Laursen, s224196

# 4. Generer diagrammer
    elif choice == 4:
        # Plotter data med eventuel ny data
        print(dataPlot(data))
# ------------------------------------------------------------------
# 5. Afslut
    elif choice == 5:
# Slutter programmet
        break

    
