import numpy as np
import matplotlib.pyplot as plt

array = np.array([1, 2, 3])
print("sum :", np.sum(array))
print("min :", np.min(array))
print("max :", np.max(array))
print("mean :", np.mean(array))
print("sqrt :", np.sqrt(array))

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.savefig("img/sin.png")
