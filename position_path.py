import pyodrivecan
import asyncio
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
from roboticstoolbox import mstraj

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
async def send_positions_to_motor(odrive1, positions):
    """
    Sends the position commands to the motor to repeat the path.
    Parameters:
    - recorded_positions (list): The recorded positions to be used as via points.
    - total_time (float): The total time for the trajectory.
    - tacc (float): Acceleration time for the trajectory.
    - qdmax (float): Maximum speed for the trajectory.
    """
    
    
    dt = 0.01
    # Iterate over the positions and send them to the motor
    for pos in positions.flatten():
        odrive1.set_position(pos)
        print(f"Setting motor position to: {pos}") 
        await asyncio.sleep(dt)



#Example of how you can create a controller to get data from the O-Drives and then send motor comands based on that data.
async def controller(odrive1, odrive2, odrive3):
        #odrive1.set_position(0)
        #print("Set odrive to postion 0")
        #odrive2.set_position(0)
        #odrive3.set_position(0)
        # Example usage
        #recorded_times, recorded_positions, _, _ = get_raw_position_over_time(10, 1)
        
        dt = 0.125


        #Run for set time delay example runs for 15 seconds.
        stop_at = datetime.now() + timedelta(seconds=15)
        while datetime.now() < stop_at:
            await asyncio.sleep(0) #Need this for async to work.
            #print(odrive1.position, odrive2.position)
            #for pos in recorded_positions:
                #odrive1.set_position(pos)
                #await asyncio.sleep(dt)
            #print("Set odrive to postion 0")
            #await asyncio.sleep(3)
            #odrive1.set_position(3)
            #print("Set odrive to postion 3")
            #await asyncio.sleep(3)
            
    
            

        #await asyncio.sleep(15) #no longer need this the timedelta =15 runs the program for 15 seconds.
        odrive1.running = False
        odrive2.running = False
        odrive3.running = False



# Run multiple busses.
async def main():
    #Set up Node_ID 1
    odrive1 = pyodrivecan.ODriveCAN(1, closed_loop_control_flag = True)
    odrive1.initCanBus()

    #Set up Node_ID 2 
    odrive2 = pyodrivecan.ODriveCAN(2, closed_loop_control_flag = False)
    odrive2.initCanBus()

    #Set up Node_ID 3 
    odrive3 = pyodrivecan.ODriveCAN(3, closed_loop_control_flag = False)
    odrive3.initCanBus()

    # Example usage
    recorded_times, recorded_positions, _, _ = get_raw_position_over_time(10, 1)
    total_time = 10  # Total time to complete the path in seconds
    tacc = 0.5  # Acceleration time for the trajectory
    qdmax = 0.5  # Maximum speed for the trajectory
    dt = 0.25
    # Generate the trajectory
    times, positions, velocities, accelerations = generate_trajectory_with_mstraj(
        recorded_positions, dt, tacc, qdmax
    )
    

    #add each odrive to the async loop so they will run.
    await asyncio.gather(
        odrive1.loop(),
        odrive2.loop(),
        odrive3.loop(),
        controller(odrive1, odrive2, odrive3),
        send_positions_to_motor(odrive1, positions)
    )

if __name__ == "__main__":
    asyncio.run(main())