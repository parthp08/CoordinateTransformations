import numpy as np

def transform2rotation(T):
    """
    convert transform matrix into rotation matrix

    Parameters
    ----------
    T : np.array(4,4)
        homogeneous transform matrix

    Returns
    -------
    R : np.array(3,3)
        rotation matrix

    Raises
    ------
    """

    R = T[:3,:3]
    return R