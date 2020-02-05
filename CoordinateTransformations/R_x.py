import numpy as np

def R_x(alpha, unit="rad"):
    """
    Rotation about OX-axis with alpha-angle

    => Ref [1] page 16

    Inputs
    ------------
    alpha: float, angle of rotation
    unit: string, unit of angle, "deg" or "rad"

    Returns
    -----------
    R: np.matrix (3x3), rotation_matrix
    """

    if unit.lower() == "deg":
        alpha = np.deg2rad(alpha)
    
    s_alpha = np.sin(alpha)
    c_alpha = np.cos(alpha)
    R = np.matrix([
        [1,0,0],
        [0,c_alpha,-s_alpha],
        [0,s_alpha,c_alpha]
    ])
    return R