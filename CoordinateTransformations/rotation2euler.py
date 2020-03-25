import numpy as np

def rotation2euler(R, output_unit='rad'):
    """
    returns euler angles (alpha, beta and gamma) given a rotation matrix

    Parameters
    ----------
    R : np.array(3,3)
        Rotation Matrix
    output_unit : string
        unit of the output angles, 'deg' or 'rad', default to rad

    Returns
    -------
    alpha : int/float
        angle around axis
    beta : int/float
        angle around axis
    gamma : int/float
        angle around axis

    Raises
    ------
    """

    def output_deg(alpha,beta,gamma):
        """ convert rad to deg """
        return (np.rad2deg(alpha), np.rad2deg(beta),np.rad2deg(gamma))


    beta = np.arctan2(-R[2,0], np.sqrt(R[0,0]**2 + R[1,0]**2))
    if beta == np.deg2rad(90):
        alpha = 0
        gamma = np.arctan2(R[0,1], R[1,1])
        
        if output_unit=='deg':
            return output_deg(alpha,beta,gamma)
        return (alpha, beta, gamma)
        
    elif beta == np.deg2rad(-90):
        alpha = 0
        gamma = -np.arctan2(R[0,1], R[1,1])
    
        if output_unit=='deg':
            return output_deg(alpha,beta,gamma)
        return (alpha, beta, gamma)
        
    c_beta = np.cos(beta)
    alpha = np.arctan2(R[1,0]/c_beta, R[0,0]/c_beta)
    gamma = np.arctan2(R[2,1]/c_beta, R[2,2]/c_beta)


    if output_unit=='deg':
        return output_deg(alpha,beta,gamma)
    return alpha, beta, gamma
