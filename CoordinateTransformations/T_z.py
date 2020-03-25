import numpy as np
from .R_z import R_z

def T_z(theta, unit="rad"):
    """
    homogeneous transformation matrix rotated around Z axis by theta angle
    
    Notes
    -----
        no translation is assumed

    Parameters
    ----------
    theta : int/float
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
    T [0:3, 0:3] = R_z(theta, unit=unit)
    return T
