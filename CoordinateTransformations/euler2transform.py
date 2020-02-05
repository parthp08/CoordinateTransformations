import numpy as np
from .euler2rotation import euler2rotation
from .rotation2transform import rotation2transform

def euler2transform(alpha,phi,theta,unit="rad",order="xyz"):
    """
    TODO
    """

    R = euler2rotation(alpha,phi,theta,unit=unit,order=order)
    T = rotation2transform(R)
    return T
    