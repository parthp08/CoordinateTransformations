import numpy as np

def axis_angle2rotation(vector_, theta, unit='rad'):
    """
    Equivalent angle-axis rotation

    => Ref [2] page 46

    Inputs
    ---------
    vector_: np.array (3,1), general vector
    theta: float, angle of rotation
    unit: string, unit of angle, "deg" or "rad"

    Returns
    --------
    R: np.matrix (3,3), rotation matrix
    """

    if unit.lower() == "deg":
        theta = np.deg2rad(theta)

    # forming unit vector
    K = vector_ / np.linalg.norm(vector_)

    c_theta = np.cos(theta)
    s_theta = np.sin(theta)
    v_theta = 1 - c_theta

    kx,ky,kz = K[0,0], K[1,0], K[2,0]

    R = np.matrix([
        [(kx**2)*v_theta + c_theta, kx*ky*v_theta - kz*s_theta, kx*kz*v_theta + ky*s_theta],
        [kx*ky*v_theta + kz*s_theta, (ky**2)*v_theta + c_theta, ky*kz*v_theta - kx*s_theta],
        [kx*kz*v_theta - ky*s_theta, ky*kz*v_theta + kx*s_theta, (kz**2)*v_theta + c_theta]
    ])

    return R
