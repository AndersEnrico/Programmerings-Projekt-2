# Importere libraries
import numpy as np
from displayMenu import *
import os.path
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from EndeligKarakterFunktion import computeFinalGrades
from plotfunktion import gradesPlot
from Karakterafrundningsfunktion import roundGrade
import pandas as pd

colorama_init()

# Denne kode er skrevet af Kasper Mejer Lærche Laursen, s214496

# Definere menu muligheder
menuItems0 =np.array(['\x1b[;30;47m' + "Indlæs data" + '\x1b[0m'])
menuItems = np.array([ '\x1b[0;30;47m' + "Indlæs ny data" + '\x1b[0m', '\x1b[0;30;47m' + "Check for datafejl" + '\x1b[0m', '\x1b[0;30;47m' + "Generer diagrammer" + '\x1b[0m', '\x1b[0;30;47m' + "Vis karakterliste" + '\x1b[0m', '\x1b[0;30;47m' + "Afslut" + '\x1b[0m'])

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
        
        if check_file == True:
            print('\x1b[6;30;42m' + f'{filNavn} er indlæst korrekt.' + '\x1b[0m')
            #print('\x1b[6;30;42m' + f'Der er indlæst {studentCount} elever og {assignCount} opgaver' + '\x1b[0m')
           
            while True:
                
# Laver csv filen om til en matrice og fjerner alt andet end karakterer
                dataFile = pd.read_csv(filNavn)
                dataMatrix = np.array(dataFile)
                gradesMatrix = np.delete(dataMatrix,slice(0,2),1)
                
# Antal elever og opgaver
                studentCount = len(gradesMatrix[:,0])
                assignCount = len(gradesMatrix[0,:])
                print('\x1b[6;30;46m' + f'Der er indlæst {studentCount} elever og {assignCount} opgaver' + '\x1b[0m')
# ------------------------------------------------------------------

# Denne kode er skrevet af Kasper Mejer Lærche Laursen, s214496
                choice = displayMenu(menuItems)
# Der kan indsættes et nyt filnavn ved at genbruge koden ovenfor
                if choice == 1:
                    # Beder bruger om at skrive filnavn
                            filNavn = input("Indsæt filnavn: ")
                    # Checker om filen findes        
                            check_file = os.path.isfile(filNavn)
                            
                            if check_file == True:
                                print('\x1b[6;30;42m' + f'{filNavn} er indlæst korrekt.' + '\x1b[0m')
                                #print('\x1b[6;30;42m' + f'Der er indlæst {studentCount} elever og {assignCount} opgaver' + '\x1b[0m')
                               
                                while True:
                                    
            
                                    
                    # Laver csv filen om til en matrice og fjerner alt andet end karakterer
                                    dataFile = pd.read_csv(filNavn)
                                    dataMatrix = np.array(dataFile)
                                    gradesMatrix = np.delete(dataMatrix,slice(0,2),1)
                                    
                    # Antal elever og opgaver
                                    studentCount = len(gradesMatrix[:,0])
                                    assignCount = len(gradesMatrix[0,:])
                                    break
                            elif check_file == False:
                                        print('\x1b[0;30;41m' + f"{filNavn} eksistere ikke i mappen, eller er der tastefejl, prøv igen." + '\x1b[0m')
                                        break
                           
                    
                elif choice == 2:
                    # giver hver studienummer en værdi
                    try:
                        for students1 in range(dataMatrix.shape[0]):
                        # giver nu hver studie nummer endnu en værdi men plus  1
                            for students2 in range(students1 + 1, dataMatrix.shape[0]):
                                # der tjekkes om der på noget tidpunkt er et sted i matrixen hvor disse 2 værdier er ens
                                if dataMatrix[students1][0] == dataMatrix[students2][0]:
                                    # hvis der er 2 med samme studienummer kommer der en ValueError
                                    raise ValueError(f"Identiske id'er fundet i linje {students1+1} og {students2+1}")
                    except ValueError as error:
                                        print(f"{error}")
                    # row bliver defineret for at give error besked i hvilken række
                    for row in range(gradesMatrix.shape[0]):
                        try:
                            # der tjekkes om alle værdier er inden for intervallet på 7trins skalen
                            if ((gradesMatrix[row] >= -3).all() and (gradesMatrix[row] <= 12).all()):
                                pass
                            else:
                                # Der defineres en matrix med de værdier der er uden for intervallet
                                # Og der bliver raise en ValueError hvis karakteren ikke eksistere
                                    outOfRange = ~((gradesMatrix[row] >= -3) & (gradesMatrix[row] <= 12))
                                    outOfRangeGrades = gradesMatrix[row, outOfRange]
                                    raise ValueError(f"Karakter ikke på skalaen i række {row+1}: {outOfRangeGrades}")
            
                             
                        except ValueError as error:
                                        print(f"{error}")



