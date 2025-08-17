import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

data = np.random.randint(0, 255, (10, 5))
print("Original Data:\n", data)

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)
print("Scaled Data:\n", scaled_data)