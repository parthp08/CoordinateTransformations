import numpy as np

def rotation2transform(R):
    """
    TODO
    """

    T = np.mat(np.zeros((4,4)))
    T[3,3] = 1
    T[:3,:3] = R
    return T
