import numpy as np

def rotation2transform(R):
    """
    convert rotation matrix into transform matrix

    Parameters
    ----------
    R : np.matrix(3,3)
        rotation matrix

    Returns
    -------
    T : np.matrix(4,4)
        homogeneous transform matrix

    Raises
    ------
    """

    T = np.mat(np.zeros((4,4)))
    T[3,3] = 1
    T[:3,:3] = R
    return T
