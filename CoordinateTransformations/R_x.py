import numpy as np

def R_x(alpha, unit="rad"):
    """
    Rotation about OX-axis with alpha-angle

    Parameters
    ----------
    alpha : int/float
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
        alpha = np.deg2rad(alpha)
    
    s_alpha = np.sin(alpha)
    c_alpha = np.cos(alpha)
    R = np.array([
        [1,0,0],
        [0,c_alpha,-s_alpha],
        [0,s_alpha,c_alpha]
    ])
    return R