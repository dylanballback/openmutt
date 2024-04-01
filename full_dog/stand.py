import pyodrivecan
import asyncio
from datetime import datetime, timedelta
import time

#Node ID for each leg (goes from hip, shoulder, knee)
front_left = [2, 1, 0]
front_right = [3, 4, 5]

back_left = [8, 7, 6]
back_right = [9, 10, 11]


front_left_knee = pyodrivecan.ODriveCAN(0)
front_left_knee.initCanBus()

front_left_shoulder = pyodrivecan.ODriveCAN(1)
front_left_shoulder.initCanBus()
    
front_left_hip = pyodrivecan.ODriveCAN(2)
front_left_hip.initCanBus()
    

#Front Right 
front_right_knee = pyodrivecan.ODriveCAN(5)
front_right_knee.initCanBus()
    
front_right_shoulder = pyodrivecan.ODriveCAN(4)
front_right_shoulder.initCanBus()

front_right_hip = pyodrivecan.ODriveCAN(3)
front_right_hip.initCanBus()


#Back of Dog

#Back Left 
back_left_knee = pyodrivecan.ODriveCAN(6, canBusID="can1")
back_left_knee.initCanBus()
    
back_left_shoulder = pyodrivecan.ODriveCAN(7, canBusID="can1")
back_left_shoulder.initCanBus()
    
back_left_hip = pyodrivecan.ODriveCAN(8, canBusID="can1")
back_left_hip.initCanBus()
    
#Back Right 
back_right_knee = pyodrivecan.ODriveCAN(11, canBusID="can1")
back_right_knee.initCanBus() 
    
back_right_shoulder = pyodrivecan.ODriveCAN(10, canBusID="can1")
back_right_shoulder.initCanBus()

back_right_hip = pyodrivecan.ODriveCAN(9, canBusID="can1")
back_right_hip.initCanBus()

# List of all your ODriveCAN instances
odrives = [
    front_left_knee,
    front_left_shoulder,
    front_left_hip,
    front_right_knee,
    front_right_shoulder,
    front_right_hip,
    back_left_knee,
    back_left_shoulder,
    back_left_hip,
    back_right_knee,
    back_right_shoulder,
    back_right_hip
]

current_limit = 35.0
velocity_limit = 10.0

def set_limits():
    for odrive in odrives:
        odrive.set_limits(velocity_limit=velocity_limit, current_limit=current_limit)

def calibrate():
    for odrive in odrives:
        odrive.set_absolute_position(0)

    print("Calibration Complete: Absolute Position Set.")


def print_positions():
    # Helper function to format the position
    def format_position(pos):
        return f"{pos:.3f}" if pos is not None else "Unknown"

    print(f"Front Left Knee Position: {format_position(front_left_knee.position)}")
    print(f"Front Left Shoulder Position: {format_position(front_left_shoulder.position)}")
    print(f"Front Left Hip Position: {format_position(front_left_hip.position)}")
    print("      ")
    print(f"Front Right Knee Position: {format_position(front_right_knee.position)}")
    print(f"Front Right Shoulder Position: {format_position(front_right_shoulder.position)}")
    print(f"Front Right Hip Position: {format_position(front_right_hip.position)}")
    print("      ")
    print(f"Back Left Knee Position: {format_position(back_left_knee.position)}")
    print(f"Back Left Shoulder Position: {format_position(back_left_shoulder.position)}")
    print(f"Back Left Hip Position: {format_position(back_left_hip.position)}")
    print("      ")
    print(f"Back Right Knee Position: {format_position(back_right_knee.position)}")
    print(f"Back Right Shoulder Position: {format_position(back_right_shoulder.position)}")
    print(f"Back Right Hip Position: {format_position(back_right_hip.position)}")
    for i in range(5):
        print("      ")

def clear_buffer():
    for odrive in odrives:
        odrive.flush_can_buffer()
        time.sleep(0.2)

def clear_errors():
    for odrive in odrives:
        odrive.clear_errors(identify=False)
        time.sleep(0.2)


def set_closed_loop():
    for odrive in odrives:
        odrive.setAxisState("closed_loop_control")
        time.sleep(0.2)

def set_idle():
    for odrive in odrives:
        odrive.setAxisState("idle")
        time.sleep(0.2)
        
    print("Idle")

