import matplotlib.pyplot as plt

x_pos, y_pos = 1.0, 0.0
step = 0.2

fig, ax = plt.subplots()
ax.set_xlim(0, 2 * 3.1416)
ax.set_ylim(-2, 2)

circle = plt.Circle((x_pos, y_pos), 0.15, color='blue')
ax.add_patch(circle)

def on_key(event):
    global x_pos, y_pos
    if event.key == 'up': y_pos += step
    elif event.key == 'down': y_pos -= step
    elif event.key == 'left': x_pos -= step
    elif event.key == 'right': x_pos += step
    circle.center = (x_pos, y_pos)
    fig.canvas.draw_idle()

fig.canvas.mpl_connect('key_press_event', on_key)

plt.title("Move Circle with Arrow Keys")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.show()
