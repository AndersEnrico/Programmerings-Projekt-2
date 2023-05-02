#Denne kode er skrevet af Kasper Mejer Lærche Laursen s214496.
def roundGrade(grades):
    # laves in liste som de nye karaktere bliver sat ind i
    gradesRounded = []
    # afrunder hver karakter til den nærmste karakter på 7 trins skalaen 
    # og appender denne nye karakter i gradesRounded
    for en_grade in grades:
        if en_grade < -1.5:   
            gradesRounded.append(-3)
        elif en_grade < 1:
            gradesRounded.append(0)
        elif en_grade < 3:
            gradesRounded.append(2)
        elif en_grade < 5.5:
            gradesRounded.append(4)
        elif en_grade < 8.5:
            gradesRounded.append(7)
        elif en_grade < 11:
            gradesRounded.append(10)
        else:
            gradesRounded.append(12)
    return gradesRounded
