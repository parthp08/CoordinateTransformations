import numpy as np

def rotation_operator(R, point):
    """
    rotation matrix as an operator which will perform rotation to a 
    point or a vector

    Parameters
    ----------
    R : np.matrix(3,3)
        rotation matrix
    point : np.array(3,1)
        point in 3D space

    Returns
    -------
    P : np.array(3,1)
        new point location rotated by the rotation matrix

    Raises
    ------
    """

    point_2 = R * point
    return point_2

