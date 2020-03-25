import numpy as np

def RP2T(R, P):
    """
    convert rotation matrix and translation vector into transform matrix

    Parameters
    ----------
    R : np.array(3,3)
        rotation matrix
    P : np.array(3,1)
        translation vector

    Returns
    -------
    T : np.array(4,4)
        homogeneous transform matrix

    Raises
    ------
    """

    T = np.zeros((4,4))
    T[3,3] = 1
    T[:3,:3] = R
    T[:3,3] = P.reshape(3,)
    return T
    