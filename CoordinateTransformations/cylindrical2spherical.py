import numpy as np

def cylindrical2spherical(r, theta, z):
    """
    convert cylindrical coordinates to spherical coordinates
    """

    r_ = np.sqrt(r**2 + z**2)
    phi = np.arctan2(r,z)
    return r_, phi, theta
    