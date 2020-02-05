import numpy as np

def cylindrical2cartesian(r, theta, z):
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return x, y, z
    