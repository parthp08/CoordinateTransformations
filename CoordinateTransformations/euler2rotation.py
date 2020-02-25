import numpy as np
from .R_x import R_x
from .R_y import R_y
from .R_z import R_z

def euler2rotation(alpha,phi,theta,unit="rad",order="xyz"):
    """
    rotation matrix from given euler angles

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
    R : np.matrix(3,3)
        rotation matrix

    Raises
    ------
    AssertionError
        if order is out of the avialable orders list
    """

    if order.lower() == "xyz":
        R = R_x(alpha,unit=unit)*R_y(phi,unit=unit)*R_z(theta,unit=unit)
    elif order.lower() == "zyz":
        R = R_z(alpha,unit=unit)*R_y(phi,unit=unit)*R_z(theta,unit=unit)
    elif order.lower() == "zyx":
        R = R_z(alpha,unit=unit)*R_y(phi,unit=unit)*R_x(theta,unit=unit)
    else:
        AssertionError("euler angle order not implemented, avialable orders: xyz, zyz, zyx")
    
    return R
