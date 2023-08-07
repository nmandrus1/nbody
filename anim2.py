import matplotlib.pyplot as plt
import pandas as pd

# Load the data
data = pd.read_csv('outdata.csv')

colors = {0: 'yellow', 1: 'orange', 2: 'blue', 3: 'green', 4: 'purple'}

fig, axs = plt.subplots(3, 1, figsize=(8, 12))

for planet in data['planet'].unique():
    planet_data = data[data['planet'] == planet]
    axs[0].plot(planet_data['time'], planet_data['x'], color=colors[planet], label=planet)
    axs[1].plot(planet_data['time'], planet_data['y'], color=colors[planet], label=planet)
    axs[2].plot(planet_data['time'], planet_data['z'], color=colors[planet], label=planet)

axs[0].set_xlabel('Time')
axs[0].set_ylabel('X')
axs[0].legend()

axs[1].set_xlabel('Time')
axs[1].set_ylabel('Y')
axs[1].legend()

axs[2].set_xlabel('Time')
axs[2].set_ylabel('Z')
axs[2].legend()

plt.tight_layout()
plt.show()
