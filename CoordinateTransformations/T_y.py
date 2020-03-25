import numpy as np
from .R_y import R_y

def T_y(phi, unit="rad"):
    """
    homogeneous transformation matrix rotated around Y axis by phi angle
    
    Notes
    -----
        no translation is assumed

    Parameters
    ----------
    phi : int/float
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
    T [0:3, 0:3] = R_y(phi, unit=unit)
    return T