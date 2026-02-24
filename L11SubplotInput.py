import matplotlib.pyplot as plt
import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

fig, axs = plt.subplots(rows, cols)

x = np.linspace(0, 2*np.pi, 100)

# Convert axs to 1D array for easy looping
axs = np.array(axs).reshape(-1)

for i in range(len(axs)):
    y = np.sin(x + i)
    axs[i].plot(x, y)
    axs[i].set_title(f"Plot {i+1}")
    axs[i].grid(True)

plt.tight_layout()
plt.show()