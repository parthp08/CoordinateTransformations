import numpy as np

def R_y(phi, unit="rad"):
    """
    Rotation about OY-axis with alpha-angle

    => Ref [1] page 18

    Inputs
    ------------
    phi: float, angle of rotation
    unit: string, unit of angle, "deg" or "rad"

    Returns
    -----------
    R: np.matrix (3x3), rotation_matrix
    """

    if unit.lower() == "deg":
        phi = np.deg2rad(phi)
    
    s_phi = np.sin(phi)
    c_phi = np.cos(phi)
    R = np.matrix([
        [c_phi,0,s_phi],
        [0,1,0],
        [-s_phi,0,c_phi]
    ])
    return R
    