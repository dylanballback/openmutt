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


# Convert mm to meters for consistency
width = 203 / 1000  # Width between shoulder joints
length = 584.5 / 1000  # Length between hip joints

# The body of the quadruped is a rectangle, we define the four corners
front_left_shoulder = np.array([-width / 2, length / 2, 0])
front_right_shoulder = np.array([width / 2, length / 2, 0])
back_left_hip = np.array([-width / 2, -length / 2, 0])
back_right_hip = np.array([width / 2, -length / 2, 0])

# We can now use the `calculate_positions` function to get the positions of the legs
# Assuming the same angles for each leg for a symmetric standing position
shoulder_angle = 0  # This will likely change as the body of the quadruped will not be at 0 level
hip_angle = 135
knee_angle = 225


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


# Function to calculate the positions of all four legs
def calculate_quadruped_legs(shoulder_angle, hip_angle, knee_angle):
    # Front left leg
    fl_hip, fl_knee, fl_foot = calculate_positions(shoulder_angle, hip_angle, knee_angle)
    fl_hip += front_left_shoulder
    fl_knee += front_left_shoulder
    fl_foot += front_left_shoulder
    
    # Front right leg
    fr_hip, fr_knee, fr_foot = calculate_positions(shoulder_angle, hip_angle, knee_angle)
    fr_hip += front_right_shoulder
    fr_knee += front_right_shoulder
    fr_foot += front_right_shoulder
    
    # Back left leg
    bl_hip, bl_knee, bl_foot = calculate_positions(shoulder_angle, hip_angle, knee_angle)
    bl_hip += back_left_hip
    bl_knee += back_left_hip
    bl_foot += back_left_hip
    
    # Back right leg
    br_hip, br_knee, br_foot = calculate_positions(shoulder_angle, hip_angle, knee_angle)
    br_hip += back_right_hip
    br_knee += back_right_hip
    br_foot += back_right_hip
    
    
    
    return (fl_hip, fl_knee, fl_foot), (fr_hip, fr_knee, fr_foot), (bl_hip, bl_knee, bl_foot), (br_hip, br_knee, br_foot)

# Function to plot the entire quadruped
def plot_quadruped(shoulder_angle, hip_angle, knee_angle):
    legs_positions = calculate_quadruped_legs(shoulder_angle, hip_angle, knee_angle)
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plotting the body rectangle
    body_corners = [front_left_shoulder, front_right_shoulder, back_right_hip, back_left_hip, front_left_shoulder]
    body_corners_x = [pos[0] for pos in body_corners]
    body_corners_y = [pos[1] for pos in body_corners]
    body_corners_z = [pos[2] for pos in body_corners]
    
    # Assuming the body's centerline is aligned with the x-axis at x=0,
    # Calculate the x-offset for the front and back legs
    front_legs_x_offset = length_hip_to_upper_leg * np.cos(np.radians(shoulder_angle))
    back_legs_x_offset = length_hip_to_upper_leg * np.cos(np.radians(shoulder_angle))

    # Now apply the offset to the x-coordinates of the body corners
    body_corners_x = [
        pos[0] + front_legs_x_offset for pos in body_corners[:2]  # Apply to front left and right shoulders
    ] + [
        pos[0] + back_legs_x_offset for pos in body_corners[2:4]  # Apply to back left and right hips
    ] + [
        body_corners[0][0] + front_legs_x_offset  # Close the loop for the rectangle
    ]
        
    ax.plot(body_corners_x, body_corners_y, body_corners_z, 'k-')
    

    # Plotting each leg
    for leg in legs_positions:
        hip, knee, foot = leg
        # Plot from shoulder/hip to hip/knee
        ax.plot([hip[0], knee[0]], [hip[1], knee[1]], [hip[2], knee[2]], 'r-')
        # Plot from hip/knee to foot
        ax.plot([knee[0], foot[0]], [knee[1], foot[1]], [knee[2], foot[2]], 'b-')
        
        # Plot the joints for clarity
        ax.scatter(*hip, color='red')
        ax.scatter(*knee, color='green')
        ax.scatter(*foot, color='blue')

    # Setting the plot limits for better visualization
    ax.set_xlim([-0.5, 0.5])
    ax.set_ylim([-0.5, 0.5])
    ax.set_zlim([-0.5, 0.5])
    
    # Labels for clarity
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    
    # Title for context
    ax.set_title('Full OpenMutt Quadruped Model')
    
    plt.show()

# Plot the full quadruped
plot_quadruped(shoulder_angle, hip_angle, knee_angle)
