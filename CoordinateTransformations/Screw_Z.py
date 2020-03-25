import numpy as np
from .R_z import R_z
from .RP2T import RP2T 

def Screw_Z(distance, angle, unit='rad'):
    """
    Screw motion around Z axis and with given distnace from the z-axis

    Parameters
    ----------
    distnace : int/float
        distance from the z-axis 
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

    R = R_z(angle, unit=unit)
    P = np.array([[0], [0], [distance]])
    T = RP2T(R,P)
    return T
