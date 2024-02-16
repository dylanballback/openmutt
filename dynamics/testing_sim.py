from roboticstoolbox import DHRobot, RevoluteMDH, jtraj
import numpy as np

# Define the link lengths as provided
L1, L2, L3, L4 = 0.08814, 0.066625, 0.2, 0.2

# Define the robot using MDH parameters
robot = DHRobot([
    RevoluteMDH(a=0, alpha=np.deg2rad(0), d=L1, offset=0),
    RevoluteMDH(a=0, alpha=np.deg2rad(90), d=0, offset=0),
    RevoluteMDH(a=L2, alpha=0, d=0, offset=0),
    RevoluteMDH(a=L3, alpha=0, d=0, offset=0),
    RevoluteMDH(a=L4, alpha=0, d=0, offset=0)
], name='Custom Robot')

# Define the zero configuration for the robot
q_zero = np.zeros(5)  # Five joints with zero angles

# Visualize the robot at the zero configuration
robot.plot(q_zero)

# Define the start and end configurations for the trajectory
q_start = np.zeros(5)  # All joints at zero position
q_end = np.array([np.pi/2, -np.pi/4, np.pi/4, -np.pi/4, np.pi/2])  # Desired end configuration

# Generate the trajectory using jtraj
t = np.linspace(0, 10, 100)  # Simulate for 10 seconds
traj = jtraj(q_start, q_end, t)

# Simulate the robot movement
for q in traj.q:
    robot.plot(q)