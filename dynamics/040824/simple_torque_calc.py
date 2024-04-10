import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
g = 9.81  # Acceleration due to gravity in m/s^2
mass = 10.0  # Mass at the shoulder joint in kg (adjust as needed)



# Leg segment lengths in meters
length_hip_to_upper_leg = 0.137
length_upper_leg = 0.203
length_lower_leg = 0.266

# Function to calculate position based on rotation angles
def calculate_positions(shoulder_angle, hip_angle, knee_angle):
    # The hip joint extends in the XY plane
    hip_x = length_hip_to_upper_leg * np.cos(np.radians(shoulder_angle))
    hip_y = length_hip_to_upper_leg * np.sin(np.radians(shoulder_angle))
    hip_z = 0  # No elevation for the hip joint
    
    # The upper leg extends downward in the YZ plane from the hip
    knee_x = hip_x  # No change in the X position for the knee
    knee_y = hip_y + length_upper_leg * np.sin(np.radians(hip_angle))
    knee_z = hip_z + length_upper_leg * np.cos(np.radians(hip_angle))
    
    # The lower leg extends from the knee, also in the YZ plane
    leg_end_x = knee_x  # No change in the X position for the end of the leg
    leg_end_y = knee_y + length_lower_leg * np.sin(np.radians(knee_angle))
    leg_end_z = knee_z + length_lower_leg * np.cos(np.radians(knee_angle))
    
    return (hip_x, hip_y, hip_z), (knee_x, knee_y, knee_z), (leg_end_x, leg_end_y, leg_end_z)


def calculate_all_torques(shoulder_angle, hip_angle, knee_angle):
    # Calculate the positions of the joints
    (hip_pos, knee_pos, leg_end_pos) = calculate_positions(shoulder_angle, hip_angle, knee_angle)

    # Calculate the vectors from the joints to the mass (assumed at the shoulder, origin in this case)
    hip_vector = np.array(hip_pos)
    knee_vector = np.array(knee_pos)
    leg_end_vector = np.array(leg_end_pos)

    # The force due to gravity acts downward (negative z-axis)
    force_vector = np.array([0, 0, -mass * g])

    # Calculate the lever arms for the hip and knee joints
    # These are perpendicular to the force of gravity (which is straight down)
    lever_arm_shoulder = np.linalg.norm(np.cross(hip_vector, force_vector)) / np.linalg.norm(force_vector)
    lever_arm_hip = np.linalg.norm(np.cross(knee_vector - hip_vector, force_vector)) / np.linalg.norm(force_vector)
    lever_arm_knee = np.linalg.norm(np.cross(leg_end_vector - knee_vector, force_vector)) / np.linalg.norm(force_vector)

    # Calculate the torques
    torque_shoulder = lever_arm_shoulder * mass * g
    torque_hip = lever_arm_hip * mass * g
    torque_knee = lever_arm_knee * mass * g

    return torque_shoulder, torque_hip, torque_knee


# Function to plot the leg in a standing position
def plot_leg_standing(shoulder_angle, hip_angle, knee_angle):
    (hip_pos, knee_pos, leg_end_pos) = calculate_positions(shoulder_angle, hip_angle, knee_angle)
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plotting the segments
    ax.plot([0, hip_pos[0]], [0, hip_pos[1]], [0, hip_pos[2]], 'r-')  # Red line from origin to hip
    ax.plot([hip_pos[0], knee_pos[0]], [hip_pos[1], knee_pos[1]], [hip_pos[2], knee_pos[2]], 'g-')  # Upper leg
    ax.plot([knee_pos[0], leg_end_pos[0]], [knee_pos[1], leg_end_pos[1]], [knee_pos[2], leg_end_pos[2]], 'b-')  # Lower leg
    
    # Setting the plot limits
    ax.set_xlim([-0.5, 0.5])
    ax.set_ylim([-0.5, 0.5])
    ax.set_zlim([-0.5, 0.5])
    
    # Labels for clarity
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    
    # Title for context
    ax.set_title('Robotic Quadruped Leg in Default Standing Position')
    
    plt.show()

# Angles for the default standing position
shoulder_angle = 50
hip_angle = 115  
knee_angle = 225  

# Use the provided angles to calculate the torques
torque_shoulder, torque_hip, torque_knee = calculate_all_torques(shoulder_angle, hip_angle, knee_angle)
print(f"Torques at Shoulder: {torque_shoulder}, Hip: {torque_hip} Knee: {torque_knee}")

# Plot the default standing position
plot_leg_standing(shoulder_angle, hip_angle, knee_angle)

