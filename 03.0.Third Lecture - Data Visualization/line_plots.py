import numpy as np
import matplotlib.pyplot as plt
years = [2016 + x for x in range(16)]
weights = [80,82,85,86,
           89,70,90,88,
           85,83,78,80,
           80,98,89,80]
plt.plot(years, weights, 
         color='purple')
plt.xlabel("Years")
plt.ylabel("Weights")
plt.show()
