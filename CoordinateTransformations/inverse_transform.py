import numpy as np

def inverse_transform(T_AB):
    """
    invert the transformation matrix
    (calculate T_BA from T_AB)

    => Ref [2] page 35-36

    Inputs
    ---------
    T_AB: np.matrix (4,4), transformation matrix

    Returns
    ---------
    T_BA: np.matrix (4,4), transformation matrix
    """

    T_BA = np.matrix(np.zeros((4,4)))
    T_BA[3,3] = 1
    
    # inverting rotation
    T_BA[:3,:3] = T_AB[:3,:3].T # transform = inverse for rotation matrices

    # inverting position
    T_BA[:3,3] = -T_BA[:3,:3]*T_AB[:3,3]

    return T_BA