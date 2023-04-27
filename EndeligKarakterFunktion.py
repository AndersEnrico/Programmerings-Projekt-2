import numpy as np
from Karakterafrundingsfunktion import roundGrade

matrix = np.random.randint(-4, 15, size=(25, 10))

def computeFinalGrades(grades):
    grades = np.array(grades)
    gradesFinal = np.empty(0)
    
    for i in range(len(grades[0,:])):
        
        
        if np.where(grades[i,:] <= -3):
            gradesFinal =np.append(gradesFinal, -3)
        
        
        #if grades[i,:].index(-3):
            #gradesFinal = np.append(gradesFinal, grades[i,:])
        
        elif len(grades[i,:]) == 1:
            gradesFinal = np.append(gradesFinal, grades[i,:])
        
        elif len(grades[i,:]) > 1:
            grades = np.delete(grades[i,:], min(grades[i,:]))
            
            gradesRound = np.mean(grades[i,:])
            
            gradesFinal = np.append(gradesFinal, gradesRound)
    
    gradesFinal = roundGrade(gradesFinal)
    
    return gradesFinal

print(computeFinalGrades(matrix))