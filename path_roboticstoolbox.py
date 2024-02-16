import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from roboticstoolbox import mstraj
import pyodrivecan

import time

# Define path to database for pyodrivecan package.
database = pyodrivecan.OdriveDatabase('odrive_data.db')

position_list = []

def get_raw_position_over_time(trial_id, node_id):
    """
    Fetches raw position and time data for a given trial_id and node_id from the database.

    Parameters:
    - trial_id (int): The trial ID to filter the data.
    - node_id (int): The node ID to filter the data.

    Returns:
    - tuple: (times, positions, trial_id, node_id) where times and positions are lists of recorded data.
             Returns None for times and positions if no data is found.
    """
    # SQL query to select time and position for a specific trial_id and node_id
    sql = """
    SELECT time, position FROM ODriveData
    WHERE trial_id = ? AND node_ID = ?
    ORDER BY time;
    """
    # Execute the query and fetch all results
    results = database.fetch(sql, (trial_id, node_id))
    
    # If results are empty, inform the user and return None
    if not results:
        print("No data found for the given trial_id and node_id.")
        return

    # Unpack the results into separate lists
    times, positions = zip(*results)
    return times, positions, trial_id, node_id


def generate_trajectory_with_mstraj(recorded_positions, dt, tacc, qdmax=None, plot=False):
    """
    Generates a trajectory using mstraj, fitting the recorded path with smooth acceleration and deceleration.

    Parameters:
    - recorded_positions (list): The recorded positions to be used as via points.
    - dt (float): Time step for the generated trajectory.
    - tacc (float): Acceleration time (seconds) for the trajectory.
    - qdmax (float or array_like): Maximum speed, optional.

    Returns:
    - A tuple containing the times, positions, velocities, and accelerations for the trajectory.
    """
    # Create via points from recorded positions, reshaping to 2D array as required by mstraj
    viapoints = np.array(recorded_positions).reshape(-1, 1)

    # Generate the trajectory using mstraj
    traj = mstraj(viapoints, dt=dt, tacc=tacc, qdmax=qdmax, verbose=True)

    # Extract the positions from the trajectory
    positions = traj.q

    # Numerically differentiate positions to get velocities and accelerations
    velocities = np.gradient(positions[:, 0], dt)
    accelerations = np.gradient(velocities, dt)

    if plot:     
        # Plotting the results
        plt.figure(figsize=(12, 8))

        # Plot the trajectory positions
        plt.subplot(3, 1, 1)
        plt.plot(traj.t, positions, label='Trajectory Position')
        plt.title('Trajectory Position vs. Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Position (revs)')
        plt.legend()

        # Plot the trajectory velocities
        plt.subplot(3, 1, 2)
        plt.plot(traj.t, velocities, label='Trajectory Velocity')
        plt.title('Trajectory Velocity vs. Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Velocity (rev/s)')
        plt.legend()

        # Plot the trajectory accelerations
        plt.subplot(3, 1, 3)
        plt.plot(traj.t, accelerations, label='Trajectory Acceleration')
        plt.title('Trajectory Acceleration vs. Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Acceleration (rev/s²)')
        plt.legend()

        plt.tight_layout()
        plt.show()

    return traj.t, positions, velocities, accelerations


# Function to send positions to the motor
def send_positions_to_motor(recorded_positions, total_time, tacc, qdmax=None):
    """
    Sends the position commands to the motor to repeat the path.

    Parameters:
    - recorded_positions (list): The recorded positions to be used as via points.
    - total_time (float): The total time for the trajectory.
    - tacc (float): Acceleration time for the trajectory.
    - qdmax (float): Maximum speed for the trajectory.
    """
    # Calculate dt based on total time and number of positions
    num_positions = len(recorded_positions)
    print(num_positions)
    dt = 0.25

    # Generate the trajectory
    times, positions, velocities, accelerations = generate_trajectory_with_mstraj(
        recorded_positions, dt, tacc, qdmax
    )
    dt = 0.01

    
    # Iterate over the positions and send them to the motor
    for pos in positions.flatten():
        print(f"Setting motor position to: {pos}") 
        position_list.append(pos)
        time.sleep(dt)
    print("   ")
    print("   ")
    print("   ")
    print(position_list)
    print("   ")
    print("   ")
    print("   ")

# Example usage
recorded_times, recorded_positions, _, _ = get_raw_position_over_time(10, 1)  # Example IDs
dt = 0.1  # Time step for the trajectory
total_time = 20  # Total time to complete the path in seconds

#for pos in recorded_positions:
#                print(pos)
#                time.sleep(0.12)

"""
A larger tacc results in a smoother, more gradual start and stop, with less jerk 
(time derivative of acceleration), which is often desirable to reduce mechanical stress.
"""
tacc = 1  # Acceleration time for the trajectory

"""
qdmax represents the maximum speed (also known as "velocity limit") that any axis can travel during the trajectory.
"""
qdmax = 2 # Optional: Maximum speed for the trajectory

# Generate the trajectory
times, positions, velocities, accelerations = generate_trajectory_with_mstraj(recorded_positions, dt, tacc, qdmax=qdmax)

# Send positions to motor
send_positions_to_motor(recorded_positions, total_time, tacc, qdmax=qdmax)

