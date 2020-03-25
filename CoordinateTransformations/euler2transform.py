import numpy as np
from .euler2rotation import euler2rotation
from .rotation2transform import rotation2transform

def euler2transform(alpha,phi,theta,unit="rad",order="xyz"):
    """
    homogeneous transform matrix from given euler angles

    Parameters
    ----------
    alpha : int/float
        angle of rotation about order[0]
    phi : int/float
        angle of rotation about order[1]
    theta : int/float
        angle of rotation about order[2]
    unit : string
        unit of angle, "deg" or "rad", default to rad
    order : string
        order of rotation axis, 
        avialable orders: "xyz", "zyz", "zyx",
        default to "xyz"
    
    Returns
    -------
    T : np.array(4,4)
        transform matrix

    Raises
    ------
    AssertionError
        if order is out of the avialable orders list
    """

    R = euler2rotation(alpha,phi,theta,unit=unit,order=order)
    T = rotation2transform(R)
    return T
    