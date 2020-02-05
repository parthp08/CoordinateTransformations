import numpy as np
# from .pure_translation import pure_translation
from pure_translation import pure_translation

def transform_operator(T, point):
    """
    transform matrix as an operator which will perform tranlation and rotation to
    a point or a vector

    Inputs
    ---------
    T: np.matrix (4x4), tranformation matrix
    point: np.array (3x1), point in 3D space

    Returns
    ----------
    P: np.array (3x1), point rotated and translated by the transformation matrix
    """

    # Rotation matrix
    R = T[:3,:3]

    # Translation vector
    TR = T[:3,3]

    # new point # apply rotation and then translation
    P = pure_translation(R*point, TR)
    return P