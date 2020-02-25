import numpy as np

def cylindrical2cartesian(r, theta, z):
    """
    convert cylindrical coordinates to cartesian coordinates
    """
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return x, y, z
    