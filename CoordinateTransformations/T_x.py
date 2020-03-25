import numpy as np
from .R_x import R_x

def T_x(alpha, unit="rad"):
    """
    homogeneous transformation matrix rotated around X axis by alpha angle
    
    Notes
    -----
        no translation is assumed

    Parameters
    ----------
    alpha : int/float
        angle of rotation
    unit : string
        unit of angle, "deg" or "rad", defaults to rad

    Returns
    -------
    T : np.array(4,4)
        homogeneous transform matrix

    Raises
    ------
    """

    T = np.zeros((4,4))
    T[3,3] = 1
    T [0:3, 0:3] = R_x(alpha, unit=unit)
    return T
    