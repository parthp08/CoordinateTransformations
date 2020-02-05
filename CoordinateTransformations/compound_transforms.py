import numpy as np

def compound_transforms(T_AB, T_BC):
    """
    perform multiplication of transforms
    (like adding two transformation)
    (compute T_AC from the knowledge of T_AB and T_BC)

    => Ref [2] page 34-45

    Inputs
    ---------
    T_AB: np.matrix (4,4), transformation matrix
    T_BC: np.matrix (4,4), transformation matrix

    Returns
    ---------
    T_AC: np.matrix (4,4), transformation matrix
    """
    T_AC = np.matrix(np.zeros((4,4)))
    T_AC[3,3] = 1

    # for rotation addition(multiplication)
    T_AC[:3,:3] = T_AB[:3,:3]*T_BC[:3,:3]
    
    # for translation
    T_AC[:3,3] = (T_AB[:3,:3]*T_BC[:3,3]) + T_AB[:3,3]

    return T_AC
    