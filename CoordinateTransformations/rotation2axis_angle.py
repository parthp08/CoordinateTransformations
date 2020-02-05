import numpy as np

def rotation2axis_angle(R, output_unit="rad"):
    """
    Input : Rotation matrix

    Output: axis passing through an origin and angle of rotation
    """

    #TODO: handle the case for 0 or 180 degrees

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


if __name__ == "__main__":
    R = np.array([
        [0.933, 0.067, 0.354],
        [0.067, 0.933, -0.354],
        [-0.354, 0.354, 0.866]
    ])

    R2 = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])

    print(rotation2axisangle(R))

    # print(axis_rotation(np.array([[0.1], [0.1], [0.1]]), 0, unit='deg'))
    print(axis_rotation(np.array([[0.7079377], [0.7079377], [0.0]]), 0.5236495809318287, unit='rad'))
