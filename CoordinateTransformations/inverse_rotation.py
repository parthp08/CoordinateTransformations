import numpy as np

def inverse_rotation(R_AB):
    """
    TODO
    """
    R_BA = np.linalg.inv(R_AB)
    return R_BA
    