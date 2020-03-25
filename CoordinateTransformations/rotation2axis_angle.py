import numpy as np

def rotation2axis_angle(R, output_unit="rad"):
    """
    convert rotation matrix into axis-angle rotation
    
    Notes
    -----
        TODO: handle the case for 0 or 180 degrees

    Parameters
    ----------
    R : np.array(3,3)
        rotation matrix
    output_unit : string
        unit of angle, "deg" or "rad", defaults to rad

    Returns
    -------
    K_hat : np.array(3,1)
        unit vector, axis around which rotation takes place
    theta : int/float
        angle of rotation around unit vector

    Raises
    ------
    """

    # always calculate the angle between 0 to 180
    theta = np.arccos((R[0,0]+R[1,1]+R[2,2]-1)/2)

    # doesnt work for theta = 0 or 180 degrees
    K_hat = (1/(2*np.sin(theta))) * np.array([
        [R[2,1] - R[1,2]],
        [R[0,2] - R[2,0]],
        [R[1,0] - R[0,1]]
    ])

    if output_unit.lower() == "deg":
        return K_hat, np.rad2deg(theta)
    return K_hat, theta
