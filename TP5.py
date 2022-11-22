import matplotlib.pyplot as plt

x = [-2, -1, 0, 1, 2]
y = [4, 1, 0, 1, 4]

fig, ax = plt.subplots()
ax.plot(x, y)

plt.savefig("img/carre.png")