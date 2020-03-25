import numpy as np
from .compound_transforms import compound_transforms

def compound_transforms_v2(T_arr):
    """
    perform multiplication of transforms (even more than 2)

    - just like adding two or more transforms
    - i.e. compute T_AC from the knowledge of T_AB and T_BC

    Parameters
    ----------
    T_arr : np.array
        array of transform matrices of same shape

    Returns
    -------
    T : np.array(4,4)
        homogeneous transform matrix

    Raises
    ------
    """
    
    for i in range(1, len(T_arr)):
        if i == 1:
            T = compound_transforms(T_arr[i-1], T_arr[i])
        else:
            T = compound_transforms(T, T_arr[i])

    return T
