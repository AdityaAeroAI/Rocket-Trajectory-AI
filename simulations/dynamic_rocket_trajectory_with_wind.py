# -*- coding: utf-8 -*-
"""Dynamic_Rocket_Trajectory_With_Wind

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ylwm-zEWgdrChF553g40koAyIteuq-hd
"""

import numpy as np
import matplotlib.pyplot as plt

g = 9.81
thrust = 30000
mass = 1000
dt = 0.1
time_total = 20

wind_velocity = 5

time = np.arange(0, time_total, dt)
velocity_x = 0
velocity_y = 1  # give small initial upward velocity
position_x = 0
position_y = 0

positions_x = []
positions_y = []

for t in time:
    acceleration_y = (thrust / mass) - g
    acceleration_x = wind_velocity * 0.1

    velocity_x += acceleration_x * dt
    velocity_y += acceleration_y * dt

    position_x += velocity_x * dt
    position_y += velocity_y * dt

    positions_x.append(position_x)
    positions_y.append(position_y)

    if position_y <= 0 and t > 0:
        break

print(f"Max altitude: {max(positions_y):.2f} m")
print(f"Horizontal distance: {positions_x[-1]:.2f} m")

plt.plot(positions_x, positions_y)
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Altitude (m)')
plt.title('Rocket Trajectory with Wind Disruption')
plt.grid()
plt.show()
