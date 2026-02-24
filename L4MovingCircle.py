import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_aspect("equal")
point, = ax.plot([], [], marker="o", markersize=10)

radius = 1
center_x, center_y = 0, 0

def update(frame_angle):
    x = center_x + radius * np.cos(frame_angle)
    y = center_y + radius * np.sin(frame_angle)
    point.set_data([x], [y])
    return point,

ani = animation.FuncAnimation(
    fig,
    update,
    frames=np.linspace(0, 2 * np.pi, 360, endpoint=False),
    interval=10,
    blit=True,
    repeat=True
)

plt.show()