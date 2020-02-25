import numpy as np

def cartesian2spherical(x,y,z):
    """
    convert cartesian coordinates to spherical coordinates
    """

    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arctan(y/x)
    phi = np.arctan((x**2 + y**2)/z)
    return r, phi, theta