#Denne kode er skrevet af Anders Enrico Krog Petersen, s224076.

# 3. Generer Plots
                elif choice == 3:
                    print(gradesPlot(gradesMatrix))

#------------------------------------------------------------------------------

# 4. Vis karakterliste


#------------------Viser afrundet karakterer fra hver opgave-------------------


                elif choice == 4:
                    print('\x1b[6;30;42m' + f'Herunder ses karakterene for alle {assignCount} opgaver:' + '\x1b[0m')

# Afrunder karakterende til 7-trinsskalen og printer dem
                    for i in range(len(gradesMatrix)):
                        for j in range(len(gradesMatrix[i])):
                            gradesMatrix[i][j] = roundGrade([gradesMatrix[i][j]])[0]
                    
# Laver en liste uden studienumre og en kun med studienumre.                 
                    noStudentNumber = np.delete(dataMatrix,0,1)
                    studentNumber = np.delete(dataMatrix,slice(1,len(dataMatrix)),1).tolist()

#Laver en liste kun med elevernes navne (ikke alfabetisk rækkefølge).
                    nonSortedNames = np.delete(noStudentNumber,slice(1,len(gradesMatrix)),1).tolist()
                    
# Indsætter studienumrene igen i listen 'nonSortedNames'.
                    for i, element in enumerate(nonSortedNames):
                        element.append(studentNumber[i])
                    
# Indsætter elevernes endelige karakter i listen 'names'.
                    for i, element in enumerate(nonSortedNames):
                        element.append(gradesMatrix[i])

# Vi konvertere nu numpy array'en til en normal list, så der ikke står "dtype=object" når det printes
                    for i, element in enumerate(nonSortedNames):
                        for j in range(len(element)):
                            if isinstance(element[j], np.ndarray):
                                element[j] = element[j].tolist()
                    
                    nonSortedNames = [[item[0], item[1][0], item[2]] for item in nonSortedNames]
                    
                    
                    print(nonSortedNames)
                    
                    
#-----------------Viser elevernes endeligere karakterer------------------------


# Sorterer matricen i alfabetisk rækkefølge efter deres navne
                    sorteretMatrix = np.sort(noStudentNumber, axis=0)
                    
# Laver en liste uden navne i og finder elevernes endelige karakter
                    noName = np.delete(sorteretMatrix,0,1)
                    final = computeFinalGrades(noName)

# Laver en numpy array kun med elevernes navne og laves om til en normal liste
                    names = np.delete(sorteretMatrix,slice(1,len(sorteretMatrix)),1).tolist()
                    
# Indsætter studienumrene igen i listen 'names'.
                    for i, element in enumerate(names):
                        element.append(studentNumber[i])
                    
# Indsætter elevernes endelige karakter i listen 'names'.
                    for i, element in enumerate(names):
                        element.append(final[i])
                    
# fjerner de firkantede paranteser, som var rundt om studienummeret
                    names = [[item[0], item[1][0], item[2]] for item in names]
                    
                    print('\x1b[6;30;42m' + 'Herunder ses elevernes endeligere karakterer:' + '\x1b[0m')
                    print(names)

#------------------------------------------------------------------------------

# 5. Afslut
                elif choice == 5:
                
                    break
                    
                    
                        
            

# Hvis filen ikke eksistere giver den fejlbesked og sender retur til hoved menu.        
        elif check_file == False:
            print('\x1b[0;30;41m' + f"{filNavn} eksistere ikke i mappen, eller er der tastefejl, prøv igen." + '\x1b[0m')
            pass
