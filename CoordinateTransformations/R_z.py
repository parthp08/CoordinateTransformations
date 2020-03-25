import numpy as np

def R_z(theta, unit="rad"):
    """
    Rotation about OZ-axis with theta-angle

    Parameters
    ----------
    theta : int/float
        angle of rotation
    unit : string
        unit of angle, "deg" or "rad", defaults to rad

    Returns
    -------
    R : np.array(3,3)
        rotation_matrix

    Raises
    ------
    """

    if unit.lower() == "deg":
        theta = np.deg2rad(theta)
    
    s_theta = np.sin(theta)
    c_theta = np.cos(theta)
    R = np.array([
        [c_theta,-s_theta,0],
        [s_theta,c_theta,0],
        [0,0,1]
    ])
    return R
    