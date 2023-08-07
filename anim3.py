import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

# Load the data
data = pd.read_csv('outdata.csv')

# Set up the figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

colors = {0: 'yellow', 1: 'orange', 2: 'blue', 3: 'green', 4: 'purple'}

def animate(i):
    ax.clear()
    ax.set_xlim([-30, 30])
    ax.set_ylim([-30, 30])
    ax.set_zlim([0, max(data['time'])])
    
    for planet in data['planet'].unique():
        planet_data = data[(data['planet'] == planet) & (data['time'] == i)]
        
        # Plot the current position
        if not planet_data.empty:
            ax.scatter(planet_data['x'], planet_data['y'], planet_data['time'], c=colors[planet], label=planet, alpha=0.6)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Time')
    ax.legend()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(0, int(max(data['time'])), 100), interval=16)
plt.show()
