import numpy as np

def T2RP(T):
    """
    convert transform matrix into rotation matrix and translation vector

    Parameters
    ----------
    T : np.matrix(4,4)
        homogeneous transform matrix

    Returns
    -------
    R : np.matrix(3,3)
        rotation matrix
    P : np.array(3,1)
        translation vector

    Raises
    ------
    """
    R = T[:3,:3]
    P = T[:3,3]
    return R,P
