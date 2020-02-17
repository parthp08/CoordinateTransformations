import numpy as np
from .compound_transforms import compound_transforms

def axis_angle2rotation(vector_, theta, unit='rad', pass_through_origin=True, pass_point=np.zeros((3,1))):
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

    if not pass_through_origin:

        """
        TODO: there is an easy way of doing this 
            on page 6 of solution manual of Ref [2]

            DOCSTRING TODO

            EVERYTHING SHOULD OUTPUT T not R 
            and then avialble conversion between T and R
        """

        T_a_a_dash = np.matrix(np.eye(4))        
        T_a_a_dash[:3,3] = pass_point
        T_b_dash_b = np.matrix(np.eye(4))        
        T_b_dash_b[:3,3] = -pass_point

        R_a_dash_b_dash = axis_angle2rotation(vector_, theta, unit=unit)
        print(R_a_dash_b_dash)
        T_a_dash_b_dash = np.matrix(np.zeros((4,4)))
        T_a_dash_b_dash[3,3] = 1
        T_a_dash_b_dash[:3,:3] = R_a_dash_b_dash

        print(T_a_a_dash)
        print(T_b_dash_b)
        print(T_a_dash_b_dash)

        T_ab = compound_transforms(T_a_a_dash, compound_transforms(T_a_dash_b_dash, T_b_dash_b))

        return T_ab[:3,:3]

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
