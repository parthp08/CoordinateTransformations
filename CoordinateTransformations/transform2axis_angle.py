import numpy as np
from .rotation2axis_angle import rotation2axis_angle

def transform2axis_angle(T, output_unit="rad"):
    """
    convert transform matrix into axis-angle rotation
    
    Notes
    -----
        TODO: handle the case for 0 or 180 degrees

    Parameters
    ----------
    T : np.array(4,4)
        rotation matrix
    output_unit : string
        unit of angle, "deg" or "rad", defaults to rad

    Returns
    -------
    K_hat : np.array(3,1)
        unit vector, axis around which rotation takes place
    theta : int/float
        angle of rotation around unit vector

    Raises
    ------
    """

    R = T[:3,:3]
    K_hat, theta = rotation2axis_angle(R, output_unit=output_unit)
    return K_hat, theta
    