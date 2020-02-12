import numpy as np
from .R_z import R_z
from .RP2T import RP2T 

def Screw_Z(distance, angle, unit='rad'):
    """
    TODO
    """

    R = R_z(angle, unit=unit)
    P = np.array([[0], [0], [distance]])
    T = RP2T(R,P)
    return T
