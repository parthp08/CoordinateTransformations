import numpy as np

def T_translation(translation_vec):
    """
    Homogeneous translation matrix
    (no rotation is assumed)

    => Ref [2] page 28

    Inputs
    ------------
    translation_vec: np.array (3x1), translation vector

    Returns
    -----------
    T: np.matrix (4x4), homogeneous translation matrix
    """

    T = np.mat(np.eye(4))
    T[0:3,3] += translation_vec
    return T
