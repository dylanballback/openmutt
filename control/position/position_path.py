import pyodrivecan
import asyncio
from datetime import datetime, timedelta

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




#Example of how you can create a controller to get data from the O-Drives and then send motor comands based on that data.
async def controller(odrive1, odrive2, odrive3):
        #odrive1.set_position(0)
        #print("Set odrive to postion 0")
        #odrive2.set_position(0)
        #odrive3.set_position(0)
        # Example usage
        recorded_times, recorded_positions, _, _ = get_raw_position_over_time(10, 1)
        
        dt = 0.125


        #Run for set time delay example runs for 15 seconds.
        stop_at = datetime.now() + timedelta(seconds=15)
        while datetime.now() < stop_at:
            await asyncio.sleep(0) #Need this for async to work.
            #print(odrive1.position, odrive2.position)
            for pos in recorded_positions:
                odrive1.set_position(pos)
                await asyncio.sleep(dt)
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
    odrive1 = pyodrivecan.ODriveCAN(1, closed_loop_control_flag = False)
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

    

    #add each odrive to the async loop so they will run.
    await asyncio.gather(
        odrive1.loop(),
        odrive2.loop(),
        odrive3.loop(),
        controller(odrive1, odrive2, odrive3),
    )

if __name__ == "__main__":
    asyncio.run(main())