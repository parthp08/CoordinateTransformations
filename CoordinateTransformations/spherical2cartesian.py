import numpy as np

def spherical2cartesian(r, phi, theta):
    """
    convert spherical coordinates to cartesian coordinates
    """

    x = r*np.sin(phi)*np.cos(theta)
    y = r*np.sin(phi)*np.sin(theta)
    z = r*np.cos(phi)
    return x,y,z
    