import matplotlib.pyplot as plt

x = [0.2, 0.3, 0.4]
y = [0.2, 0.25, 0.2]

plt.plot(x, y, marker='o', linewidth=2)

plt.scatter(x[0], y[0], s=100, label="Start Point")
plt.scatter(x[-1], y[-1], s=100, label="End Point")

plt.title("Robotic Arm Path Planning")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.grid(True)
plt.legend()

plt.show()