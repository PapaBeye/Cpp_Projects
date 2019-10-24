from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, PathPatch
import mpl_toolkits.mplot3d.art3d as art3d
from itertools import count
import numpy as np
import math


def plotRing(Radius, With):
    theta = np.linspace(0, 2.*np.pi, 100)
    phi = np.linspace(0, 2*np.pi, 100)
    theta, phi = np.meshgrid(theta, phi)
    x = (Radius + With*np.cos(theta)) * np.cos(phi)
    y = (Radius + With*np.cos(theta)) * np.sin(phi)
    z = With * np.sin(theta)
    return x ,y ,z

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
ax1.set_zlim(-10,10)
x , y , z = plotRing(10, 0.1)
print(x, "\n\n\n\n\n\n\n\n\n" , y,"\n\n\n\n\n\n\n\n\n", z)
ax1.plot_surface(y, x, z, rstride=5, cstride=5, color='b', edgecolors='b')


plt.show()









