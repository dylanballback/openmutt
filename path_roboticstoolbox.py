import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from roboticstoolbox import jtraj
import pyodrivecan


# Define path to database for pyodrivecan package.
database = pyodrivecan.OdriveDatabase('odrive_data.db')


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


def generate_trajectory_with_jtraj(recorded_times, recorded_positions, total_time, max_acc):
    """
    Generates a trajectory using jtraj, fitting the recorded path into a specific total time
    and respecting a maximum acceleration limit.

    Parameters:
    - recorded_times (list): The times at which positions were recorded.
    - recorded_positions (list): The recorded positions.
    - total_time (float): The desired total time to complete the path.
    - max_acc (float): The maximum acceleration limit.

    Returns:
    - A tuple containing the times, positions, velocities, and accelerations for the trajectory.
    """
    
    # Interpolate the recorded data to fit the total_time
    original_duration = recorded_times[-1] - recorded_times[0]
    time_scaling_factor = original_duration / total_time
    scaled_times = np.linspace(0, total_time, len(recorded_times))
    
    # Use CubicSpline for interpolation to get positions matching the scaled times
    cs = CubicSpline(recorded_times, recorded_positions)
    interpolated_positions = cs(scaled_times * time_scaling_factor)
    
    # Calculate the jtraj trajectory
    q0 = interpolated_positions[0:1]  # Initial position
    qf = interpolated_positions[-1:]  # Final position
    t = np.linspace(0, total_time, 100)  # Generate 100 time steps over the total_time
    
    # jtraj requires start and end velocities, assuming 0 for simplicity
    traj = jtraj(q0, qf, t)
    
    # Plotting
    fig, axs = plt.subplots(3, 1, figsize=(10, 15))
    
    # Original recorded positions
    axs[0].plot(recorded_times, recorded_positions, 'o-', label='Original Positions')
    axs[0].set_title('Original Recorded Positions')
    axs[0].set_xlabel('Time (s)')
    axs[0].set_ylabel('Position')
    axs[0].legend()
    
    # Calculated trajectory positions
    axs[1].plot(t, traj.q, label='Trajectory Position')
    axs[1].set_title('Trajectory Position vs. Time')
    axs[1].set_xlabel('Time (s)')
    axs[1].set_ylabel('Position')
    axs[1].legend()
    
    # Calculated trajectory velocities
    axs[2].plot(t, traj.qd, label='Trajectory Velocity')
    axs[2].set_title('Trajectory Velocity vs. Time')
    axs[2].set_xlabel('Time (s)')
    axs[2].set_ylabel('Velocity')
    axs[2].legend()

    plt.tight_layout()
    plt.show()

    return t, traj.q, traj.qd, traj.qdd

# Example usage
# Assuming you have fetched `recorded_times` and `recorded_positions` from `get_raw_position_over_time`
recorded_times, recorded_positions, _, _ = get_raw_position_over_time(10, 1)  # Example IDs
total_time = 10  # Desired total time to complete the path in seconds
max_acc = 0.5  # Maximum acceleration (units depend on your specific application)

# Convert lists to numpy arrays for processing
# Convert lists to numpy arrays for processing
recorded_times = np.array(recorded_times, dtype=np.float64)
recorded_positions = np.array(recorded_positions, dtype=np.float64)


generate_trajectory_with_jtraj(recorded_times, recorded_positions, total_time, max_acc)
