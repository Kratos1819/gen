import numpy as np
import matplotlib.pyplot as plt


data_group1 = np.random.normal(loc=50, scale=10, size=500)
data_group2 = np.random.normal(loc=200, scale=15, size=500)


plt.hist(data_group1, label='Group 1', color='blue')
plt.hist(data_group2, label='Group 2', color='green')
plt.title("Data Distribution")
plt.xlabel("Data Values")
plt.ylabel("Frequency")
plt.legend()
plt.show()
