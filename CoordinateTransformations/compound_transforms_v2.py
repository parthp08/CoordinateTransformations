import numpy as np
from .compound_transforms import compound_transforms

def compound_transforms_v2(T_arr):
    """

    Compound transform multiple transforms (even > 2)

    TODO
    """
    T = np.matrix(np.zeros((4,4)))
    T[3,3] = 1

    for i in range(1, len(T_arr)-1):
        if i == 1:
            T = compound_transforms(T_arr[i-1], T_arr[i])
        else:
            T = compound_transforms(T, T_arr[i])

    return T
