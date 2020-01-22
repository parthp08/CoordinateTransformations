# functions to work with spatial descriptions and transformations
"""
Ref: [1] Robotics: Control, Sensing, Vision and Intelligence,
         by K.S.Fu, R.C.Gonzalez, C.S.G.Lee
Ref: [2] Introduction to Robotics: Mechanics and Control, 3rd
         edition, J.J.Craig
"""

import numpy as np

def R_x(alpha, unit="rad"):
    """
    Rotation about OX-axis with alpha-angle

    => Ref [1] page 16

    Inputs
    ------------
    alpha: float, angle of rotation
    unit: string, unit of angle, "deg" or "rad"

    Returns
    -----------
    R: np.matrix (3x3), rotation_matrix
    """

    if unit.lower() == "deg":
        alpha = np.deg2rad(alpha)
    
    s_alpha = np.sin(alpha)
    c_alpha = np.cos(alpha)
    R = np.matrix([
        [1,0,0],
        [0,c_alpha,-s_alpha],
        [0,s_alpha,c_alpha]
    ])
    return R

def R_y(phi, unit="rad"):
    """
    Rotation about OY-axis with alpha-angle

    => Ref [1] page 18

    Inputs
    ------------
    phi: float, angle of rotation
    unit: string, unit of angle, "deg" or "rad"

    Returns
    -----------
    R: np.matrix (3x3), rotation_matrix
    """

    if unit.lower() == "deg":
        phi = np.deg2rad(phi)
    
    s_phi = np.sin(phi)
    c_phi = np.cos(phi)
    R = np.matrix([
        [c_phi,0,s_phi],
        [0,1,0],
        [-s_phi,0,c_phi]
    ])
    return R

def R_z(theta, unit="rad"):
    """
    Rotation about OZ-axis with alpha-angle

    => Ref [1] page 18

    Inputs
    ------------
    theta: float, angle of rotation
    unit: string, unit of angle, "deg" or "rad"

    Returns
    -----------
    R: np.matrix (3x3), rotation_matrix
    """

    if unit.lower() == "deg":
        theta = np.deg2rad(theta)
    
    s_theta = np.sin(theta)
    c_theta = np.cos(theta)
    R = np.matrix([
        [c_theta,-s_theta,0],
        [s_theta,c_theta,0],
        [0,0,1]
    ])
    return R

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

def T_x(alpha, unit="rad"):
    """
    homogeneous transformation matrix rotated around X axis by alpha angle
    (no translation is assumed)

    => Ref [2] page 28

    Inputs
    ------------
    alpha: float, angle of rotation
    unit: string, unit of angle, "deg" or "rad"

    Returns
    -----------
    T: np.matrix (4x4), homogeneous rotation matrix
    """

    T = np.matrix(np.zeros((4,4)))
    T[3,3] = 1
    T [0:3, 0:3] = R_x(alpha, unit=unit)
    return T

def T_y(phi, unit="rad"):
    """
    homogeneous transformation matrix rotated around Y axis by alpha angle
    (no translation is assumed)

    => Ref [2] page 28

    Inputs
    ------------
    phi: float, angle of rotation
    unit: string, unit of angle, "deg" or "rad"

    Returns
    -----------
    T: np.matrix (4x4), homogeneous rotation matrix
    """

    T = np.matrix(np.zeros((4,4)))
    T[3,3] = 1
    T [0:3, 0:3] = R_x(phi, unit=unit)
    return T

def T_z(theta, unit="rad"):
    """
    homogeneous transformation matrix rotated around Z axis by alpha angle
    (no translation is assumed)

    => Ref [2] page 28

    Inputs
    ------------
    theta: float, angle of rotation
    unit: string, unit of angle, "deg" or "rad"

    Returns
    -----------
    T: np.matrix (4x4), homogeneous rotation matrix
    """

    T = np.matrix(np.zeros((4,4)))
    T[3,3] = 1
    T [0:3, 0:3] = R_z(theta, unit=unit)
    return T

def T_translation(translation_vec):
    """
    Homogeneous translation matrix
    (no rotation is assumed)

    => Ref [2] page 28

    Inputs
    ------------
    translation_vec: np.array (3x1), translation vector

    Returns
    -----------
    T: np.matrix (4x4), homogeneous translation matrix
    """

    T = np.mat(np.eye(4))
    T[0:3,3] += translation_vec
    return T

def transform_operator(T, point):
    """
    transform matrix as an operator which will perform tranlation and rotation to
    a point or a vector

    Inputs
    ---------
    T: np.matrix (4x4), tranformation matrix
    point: np.array (3x1), point in 3D space

    Returns
    ----------
    P: np.array (3x1), point rotated and translated by the transformation matrix
    """

    # Rotation matrix
    R = T[:3,:3]

    # Translation vector
    TR = T[:3,3]

    # new point
    P = pure_translation(R*point, TR)
    return P

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

def inverse_transformation(T_AB):
    """
    invert the transformation matrix
    (calculate T_BA from T_AB)

    => Ref [2] page 35-36

    Inputs
    ---------
    T_AB: np.matrix (4,4), transformation matrix

    Returns
    ---------
    T_BA: np.matrix (4,4), transformation matrix
    """

    T_BA = np.matrix(np.zeros((4,4)))
    T_BA[3,3] = 1
    
    # inverting rotation
    T_BA[:3,:3] = T_AB[:3,:3].T # transform = inverse for rotation matrices

    # inverting position
    T_BA[:3,3] = (T_AB[:3,:3].T)*T_AB[:3,3]

    return T_BA

def euler_angles(alpha,phi,theta,unit="rad",order="xyz"):
    """
    rotation matrix from euler angles

    => Ref [1] page 22-25

    Inputs
    --------
    alpha: float, angle of rotation about order[0]
    phi: float, angle of rotation about order[1]
    theta: float, angle of rotation about order[2]
    unit: string, unit of angle, "deg" or "rad"
    order: string, order of rotation axis 
            avialable orders: "xyz", "zyz", "zyx"
    
    Returns
    --------
    R: np.matrix (3,3), rotation matrix
    """

    if order.lower() == "xyz":
        R = R_z(theta,unit=unit)*R_y(phi,unit=unit)*R_x(alpha,unit=unit)
    elif order.lower() == "zyz":
        R = R_z(theta,unit=unit)*R_y(phi,unit=unit)*R_z(alpha,unit=unit)
    elif order.lower() == "zyx":
        R = R_x(theta,unit=unit)*R_y(phi,unit=unit)*R_z(alpha,unit=unit)
    else:
        AssertionError("euler angle order not implemented, avialable orders: xyz, zyz, zyx")
    
    return R

def axis_rotation(vector_, theta, unit='rad', pass_through_origin=True, pass_point=np.zeros((3,1))):
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

        R_a_dash_b_dash = axis_rotation(vector_, theta, unit=unit)
        print(R_a_dash_b_dash)
        T_a_dash_b_dash = np.matrix(np.zeros((4,4)))
        T_a_dash_b_dash[3,3] = 1
        T_a_dash_b_dash[:3,:3] = R_a_dash_b_dash

        print(T_a_a_dash)
        print(T_b_dash_b)
        print(T_a_dash_b_dash)

        T_ab = compound_transforms(T_a_a_dash, compound_transforms(T_a_dash_b_dash, T_b_dash_b))

        return T_ab

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




