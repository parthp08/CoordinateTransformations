import numpy as np

def T_translation(translation_vec):
    """
    Homogeneous transform matrix for given translation

    Notes
    -----
        no rotation is assumed

    Parameters
    ----------
    translation_vec : np.array(3,1)
        translation vector

    Returns
    -----------
    T : np.matrix(4,4)
        homogeneous translation matrix
    """

    T = np.mat(np.eye(4))
    T[0:3,3] += translation_vec
    return T
