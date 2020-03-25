import numpy as np

def compound_rotations(R_AB, R_BC):
    """
    perform multiplication of rotations

    - just like adding two rotations
    - i.e. compute R_AC from the knowledge of R_AB and R_BC

    Parameters
    ----------
    R_AB : np.array(3,3)
        rotation matrix
    R_BC : np.array(3,3)
        rotation matrix

    Returns
    -------
    R_AC : np.array(3,3)
        rotation matrix

    Raises
    ------
    """

    R_AC = np.matmul(R_AB,R_BC)
    
    return R_AC
    