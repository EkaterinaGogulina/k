
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

fig=plt.figure()
ax=Axes3D(fig)
v=np.linspace(0,np.pi,100)
u=np.linspace(0,2*np.pi,100)

x=np.outer(np.sin(u),np.cos(v))
y=np.outer(np.sin(u), np.sin(v))
z=np.outer(np.cos(u), np.ones(np.size(v)))
# Plot the surface
ax.plot_surface(x, y, z, color='b')

plt.show()



