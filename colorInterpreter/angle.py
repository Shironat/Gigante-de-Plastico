import numpy as np
import math

def calcular(A, B, C):
    BA = np.array(A) - np.array(B)
    BC = np.array(C) - np.array(B)

    produto = np.dot(BA, BC)
    norma_BA = np.linalg.norm(BA)
    norma_BC = np.linalg.norm(BC)

    if norma_BA == 0 or norma_BC == 0:
        return 0

    cos_angulo = produto / (norma_BA * norma_BC)
    cos_angulo = np.clip(cos_angulo, -1.0, 1.0)

    return math.degrees(math.acos(cos_angulo))
