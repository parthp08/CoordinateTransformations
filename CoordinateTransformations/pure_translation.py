def pure_translation(position, translation_vec):
    """
    pure translation of point by a vector in same coordinate frame

    => Ref [2] page 24 eq(2.9)

    Inputs
    ---------
    position: np.array (3x1), position of point in any coord frame
    translation_vec: np.array (3x1), translation vector in same coord frame

    Returns
    -----------
    tr_vec: np.array (3x1), translated position of point by trans_vec
                            in same coord frame
    """

    tr_vec = position + translation_vec
    return tr_vec