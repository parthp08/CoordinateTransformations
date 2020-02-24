import numpy as np

def T2RP(T):
    """
    TODO
    """
    R = T[:3,:3]
    P = T[:3,3]
    return R,P