def set_all_filtered_pos_control():
    clear_buffer()
    time.sleep(0.1)
    for odrive in odrives:
        # Set each ODrive to filtered position control
        odrive.set_controller_mode(control_mode_name="position_control", input_mode_name="pos_filter")
        time.sleep(0.1)  # Delay to prevent command overlap on CAN bus
        print(f"Set ODrive {odrive.nodeID} to filtered position control.")


def estop_all():
    for odrive in odrives:
        odrive.estop()

def bus_shutdown_all():
    for odrive in odrives:
        odrive.bus_shutdown()


# Function to move a joint smoothly between a min and max position
async def move_joint_smoothly(odrive, min_pos, max_pos, sleep_time=2):
    while True:
        odrive.set_position(min_pos)
        await asyncio.sleep(sleep_time)
        odrive.set_position(max_pos)
        await asyncio.sleep(sleep_time)


#Example of how you can create a controller to get data from the O-Drives and then send motor comands based on that data.
async def controller():
        clear_buffer()
        await asyncio.sleep(0.5)
        clear_errors()
        await asyncio.sleep(0.5)
        clear_buffer()
        await asyncio.sleep(0.5)
        set_closed_loop()
        await asyncio.sleep(0.5)
        print_positions()
        await asyncio.sleep(0.5)
        calibrate()

        """
        await asyncio.sleep(2)
        set_all_filtered_pos_control()

        await asyncio.sleep(5)
        clear_buffer()
        await asyncio.sleep(5)
        clear_buffer()
        await asyncio.sleep(5)
        clear_buffer()
        await asyncio.sleep(5)
        clear_buffer()
        await asyncio.sleep(5)
        clear_buffer()
        await asyncio.sleep(2)
        

        hip_position = 2
        front_right_hip.set_position(hip_position)
        front_left_hip.set_position(hip_position)
        back_right_hip.set_position(hip_position)
        back_left_hip.set_position(hip_position)
        
        await asyncio.sleep(5)
        clear_buffer()
        await asyncio.sleep(5)
        clear_buffer()
        await asyncio.sleep(5)
        clear_buffer()
        await asyncio.sleep(5)
        clear_buffer()
        await asyncio.sleep(5)
        clear_buffer()
        await asyncio.sleep(2)

        print("Moving")
        


        

        # Create tasks for each joint to move smoothly between its ranges
        tasks = [
            move_joint_smoothly(front_left_knee, 0.1, 7.9),
            move_joint_smoothly(front_left_shoulder, 0.1, 6.6),
            move_joint_smoothly(front_right_knee, 0.1, -7.9),
            move_joint_smoothly(front_right_shoulder, 0.1, -6.6),
            move_joint_smoothly(back_left_knee, 0.1, -7.9),
            move_joint_smoothly(back_left_shoulder, 0.1, -6.6),
            move_joint_smoothly(back_right_knee, 0.1, 7.9),
            move_joint_smoothly(back_right_shoulder, 0.1, 6.6),
            # Add tasks for other joints as necessary
        ]

        #await asyncio.gather(*tasks)
        """

        set_idle()
        #Run for set time delay example runs for 15 seconds.
        stop_at = datetime.now() + timedelta(seconds=1000)
        while datetime.now() < stop_at:
            
            print_positions()
            await asyncio.sleep(1) #Need this for async to work.
            #pass
        
            #odrive1.set_position(0)
            #print("Set odrive to postion 0")
            #await asyncio.sleep(3)
            #odrive1.set_position(3)
            #print("Set odrive to postion 3")
            #await asyncio.sleep(3)
            


    



# Run multiple busses.
async def main():
    clear_buffer()
    time.sleep(1)
    clear_errors()

    clear_buffer()
    time.sleep(1)
    set_limits()
    
    try:
        await asyncio.gather(
            front_left_knee.loop(),
            front_left_shoulder.loop(),
            front_left_hip.loop(),
            front_right_knee.loop(),
            front_right_shoulder.loop(),
            front_right_hip.loop(),
            back_left_knee.loop(),
            back_left_shoulder.loop(),
            back_left_hip.loop(),
            back_right_knee.loop(),
            back_right_shoulder.loop(),
            back_right_hip.loop(),
            controller() 
        )
    except KeyboardInterrupt:
        estop_all()
    finally:
        estop_all()
        bus_shutdown_all()


if __name__ == "__main__":
    asyncio.run(main())