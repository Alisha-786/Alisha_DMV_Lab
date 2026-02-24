import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y = np.cos(x)
plt.plot(x, y)
plt.title("Basic Line Plot of a Cosine Wave")
plt.xlabel("x-axis Value")
plt.ylabel("Y-axis Value")
plt.show()