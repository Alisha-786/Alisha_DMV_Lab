import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
x = np.arange(0, 2 * np.pi, 0.01)
line, = ax.plot(x, np.sin(x))  
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.1, 1.1)


def animate(i):
    """
    Updates the y-data of the line for each frame 'i'.
    'i' is the frame number passed by FuncAnimation.
    """
    line.set_ydata(np.sin(x + i / 50.0)) 
    return line,  

ani = animation.FuncAnimation(
    fig,           
    animate,       
    interval=20,   
    blit=True      
)

plt.show()