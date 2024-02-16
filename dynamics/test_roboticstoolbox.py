import numpy as np
from path_roboticstoolbox import jtraj
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import time

# Define initial and final states (position, velocity)
q0 = np.array([0])  # Initial position
qf = np.array([1])  # Final position
v0 = np.array([0])  # Initial velocity
vf = np.array([0])  # Final velocity

# Define time steps
t = np.linspace(0, 10, 100)  # 10 seconds, 100 time steps

# Generate the trajectory
traj = jtraj(q0, qf, t, qd0=v0, qd1=vf)

# Plot the trajectory
plt.figure()
plt.plot(t, traj.q, label="Position")
plt.plot(t, traj.qd, label="Velocity")
plt.plot(t, traj.qdd, label="Acceleration")
plt.xlabel("Time (s)")
plt.ylabel("State")
plt.title("Motor Trajectory")
plt.legend()
plt.show()


from path_roboticstoolbox import quintic
tg = quintic(1, 2, 10)
#Trajectory created by quintic: 10 time steps x 1 axes
len(tg)
tg.q
tg.plot()
