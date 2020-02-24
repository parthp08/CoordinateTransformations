import numpy as np
from .R_y import R_y

def T_y(phi, unit="rad"):
    """
    homogeneous transformation matrix rotated around Y axis by alpha angle
    (no translation is assumed)

    => Ref [2] page 28

    Inputs
    ------------
    phi: float, angle of rotation
    unit: string, unit of angle, "deg" or "rad"

    Returns
    -----------
    T: np.matrix (4x4), homogeneous rotation matrix
    """

    T = np.matrix(np.zeros((4,4)))
    T[3,3] = 1
    T [0:3, 0:3] = R_y(phi, unit=unit)
    return T