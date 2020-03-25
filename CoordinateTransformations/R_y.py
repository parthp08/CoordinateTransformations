import numpy as np

def R_y(phi, unit="rad"):
    """
    Rotation about OY-axis with phi-angle

    Parameters
    ----------
    phi : int/float
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
        phi = np.deg2rad(phi)
    
    s_phi = np.sin(phi)
    c_phi = np.cos(phi)
    R = np.array([
        [c_phi,0,s_phi],
        [0,1,0],
        [-s_phi,0,c_phi]
    ])
    return R
    