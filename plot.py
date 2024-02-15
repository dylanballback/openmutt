import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pyodrivecan
import numpy as np
from scipy.interpolate import CubicSpline


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


def plot_raw_position_over_time(times, positions, trial_id, node_id):
    # Plotting the position data
    plt.figure(figsize=(10, 6))
    plt.plot(times, positions, marker='o', linestyle='-', color='b')
    plt.title(f'Position Over Time for Trial ID {trial_id} and Node ID {node_id}')
    plt.xlabel('Time (s)')
    plt.ylabel('Position')
    plt.grid(True)
    plt.show()

    



def generate_smooth_path(times, positions, num_points=1000):
    """
    Generates a smooth path using cubic spline interpolation over given position data.

    Parameters:
    - times (list): A list of times at which the positions were recorded.
    - positions (list): A list of recorded positions.
    - num_points (int): The number of points to generate for the smooth path.

    Returns:
    - tuple: (new_times, smooth_positions) where 'new_times' is a list of evenly spaced time points
             and 'smooth_positions' is a list of interpolated positions corresponding to 'new_times'.
    """
    # Create a cubic spline interpolation of the provided points
    cs = CubicSpline(times, positions)

    # Generate a new set of evenly spaced time points
    new_times = np.linspace(min(times), max(times), num_points)

    # Evaluate the spline at the new time points to get the smooth positions
    smooth_positions = cs(new_times)

    # Optionally, plot the original and interpolated points for verification
    plt.figure(figsize=(10, 6))
    plt.plot(times, positions, 'o', label='Original data')
    plt.plot(new_times, smooth_positions, '-', label='Smooth path')
    plt.legend()
    plt.show()

    return new_times, smooth_positions



def calculate_velocity_commands(smooth_positions, smooth_times, total_time):
    """
    Calculates velocity commands needed to follow a smooth path within a specified total time.

    Parameters:
    - smooth_positions (list): Interpolated positions from the smooth path.
    - smooth_times (list): Times corresponding to the smooth positions.
    - total_time (float): The desired total time to complete the path.

    Returns:
    - tuple: (scaled_times, adjusted_velocities) where 'scaled_times' is the list of time points
             adjusted to fit the total_time, and 'adjusted_velocities' are the corresponding
             velocity commands to follow the smooth path.
    """
    # Scale the time to fit the new total_time
    time_scaling_factor = (smooth_times[-1] - smooth_times[0]) / total_time
    scaled_times = smooth_times / time_scaling_factor

    # Create a spline based on the original smooth path
    position_spline = CubicSpline(smooth_times, smooth_positions)

    # Create a new spline for velocity based on scaled times
    velocity_spline = position_spline.derivative()

    # Calculate the new velocity commands based on scaled times
    velocity_commands = velocity_spline(scaled_times)

    # Adjust the velocities by the time scaling factor
    adjusted_velocities = velocity_commands * time_scaling_factor

    return scaled_times, adjusted_velocities



def plot_all(raw_times, raw_positions, new_times, smooth_positions, total_time):
    """
    Plots all related graphs: raw positions vs. time, smooth path, velocity commands, and acceleration.

    Parameters:
    - raw_times (list): Times at which the raw positions were recorded.
    - raw_positions (list): Recorded raw positions.
    - new_times (list): Time points for the smooth path and velocity/acceleration calculations.
    - smooth_positions (list): Interpolated positions for the smooth path.
    - total_time (float): The desired total time to complete the path, used for velocity calculations.
    """
    # Calculate velocity and acceleration commands
    scaled_times, velocity_commands = calculate_velocity_commands(smooth_positions, new_times, total_time)
    position_spline = CubicSpline(new_times, smooth_positions)
    velocity_spline = position_spline.derivative()
    acceleration_commands = velocity_spline.derivative()(scaled_times) * ((new_times[-1] - new_times[0]) / total_time) ** 2

    # Set up the plot grid
    fig = plt.figure(figsize=(12, 10))
    gs = gridspec.GridSpec(2, 2, figure=fig)

    # Plot configurations for each subplot
    ax0 = fig.add_subplot(gs[0, 0])  # Raw positions vs. time
    ax1 = fig.add_subplot(gs[1, 0])  # Smooth path
    ax2 = fig.add_subplot(gs[0, 1])  # Velocity commands vs. new times
    ax3 = fig.add_subplot(gs[1, 1])  # Acceleration commands vs. new times

    # Raw positions vs. time
    ax0.plot(raw_times, raw_positions, 'o-', label='Raw Positions')
    ax0.set_title('Raw Positions vs. Time')
    ax0.set_xlabel('Time (s)')
    ax0.set_ylabel('Position')
    ax0.grid(True)
    ax0.legend()

    # Smooth path
    ax1.plot(new_times, smooth_positions, '-', label='Smooth Path')
    ax1.set_title('Smooth Path')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Position')
    ax1.grid(True)
    ax1.legend()

    # Velocity commands vs. new times
    ax2.plot(scaled_times, velocity_commands, '-', label='Velocity Commands')
    ax2.set_title('Velocity Commands vs. New Times')
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Velocity')
    ax2.grid(True)
    ax2.legend()

    # Acceleration commands vs. new times
    ax3.plot(scaled_times, acceleration_commands, '-', label='Acceleration Commands')
    ax3.set_title('Acceleration Commands vs. New Times')
    ax3.set_xlabel('Time (s)')
    ax3.set_ylabel('Acceleration')
    ax3.grid(True)
    ax3.legend()

    plt.tight_layout()
    plt.show()




def main():
    
   # Get the position and time data for the specific trial_id and node_id
    recorded_times, recorded_positions, trial_id, node_id = get_raw_position_over_time(10, 1)

    # Check if data was found
    if recorded_times is None or recorded_positions is None:
        print("No data found. Exiting.")
        return

    # Convert times and positions to numpy arrays for further processing
    recorded_times = np.array(recorded_times, dtype=np.float64)
    recorded_positions = np.array(recorded_positions, dtype=np.float64)

    # Generate the smooth path from the recorded data
    smooth_times, smooth_positions = generate_smooth_path(recorded_times, recorded_positions, num_points=1000)

    # Calculate velocity commands to complete the path in the desired total time
    desired_total_time = 10  # For example, complete the path in 10 seconds
    new_times, velocity_commands = calculate_velocity_commands(smooth_positions, smooth_times, desired_total_time)

    # Plot raw positions, smooth path, velocity, and acceleration in a comprehensive plot
    plot_all(recorded_times, recorded_positions, new_times, smooth_positions, desired_total_time)


if __name__ == "__main__":
    main()