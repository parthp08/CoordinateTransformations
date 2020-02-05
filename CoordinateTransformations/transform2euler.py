import numpy as np
from .rotation2euler import rotation2euler

def transform2euler(T, output_unit='rad'):
    """
    TODO
    """

    R = T[:3,:3]
    alpha, beta, gamma = rotation2euler(R, output_unit=output_unit)
    return alpha, beta, gamma
    