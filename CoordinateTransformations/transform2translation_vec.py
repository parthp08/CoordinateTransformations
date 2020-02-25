import numpy as np

def transform2translation_vec(T):
    """
    gives translation_vec from T

    Parameters
    ----------
    T : np.matrix(4,4)
        homogeneous transform matrix

    Returns
    -------
    translation_vec : np.array(3,1)
        translation vector

    Raises
    ------
    """

    vector_ = T[:3,3] 
    return vector_
