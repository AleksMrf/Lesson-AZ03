import matplotlib.pyplot as plt
import numpy as np

random_array = np.random.rand(5)
x = np.arange(0, 5, 1)
y = np.arange(0, 5, 1)
plt.scatter(x, y)
print(random_array)

plt.xlabel("ось Х")
plt.ylabel("ось Y")
plt.title("Диаграмма рассеяния")

plt.show()