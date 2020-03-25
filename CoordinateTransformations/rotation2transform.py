import numpy as np

def rotation2transform(R):
    """
    convert rotation matrix into transform matrix

    Parameters
    ----------
    R : np.array(3,3)
        rotation matrix

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
    return T
