from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure
ax = plt.axes (projection="3d")

'''
#dibujar elice circular
z = np.linspace(0,10,100)
x = np.sin(z)
y = np.cos(z)
ax.plot3D(x,y,z,'red')
# view points of the curve 
ax.scatter3D(x,y,z) 
'''
def f(x,y):
    return 4-x**2-y**2

x = np.linspace(-5,5,40)
y = x
X,Y = np.meshgrid(x,y)
Z = f(X,Y)
#wireframe(maya estructura metalica)
#ax.plot_wireframe(X,Y,Z)

#dibujar malla metalica a color
ax.plot_surface(X,Y,Z,cmap="viridis")

# visualize the plane
plt.show()
