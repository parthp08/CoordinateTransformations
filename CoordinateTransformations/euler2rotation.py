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
        choose order : "ijk" where i=x/y/z, j=x/y/z, k=x/y/z
        default to "xyz"
    
    Returns
    -------
    R : np.array(3,3)
        rotation matrix

    Raises
    ------
    """

    assert order[0]!=order[1] and order[1]!=order[2], "order choice is constrained to not have two succesive rotation with same axis such as xxy or xzz" 

    angle_list = [alpha, phi, theta]
    R = np.eye(3)
    i = 0
    for axis in order:
        if axis == 'x':
            R = np.matmul(R, R_x(angle_list[i],unit=unit))
        elif axis == 'y':
            R = np.matmul(R, R_y(angle_list[i],unit=unit))
        elif axis == 'z':
            R = np.matmul(R, R_z(angle_list[i],unit=unit))
        
        i += 1
    
    return R
