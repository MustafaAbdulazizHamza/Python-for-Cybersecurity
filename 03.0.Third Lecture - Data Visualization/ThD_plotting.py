import numpy as np
import matplotlib.pyplot as plt
x = np.random.random(100)
y = np.random.random(100)
z = np.random.random(100)
ax = plt.axes(projection="3d")
ax.scatter(x,y,z)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()