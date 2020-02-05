import numpy as np
from .axis_angle2rotation import axis_angle2rotation
from .rotation2transform import rotation2transform

def axis_angle2transform(vector_, theta, unit='rad', pass_through_origin=True, pass_point=np.zeros((3,1))):
    """
    TODO

    => is translation case applies here ??
    """

    R = axis_angle2rotation(vector_, theta, unit=unit, pass_through_origin=pass_through_origin, pass_point=pass_point)
    T = rotation2transform(R)
    return T
