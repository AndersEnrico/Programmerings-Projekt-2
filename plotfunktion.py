#Denne kode er skrevet af Anders Enrico Krog Petersen, S224076.

import matplotlib.pyplot as plt
import numpy as np
from Karakterafrundningsfunktion import roundGrade
from EndeligKarakterFunktion import computeFinalGrades

""" Denne funktion plotter alle de karaktere som er givet for hver opgave.
Der tilføjes tilfældig +/- 0.1 i støj til hvert data punkt i x og y, så der
kan ses forskel på nærtliggende data punkter. """
def gradesPlot(grades):
    
# Laver en variabel for antalet af elever og antal opgaver.
    assignments = len(grades[0,:])
    students = len(grades[:,0])
    
# Afrunder karakterene med roundGrade funktionen.    
    for i in range(len(grades)):
        for j in range(len(grades[i])):
            grades[i][j] = roundGrade([grades[i][j]])[0]
    
# Laver plot at hver karakter for hver opgave, med +/- 0.1 i støj, så der kan ses forskel.
    for i in range(assignments):
        xValues = np.full(students, i+1) + np.random.uniform(-0.1, 0.1, size=students)
        yValues = grades[:, i] + np.random.uniform(-0.1, 0.1, size=students)
        plt.plot(xValues, yValues, '.', color='blue')
    
    
# Laver plot for gennemsnits karakteren.
    avgGrade = np.mean(grades, axis=0)
    avgGrade = roundGrade(avgGrade)
    plt.plot(np.arange(1, assignments+1), avgGrade, color='red', label='Average Grade')
    
 #----------------------Layout & instillinger af plot--------------------------
    
# Sætter placeringen af signaturforklaringen.
    ax = plt.subplot(111)
    
# Skrumper den nuværende axes højde med 10% i bunden
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])
    # Put a legend below current axis
    ax.legend(loc='upper right', bbox_to_anchor=(1, -0.07),
          fancybox=True, shadow=True, ncol=5, fontsize='8')
    
# Laver y-aksens værdier og spreder dem jævnt ud
    yTickValues = [-3, 0, 2, 4, 7, 10, 12]
    yTicks = np.linspace(min(yTickValues), max(yTickValues), len(yTickValues))

# Laver x-aksens værdier til at går fra 1 til antallet af opgaver og lader den stige med 1
    xTicks = range(1,len(grades[0])+1)
    
# Font til overskrift (font1) og aksetitler (font2)
    font1 = {'family':'serif','color':'blue','size':15}
    font2 = {'family':'serif','color':'darkred','size':10}
    
# Plot layout instillinger
    plt.xticks(xTicks)
    plt.yticks(yTicks, ["-3", '00', '02', '4', '7', '10', '12'])
    plt.title("Grades per assignment", fontdict = font1)
    plt.xlabel("Assignment", fontdict = font2)
    plt.ylabel("Grades", fontdict = font2)

# Vis plottet
    plt.show()
    
#Denne kode er skrevet af Kasper Mejer Lærche Laursen, s214496.
# første bliver karakteren afrundet
    grades = computeFinalGrades(grades)
    # størrelse of font på plottet
    plt.figure(figsize=(8, 5))
    font1 = {'family': 'serif', 'color': 'blue', 'size': 15}
    font2 = {'family': 'serif', 'color': 'darkred', 'size': 10}

    # tæller antallet af tilfælde hvor eleverne har fået en bestem karakter
    antal_karakter = [np.count_nonzero(np.array(grades) == -3), 
         np.count_nonzero(np.array(grades) == 0), 
         np.count_nonzero(np.array(grades) == 2),
         np.count_nonzero(np.array(grades) == 4),
         np.count_nonzero(np.array(grades) == 7),
         np.count_nonzero(np.array(grades) == 10),
         np.count_nonzero(np.array(grades) == 12)]
    # Opretter søjle diagram
    plt.bar([-3, 0, 2, 4, 7, 10, 12], antal_karakter)

    # Tilføj labels til søjler
    plt.xticks([-3, 0, 2, 4, 7, 10, 12], ["-3", '0', '2', '4', '7', '10', '12'], fontdict=font2)
    plt.ylabel("Antal af Karakter", fontdict=font2)
    plt.title("Karakter", fontdict=font1)

    # Vis søjle-diagrammer
    plt.show()
    
    
