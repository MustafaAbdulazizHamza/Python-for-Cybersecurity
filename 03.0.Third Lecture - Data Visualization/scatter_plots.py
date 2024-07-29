import numpy as np
import matplotlib.pyplot as plt
x_data = np.random.random(50) 
y_data = np.random.random(50) 
plt.scatter(x_data, y_data, c='blue')
plt.title("Scatter Plot")
plt.xlabel("X Data")
plt.ylabel("Y Data")
plt.show()