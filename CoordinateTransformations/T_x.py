import numpy as np
from .R_x import R_x

def T_x(alpha, unit="rad"):
    """
    homogeneous transformation matrix rotated around X axis by alpha angle
    (no translation is assumed)

    => Ref [2] page 28

    Inputs
    ------------
    alpha: float, angle of rotation
    unit: string, unit of angle, "deg" or "rad"

    Returns
    -----------
    T: np.matrix (4x4), homogeneous rotation matrix
    """

    T = np.matrix(np.zeros((4,4)))
    T[3,3] = 1
    T [0:3, 0:3] = R_x(alpha, unit=unit)
    return T
    