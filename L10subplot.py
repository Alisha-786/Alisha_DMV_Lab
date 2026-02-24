import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)

y1 = np.sin(x)
y2 = np.cos(x)

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Sine Wave")

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Cosine Wave")

plt.tight_layout()
plt.show()