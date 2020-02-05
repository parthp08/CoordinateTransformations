import numpy as np
from .rotation2axis_angle import rotation2axis_angle

def transform2axis_angle(T, output_unit="rad"):
    """
    TODO
    """
    R = T[:3,:3]
    K_hat, theta = rotation2axis_angle(R, output_unit=output_unit)
    return K_hat, theta
    