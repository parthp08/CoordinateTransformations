import numpy as np

def inverse_transform(T_AB):
    """
    inverse the trasform matrix

    i.e. given T_AB, returns T_BA 

    Parameters
    ----------
    T_AB : np.array(4,4)
        homogeneous transform matrix

    Returns
    -------
    R_BA : np.array(4,4)
        homogeneous transform matrix

    Raises
    ------
    """

    T_BA = np.zeros((4,4))
    T_BA[3,3] = 1
    
    # inverting rotation
    T_BA[:3,:3] = T_AB[:3,:3].T # transform = inverse for rotation matrices

    # inverting position
    T_BA[:3,3] = -np.matmul(T_BA[:3,:3],T_AB[:3,3])

    return T_BA