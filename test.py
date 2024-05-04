from SphericalFuncs import SphericalFuncs
import matplotlib.pyplot as plt
import numpy as np

a = SphericalFuncs()

phi = range(0, 3, 100)
theta = range(0, 3, 100)
print(np.meshgrid(phi, theta))

# y = [a.spherical_harmonic_real(phi, theta, 1, 1) for phi, theta in phi, theta]

