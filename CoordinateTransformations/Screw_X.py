import numpy as np
from .R_x import R_x
from .RP2T import RP2T 

def Screw_X(distance, angle, unit='rad'):
    """
    TODO
    """
    
    R = R_x(angle, unit=unit)
    P = np.array([[distance], [0], [0]])
    T = RP2T(R,P)
    return T
