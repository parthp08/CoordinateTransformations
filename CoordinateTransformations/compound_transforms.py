import numpy as np

def compound_transforms(T_AB, T_BC):
    """
    perform multiplication of transforms

    - just like adding two transforms
    - i.e. compute T_AC from the knowledge of T_AB and T_BC

    Parameters
    ----------
    T_AB : np.array(4,4)
        transform matrix
    T_BC : np.array(4,4)
        transform matrix

    Returns
    -------
    T_AC : np.array(4,4)
        homogeneous transform matrix

    Raises
    ------
    """

    T_AC = np.zeros((4,4))
    T_AC[3,3] = 1

    # for rotation addition(multiplication)
    T_AC[:3,:3] = np.matmul(T_AB[:3,:3],T_BC[:3,:3])
    
    # for translation
    T_AC[:3,3] = (np.matmul(T_AB[:3,:3],T_BC[:3,3])).reshape(3,) + T_AB[:3,3]

    return T_AC
    