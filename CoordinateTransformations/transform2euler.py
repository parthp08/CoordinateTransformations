import numpy as np
from .rotation2euler import rotation2euler

def transform2euler(T, output_unit='rad'):
    """
    returns euler angles (alpha, beta and gamma) given a transform matrix

    Parameters
    ----------
    T : np.array(4,4)
        transform matrix
    output_unit : string
        unit of the output angles, 'deg' or 'rad', default to rad

    Returns
    -------
    alpha : int/float
        angle around axis
    beta : int/float
        angle around axis
    gamma : int/float
        angle around axis

    Raises
    ------
    """

    R = T[:3,:3]
    alpha, beta, gamma = rotation2euler(R, output_unit=output_unit)
    return alpha, beta, gamma
    