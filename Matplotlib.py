import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 101, 10)
y = np.random.randint(0, 50, 11)

plt.plot(x, y, "r--", label = "Graph")
plt.legend()
plt.scatter(x, y)
plt.title("Random Value")
plt.xlabel("Random x Value")
plt.ylabel("Random y Value")
plt.grid()

x = np.linspace(0, 6 * np.pi, 1000)
y1 =  (1 / 2) * np.cos(x)
y2 = np.sin(x)

plt.plot(x, y1,"--", label = "Cos")
plt.plot(x, y2, "r:", label = "Sin")
plt.legend()