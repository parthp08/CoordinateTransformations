import numpy as np
from CoordinateTransformations import *


def comparing_array(A, B, tol=0.001, debugging=False):
    """
    compare two same sized array/matrix
    """

    assert np.shape(A) == np.shape(B)

    for i in range(0, np.shape(A)[0]):
        for j in range(0, np.shape(A)[1]):
            if debugging:
                print(abs(A[i,j] - B[i,j]) < tol)
            if abs(A[i,j] - B[i,j]) <= tol:
                continue
            else:
                return False
    return True

def comparing_tuple(A,B, tol=0.01):
    """
    comparing two same sized tuple
    """
    assert len(A) == len(B)
    for i in range(0,len(A)):
        if abs(A[i] - B[i]) <= tol:
            continue
        else:
            return False
    return True


def test_R_X_with_deg():
    assert comparing_array(R_x(30,unit='deg'), np.matrix([[1,0,0], [0,0.866,-0.5], [0,0.5,0.866]]))

def test_R_Y_with_deg():
    assert comparing_array(R_y(30,unit='deg'), np.matrix([[0.866,0,0.5], [0,1,0], [-0.5,0,0.866]]))

def test_R_Z_with_deg():
    assert comparing_array(R_z(30,unit='deg'), np.matrix([[0.866,-0.5,0], [0.5,0.866,0], [0,0,1]]))

def test_T_X_with_deg():
    assert comparing_array(T_x(30,unit='deg'), np.matrix([[1,0,0,0], [0,0.866,-0.5,0], [0,0.5,0.866,0], [0,0,0,1]]))

def test_T_Y_with_deg():
    assert comparing_array(T_y(30,unit='deg'), np.matrix([[0.866,0,0.5,0], [0,1,0,0], [-0.5,0,0.866,0], [0,0,0,1]]))

def test_T_Z_with_deg():
    assert comparing_array(T_z(30,unit='deg'), np.matrix([[0.866,-0.5,0,0], [0.5,0.866,0,0], [0,0,1,0], [0,0,0,1]]))

def test_transform_operator():
    T = np.matrix([[0.866,-0.5,0,10], [0.5,0.866,0,5], [0,0,1,0], [0,0,0,1]])
    p_a = np.array([[3],[7],[0]])
    assert comparing_array(T_operator(T,p_a), np.array([[9.098],[12.562],[0]]))

def test_rotation_operator():
    R = np.matrix([[0.866,-0.5,0], [0.5,0.866,0], [0,0,1]])
    p_b = np.array([[0],[2],[0]])
    assert comparing_array(R_operator(R,p_b), np.array([[-1],[1.732],[0]]))

def test_compound_rotations_v2():
    R_1 = np.matrix([[1,0,0],[0,1,0],[0,0,1]])
    R_3 = np.matrix([[1,0,0],[0,1,0],[0,0,1]])
    R_2 = np.matrix([[0.933,0.067,0.354],[0.067,0.933,-0.354],[-0.354,0.354,0.866]])
    R_ans = np.matrix([[0.933,0.067,0.354],[0.067,0.933,-0.354],[-0.354,0.354,0.866]])
    assert comparing_array(R_compound_v2([R_1,R_2,R_3]), R_ans, tol=0.01)

def test_compound_transforms_v2():
    T_1 = np.matrix([[1,0,0,1],[0,1,0,2],[0,0,1,3],[0,0,0,1]])
    T_3 = np.matrix([[1,0,0,-1],[0,1,0,-2],[0,0,1,-3],[0,0,0,1]])
    T_2 = np.matrix([[0.933,0.067,0.354,0],[0.067,0.933,-0.354,0],[-0.354,0.354,0.866,0],[0,0,0,1]])
    T_ans = np.matrix([[0.933,0.067,0.354,-1.13],[0.067,0.933,-0.354,1.13],[-0.354,0.354,0.866,0.05],[0,0,0,1]])
    assert comparing_array(T_compound_v2([T_1,T_2,T_3]), T_ans, tol=0.01)

def test_inverse_transform():
    T_AB = np.matrix([[0.866,-0.5,0,4], [0.5,0.866,0,3], [0,0,1,0], [0,0,0,1]])
    T_BA = np.matrix([[0.866,0.5,0,-4.964], [-0.5,0.866,0,-0.598], [0,0,1,0], [0,0,0,1]])
    assert comparing_array(T_inverse(T_AB), T_BA)

def test_inverse_rotation():
    R_AB = np.matrix([[0.866,-0.5,0], [0.5,0.866,0], [0,0,1]])
    R_BA = np.matrix([[0.866,0.5,0], [-0.5,0.866,0], [0,0,1]])
    assert comparing_array(R_inverse(R_AB), R_BA)

def test_pure_translation():
    p_b = np.array([1,2,3]).reshape(3,1)
    p_a_borg = np.array([1,2,3]).reshape(3,1)
    p_a = np.array([2,4,6]).reshape(3,1)
    assert comparing_array(pure_translation(p_b,p_a_borg), p_a)

def test_P2T():
    assert comparing_array(P2T(np.array([[1],[2],[3]])), np.matrix([[1,0,0,1],[0,1,0,2],[0,0,1,3],[0,0,0,1]]))

def test_RP2T():
    R = np.matrix([[0.866,-0.5,0], [0.5,0.866,0], [0,0,1]])
    p = np.array([[1],[2],[3]])
    T = np.matrix([[0.866,-0.5,0,1], [0.5,0.866,0,2], [0,0,1,3], [0,0,0,1]])
    assert comparing_array(RP2T(R,p), T)

