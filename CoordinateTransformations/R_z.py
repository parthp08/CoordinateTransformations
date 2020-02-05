import numpy as np

def R_z(theta, unit="rad"):
    """
    Rotation about OZ-axis with alpha-angle

    => Ref [1] page 18

    Inputs
    ------------
    theta: float, angle of rotation
    unit: string, unit of angle, "deg" or "rad"

    Returns
    -----------
    R: np.matrix (3x3), rotation_matrix
    """

    if unit.lower() == "deg":
        theta = np.deg2rad(theta)
    
    s_theta = np.sin(theta)
    c_theta = np.cos(theta)
    R = np.matrix([
        [c_theta,-s_theta,0],
        [s_theta,c_theta,0],
        [0,0,1]
    ])
    return R
    