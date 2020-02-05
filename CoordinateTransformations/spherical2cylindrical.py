import numpy as np

def spherical2cylindrical(r, phi, theta):
    r_ = r*np.sin(phi)
    z = r*np.cos(phi)
    return r_, theta, z
