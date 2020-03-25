import numpy as np

def inverse_rotation(R_AB):
    """
    inverse the rotation

    i.e. given R_AB, returns R_BA 

    Parameters
    ----------
    R_AB : np.array(3,3)
        rotation matrix

    Returns
    -------
    R_BA : np.array(3,3)
        rotation matrix

    Raises
    ------
    """
    R_BA = np.transpose(R_AB)
    return R_BA
    