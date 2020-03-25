import numpy as np
from .compound_rotations import compound_rotations

def compound_rotations_v2(R_arr):
    """
    perform multiplication of rotations (even more than 2)

    - just like adding two or more rotations
    - i.e. compute R_AC from the knowledge of R_AB and R_BC

    Parameters
    ----------
    R_arr : np.array
        array of rotation matrices of same shape

    Returns
    -------
    R : np.array(3,3)
        rotation matrix

    Raises
    ------
    """
    
    for i in range(1, len(R_arr)):
        if i == 1:
            R = compound_rotations(R_arr[i-1], R_arr[i])
        else:
            R = compound_rotations(R, R_arr[i])

    return R
