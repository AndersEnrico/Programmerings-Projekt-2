"""Denne kode er skrevet af Anders Enrico Krog Petersen, S224076."""

from Karakterafrundningsfunktion import roundGrade

"""
funktion tages en NxM matrice, hvor N er antal studerende og M er antal opgever. Den regner derefter gennemsnittet,
og laver det om til 7-trins skala. Hvis eleven har fået -3 i én opgave bliver dette den endelige karakter. Hvis der kun
er en opgave er dette den endelige karakter.
"""
def computeFinalGrades(grades):
    
# Laver en tom liste som vi sætter den endelige karakter ind ind
    gradesFinal = []
    
# Itterere gennem alle elever
    for student in grades:
        
# Hvis en elev har fået -3 i en eller flere opgaver er deres endelige karakter -3
        if -3 in student:
            gradesFinal.append(-3)
        
        else:
            
# Hvis M>1 fjerner den, den dårligste karakter og regner gennemsnittet
            if len(student) > 1:
                avgGrade = (sum(student) - min(student))/(len(student)-1)
                gradesFinal.append(avgGrade)
                
# Hvis eleven kun har 1 opgave, er dette den endelige karakter.
            else:
                gradesFinal.append(student[0])
    
# Laver karakteren om til 7-trins skalaen og returnerer dette.
    return roundGrade(gradesFinal)
