import numpy as np

def RP2T(R, P):
    """
    TODO
    """

    T = np.matrix(np.zeros((4,4)))
    T[3,3] = 1
    T[:3,:3] = R
    T[:3,3] = P
    return T
    