def test_T2RP():
    R = np.matrix([[0.866,-0.5,0], [0.5,0.866,0], [0,0,1]])
    p = np.array([[1],[2],[3]])
    T = np.matrix([[0.866,-0.5,0,1], [0.5,0.866,0,2], [0,0,1,3], [0,0,0,1]])
    assert comparing_array(T2RP(T)[0], R) and comparing_array(T2RP(T)[1], p)

def test_R2Euler_deg():
    R = np.matrix([[0.866,-0.5,0], [0.5,0.866,0], [0,0,1]])
    assert comparing_tuple(R2Euler(R,output_unit='deg'), (30,0,0))

def test_R2Euler_deg_90_deg():
    R = np.matrix([[0,-0.342,0.939], [0,0.939,0.342], [-1,0,0]])
    alpha,beta,gamma = R2Euler(R, output_unit='deg')
    assert abs(beta-90)<0.01 and (abs(abs(alpha+gamma)-abs(35+15))<0.1 or abs(abs(alpha-gamma)-abs(35-15))<0.1) 

def test_R2Euler_deg_neg_90_deg():
    R = np.matrix([[0,-0.766,-0.642], [0,0.642,-0.766], [1,0,0]])
    alpha,beta,gamma = R2Euler(R, output_unit='deg')
    assert abs(beta+90)<0.01 and (abs(abs(alpha+gamma)-abs(35+15))<0.1 or abs(abs(alpha-gamma)-abs(35-15))<0.1) 

def test_Euler2R():
    R = np.matrix([[0.866,-0.5,0], [0.5,0.866,0], [0,0,1]])
    assert comparing_array(Euler2R(30,0,0,unit='deg',order='zyx'), R)
test_Euler2R()

def test_T2Euler_deg():
    T = np.matrix([[0.866,-0.5,0,4], [0.5,0.866,0,3], [0,0,1,5],[0,0,0,1]])
    assert comparing_tuple(T2Euler(T,output_unit='deg'), (30,0,0))

def test_Euler2T():
    T = np.matrix([[0.866,-0.5,0,4], [0.5,0.866,0,3], [0,0,1,5],[0,0,0,1]])
    T[:3,3] = np.array([0,0,0]).reshape(3,1) # because of no postion vec in euler angle rotation
    assert comparing_array(Euler2T(30,0,0,unit='deg',order='zyx'), T)

def test_R2T():
    R = np.matrix([[0.866,-0.5,0], [0.5,0.866,0], [0,0,1]])
    T = np.matrix([[0.866,-0.5,0,0], [0.5,0.866,0,0], [0,0,1,0],[0,0,0,1]])
    assert comparing_array(R2T(R), T)

def test_T2R():
    R = np.matrix([[0.866,-0.5,0], [0.5,0.866,0], [0,0,1]])
    T = np.matrix([[0.866,-0.5,0,4], [0.5,0.866,0,3], [0,0,1,2],[0,0,0,1]])
    assert comparing_array(T2R(T), R)

def test_T2P():
    P = np.array([4,3,2]).reshape(3,1)
    T = np.matrix([[0.866,-0.5,0,4], [0.5,0.866,0,3], [0,0,1,2],[0,0,0,1]])
    assert comparing_array(T2P(T), P)

def test_T2AxAng_deg():
    T = np.array([[0.933,0.067,0.354,0],[0.067,0.933,-0.354,0],[-0.354,0.354,0.866,0],[0,0,0,1]])
    axis, angle = T2AxAng(T,output_unit='deg')
    assert (abs(angle-30)<0.01) and comparing_array(axis, np.array([0.707,0.707,0]).reshape(3,1))

def test_R2AxAng_deg():
    T = np.array([[0.933,0.067,0.354,0],[0.067,0.933,-0.354,0],[-0.354,0.354,0.866,0],[0,0,0,1]])
    R = T[:3,:3]
    axis, angle = R2AxAng(R,output_unit='deg')
    assert (abs(angle-30)<0.01) and comparing_array(axis, np.array([0.707,0.707,0]).reshape(3,1))

def test_AxAng2T_deg_pass_origin():
    T = np.array([[0.933,0.067,0.354,0],[0.067,0.933,-0.354,0],[-0.354,0.354,0.866,0],[0,0,0,1]])
    assert comparing_array(AxAng2T(np.array([[0.707],[0.707],[0]]), 30, unit='deg'), T)

def test_AxAng2T_deg_not_pass_origin():
    T = np.array([[0.933,0.067,0.354,-1.13],[0.067,0.933,-0.354,1.13],[-0.354,0.354,0.866,0.05],[0,0,0,1]])
    vec = np.array([[0.707],[0.707],[0]])
    pass_point = np.array([1,2,3]).reshape(3,1)
    assert comparing_array(AxAng2T(vec, 30, unit='deg', pass_through_origin=False, pass_point=pass_point), T, tol=0.01)

def test_AxAng2R_deg():
    T = np.array([[0.933,0.067,0.354,-1.13],[0.067,0.933,-0.354,1.13],[-0.354,0.354,0.866,0.05],[0,0,0,1]])
    R = T[:3,:3]
    vec = np.array([[0.707],[0.707],[0]])
    pass_point = np.array([1,2,3]).reshape(3,1)
    assert comparing_array(AxAng2R(vec, 30, unit='deg'), R, tol=0.01)

def test_Screw_Z():
    T_ans = np.array([[0.866,-0.5,0,0], [0.5,0.866,0,0], [0,0,1,10],[0,0,0,1]])
    assert comparing_array(Screw_Z(10,30,unit='deg'), T_ans)

def test_Screw_X():
    T_ans = np.array([[1,0,0,10], [0,0.866,-0.5,0], [0,0.5,0.866,0], [0,0,0,1]])
    assert comparing_array(Screw_X(10,30,unit='deg'), T_ans)

