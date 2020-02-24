import numpy as np
from .compound_rotations import compound_rotations

def compound_rotations_v2(R_arr):
    """

    Compound multiple rotations (even > 2)

    TODO
    """
    
    for i in range(1, len(R_arr)):
        if i == 1:
            R = compound_rotations(R_arr[i-1], R_arr[i])
        else:
            R = compound_rotations(R, R_arr[i])

    return R
