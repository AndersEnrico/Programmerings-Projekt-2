    
import numpy as np

def beamDeflection(positions, beamLength, loadPosition, loadForce, beamSupport):
    I = 0.001 
    E = 200*10**9
    x = positions 
    l = beamLength
    a = loadPosition
    W = loadForce
    deflection = np.empty(len(x))

    if beamSupport == "both":
        if x[0] < a:
            deflection = (W * (l - a) * x) / (6 * E * I * l) * (l ** 2 - x ** 2 - (l - a) ** 2)

        elif x[0] >= a:
            deflection = (W * a * (l - x)) / (6 * E * I * l) * (l ** 2 - (l - x) ** 2 - a ** 2)
    elif beamSupport == "cantilever":
        if x[0] < a :
            deflection = (W * x ** 2) / (6 * E * I) * (3 * a - x)
        elif x[0] >= a :
            deflection = (W * a ** 2) / (6 * E * I) * (3 * x - a)
    else:
        raise ValueError("Invalid beam support. Must be 'both' or 'cantilever'.")

    return deflection
print()