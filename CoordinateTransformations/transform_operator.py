import numpy as np
from .pure_translation import pure_translation

def transform_operator(T, point):
    """
    transform matrix as an operator which will perform tranlation and rotation to
    a point or a vector

    Parameters
    ----------
    T : np.array(4,4)
        tranform matrix
    point : np.array(3,1)
        point in 3D space

    Returns
    -------
    P : np.array(3,1)
        new point location rotated and translated by the transform matrix

    Raises
    ------
    """

    # Rotation matrix
    R = T[:3,:3]

    # Translation vector
    TR = T[:3,3].reshape(3,1)

    # new point # apply rotation and then translation
    P = pure_translation(np.matmul(R,point), TR)
    return P