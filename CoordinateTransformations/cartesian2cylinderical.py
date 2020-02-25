import numpy as np

def cartesian2cylindrical(x, y, z):
    """
    convert cartesian coordinates to cylindrical coordinates
    """
    
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y,x)
    return r, theta, z
