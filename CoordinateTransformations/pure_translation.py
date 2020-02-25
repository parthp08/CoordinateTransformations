def pure_translation(position, translation_vec):
    """
    pure translation of point by a vector in same coordinate frame

    Parameters
    ----------
    position : np.array(3,1)
        position of point in any coord frame
    translation_vec : np.array(3,1)
        translation vector in same coord frame

    Returns
    -------
    tr_vec : np.array(3,1)
        translated position of point by trans_vec
        in same coord frame
    
    Raises
    ------
    """

    tr_vec = position + translation_vec
    return tr_vec