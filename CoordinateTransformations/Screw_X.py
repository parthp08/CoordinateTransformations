import numpy as np
from .R_x import R_x
from .RP2T import RP2T 

def Screw_X(distance, angle, unit='rad'):
    """
    Screw motion around X axis and with given distnace from the x-axis

    Parameters
    ----------
    distnace : int/float
        distance from the x-axis 
    alpha : int/float
        angle of rotation
    unit : string
        unit of angle, "deg" or "rad", defaults to rad

    Returns
    -------
    T : np.array(4,4)
        homogeneous rotation matrix

    Raises
    ------
    """
    
    R = R_x(angle, unit=unit)
    P = np.array([[distance], [0], [0]])
    T = RP2T(R,P)
    return T
