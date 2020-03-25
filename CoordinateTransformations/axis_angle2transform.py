import numpy as np
from .axis_angle2rotation import axis_angle2rotation
from .rotation2transform import rotation2transform as R2T
from .T_translation import T_translation as P2T
from .compound_transforms_v2 import compound_transforms_v2

def axis_angle2transform(vector_, theta, unit='rad', pass_through_origin=True, pass_point=np.zeros((3,1))):
    """
    Equivalent angle-axis rotation of theta angle around a unit vector in arbitrary direction

    Parameters
    ----------
    vector_ : np.array(3,1)
        unit vector
    theta : int/float
        angle of rotation
    unit : string
        unit of angle, "deg" or "rad", defaults to rad
    pass_through_origin : bool
        True if vector_ passes through orign, default to True
    pass_point : np.array(3,1)
        point of pass if vector_ not passes through origin, default to zero vector

    Returns
    --------
    T : np.array(4,4)
        homogeneous transformation matrix
    
    Raises
    ------
    """

    if not pass_through_origin:
        T_a_a_dash = P2T(pass_point)        
        T_b_dash_b = P2T(-pass_point)
        T_a_dash_b_dash = axis_angle2transform(vector_, theta, unit=unit)
        T_ab = compound_transforms_v2([T_a_a_dash, T_a_dash_b_dash, T_b_dash_b])
        return T_ab

    else:
        R = axis_angle2rotation(vector_, theta, unit=unit)
        T = R2T(R)
        return T
    