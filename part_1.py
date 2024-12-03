import matplotlib.pyplot as plt
import numpy as np

mean = 0
std_dev = 1
num_samples = 1000
data = np.random.normal(mean, std_dev, num_samples)

plt.xlabel("x ось")
plt.ylabel("y ось")
plt.title("Тестовая гистограма")
plt.hist(data, bins=30, edgecolor='black')
plt.show()

