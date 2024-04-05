import pyodrivecan
import asyncio
from datetime import datetime, timedelta
import time

#This standing the dog wanted to lean and fall backwards 
stand_back = [[0.475, 1.275, 2.500]]
stand_front =[[7.486, 5.775, 2.500]]

# Moving Back Knee to more under dog not so far behind it.
# Dog still wants to lean too far back and fall.
stand_back_v3 = [[1.579, 2.256, 2.500]]
stand_front_v3 =[[6.420, 4.909, 2.500]]

# Moving legs to both go inwards to center of dog.
# Dog Stands on old lab floor
stand_back_v4 = [[7.281, 5.215, 2.400]]
stand_front_v4 =[[7.171, 5.262, 2.400]]


square_gait_v1 = [[1.231, 1.706, 2.500], [0.257, 1.193, 2.500], [0.102, 1.730, 2.500], [1.017, 2.235, 2.500]]

front_square_gait_v1 = [[7.129, 5.946, 2.500], [7.822, 5.946, 2.500], [7.915, 5.628, 2.500], [7.111, 5.207, 2.500]]

#Node ID for each leg (goes from hip, shoulder, knee)
front_left = [2, 1, 0]
front_right = [3, 4, 5]

back_left = [8, 7, 6]
back_right = [9, 10, 11]


front_left_knee = pyodrivecan.ODriveCAN(0, canBitRate=1000000)
front_left_knee.initCanBus()

front_left_shoulder = pyodrivecan.ODriveCAN(1, canBitRate=1000000)
front_left_shoulder.initCanBus()
    
front_left_hip = pyodrivecan.ODriveCAN(2, canBitRate=1000000)
front_left_hip.initCanBus()
    

#Front Right 
front_right_knee = pyodrivecan.ODriveCAN(5, canBitRate=1000000)
front_right_knee.initCanBus()
    
front_right_shoulder = pyodrivecan.ODriveCAN(4, canBitRate=1000000)
front_right_shoulder.initCanBus()

front_right_hip = pyodrivecan.ODriveCAN(3, canBitRate=1000000)
front_right_hip.initCanBus()


#Back of Dog

#Back Left 
back_left_knee = pyodrivecan.ODriveCAN(6, canBusID="can1", canBitRate=1000000)
back_left_knee.initCanBus()
    
back_left_shoulder = pyodrivecan.ODriveCAN(7, canBusID="can1", canBitRate=1000000)
back_left_shoulder.initCanBus()
    
back_left_hip = pyodrivecan.ODriveCAN(8, canBusID="can1", canBitRate=1000000)
back_left_hip.initCanBus()
    
#Back Right 
back_right_knee = pyodrivecan.ODriveCAN(11, canBusID="can1", canBitRate=1000000)
back_right_knee.initCanBus() 
    
back_right_shoulder = pyodrivecan.ODriveCAN(10, canBusID="can1", canBitRate=1000000)
back_right_shoulder.initCanBus()

back_right_hip = pyodrivecan.ODriveCAN(9, canBusID="can1", canBitRate=1000000)
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

kneesandshoulder = [
    front_left_knee,
    front_left_shoulder,
    front_right_knee,
    front_right_shoulder,
    back_left_knee,
    back_left_shoulder,
    back_right_knee,
    back_right_shoulder
]


front_kneesandshoulder = [
    front_left_knee,
    front_left_shoulder,
    front_right_knee,
    front_right_shoulder
]

back_kneesandshoulder = [
    back_left_knee,
    back_left_shoulder,
    back_right_knee,
    back_right_shoulder
]

front_right = [
    front_right_knee,
    front_right_shoulder,
    front_right_hip,
]

front_left = [
    front_left_knee,
    front_left_shoulder,
    front_left_hip,
]

back_right = [
    back_right_knee,
    back_right_shoulder,
    back_right_hip
]

back_left = [
    back_left_knee,
    back_left_shoulder,
    back_left_hip,
]

def set_leg_pos(leg, stand):
    leg_name = ''
    # Determine which leg we are controlling based on the motors list
    if leg == front_right:
        leg_name = 'front_right'
    elif leg == front_left:
        leg_name = 'front_left'
    elif leg == back_right:
        leg_name = 'back_right'
    elif leg == back_left:
        leg_name = 'back_left'

    # Define the multipliers for knee, shoulder, and hip for each leg
    multipliers = {
        'front_right': (-1, -1, 1),
        'front_left': (1, 1, -1),
        'back_right': (1, 1, -1),
        'back_left': (-1, -1, 1),
    }

    # Get the multipliers for the current leg
    knee_mult, shoulder_mult, hip_mult = multipliers.get(leg_name, (1, 1, 1))


    for position in stand:
        # Apply offsets to the knee and shoulder positions for front legs
        knee_position = (position[0] ) * knee_mult
        shoulder_position = (position[1] ) * shoulder_mult
        hip_position = position[2] * hip_mult

        # Set positions for each motor
        leg[0].set_position(knee_position)       # Knee
        leg[1].set_position(shoulder_position)   # Shoulder
        leg[2].set_position(hip_position)        # Hip

def stand():
    set_leg_pos(front_left, stand_front_v4)
    set_leg_pos(front_right, stand_front_v4)
    set_leg_pos(back_left, stand_back_v4)
    set_leg_pos(back_right, stand_back_v4)

async def idle_lower():
    # Set Front and Back Knee and Shoulder Motors to Idle State
    for knee in kneesandshoulder:
        knee.setAxisState("idle")
        await asyncio.sleep(0.2)


async def front_idle_lower():
    # Set Front Knee and Shoulder Motors to Idle State
    for knee in front_kneesandshoulder:
        knee.setAxisState("idle")
        await asyncio.sleep(0.2)

async def back_idle_lower():
    # Set Back Knee and Shoulder Motors to Idle State
    for knee in back_kneesandshoulder:
        knee.setAxisState("idle")
        await asyncio.sleep(0.2)

async def closedloop_lower():
    # Set Front Knee and Shoulder Motors to Closed Loop 
    for knee in kneesandshoulder:
        knee.setAxisState("closed_loop_control")
        await asyncio.sleep(0.2)

current_limit = 35.0
velocity_limit = 30.0

def set_limits():
    for odrive in odrives:
        odrive.set_limits(velocity_limit=velocity_limit, current_limit=current_limit)


def print_positions():

    # Helper function to format the position
    def format_position(pos):
        return f"{pos:.3f}" if pos is not None else "Unknown"
    
    print(f"\rFront Left: {format_position(front_left_knee.position)}, {format_position(front_left_shoulder.position)}, {format_position(front_left_hip.position)}   Front Right: {format_position(front_right_knee.position)}, {format_position(front_right_shoulder.position)}, {format_position(front_right_hip.position)}   "
              f"Back Left: {format_position(back_left_knee.position)}, {format_position(back_left_shoulder.position)}, {format_position(back_left_hip.position)}   Back Right: {format_position(back_right_knee.position)}, {format_position(back_right_shoulder.position)}, {format_position(back_right_hip.position)}", end='', flush=True)


async def clear_buffer():
    front_left_knee.flush_can_buffer()
    await asyncio.sleep(0.2)
    back_left_knee.flush_can_buffer()
        

async def clear_errors():
    for odrive in odrives:
        odrive.clear_errors(identify=False)
        await asyncio.sleep(0.2)


async def set_closed_loop():
    for odrive in odrives:
        odrive.setAxisState("closed_loop_control")
        await asyncio.sleep(0.2)

async def set_idle():
    for odrive in odrives:
        odrive.setAxisState("idle")
        await asyncio.sleep(0.2)
        
    print("Idle")

async def set_all_filtered_pos_control():
    #await clear_buffer()
    #await asyncio.sleep(0.5)
    for odrive in odrives:
        # Set each ODrive to filtered position control
        odrive.set_controller_mode(control_mode_name="position_control", input_mode_name="pos_filter")
        await asyncio.sleep(0.2)  # Delay to prevent command overlap on CAN bus
        print(f"Set ODrive {odrive.nodeID} to filtered position control.")


def estop_all():
    for odrive in odrives:
        odrive.estop()

def bus_shutdown_all():
    for odrive in odrives:
        odrive.bus_shutdown()
        time.sleep(0.1)
        

async def save_config():
    for odrive in odrives:
        odrive.reboot_save(action="save")
        await asyncio.sleep(0.2)


async def calibrate():
    for odrive in odrives:
        odrive.set_absolute_position(0)
        await asyncio.sleep(0.2)

    #await set_idle()
    #await save_config()

    print("Calibration Complete: Absolute Position Set.")


async def print_positions_continuously(duration, interval=0.5):
    stop_at = datetime.now() + timedelta(seconds=duration)
    while datetime.now() < stop_at:
        print_positions()
        await asyncio.sleep(interval)



# Function to move a joint smoothly between a min and max position
async def move_joint_smoothly(odrive, min_pos, max_pos, sleep_time=2):
    while True:
        odrive.set_position(min_pos)
        await asyncio.sleep(sleep_time)
        odrive.set_position(max_pos)
        await asyncio.sleep(sleep_time)


async def leg_square_gait(leg, gait, delay=3):
    leg_name = ''
    # Determine which leg we are controlling based on the motors list
    if leg == front_right:
        leg_name = 'front_right'
    elif leg == front_left:
        leg_name = 'front_left'
    elif leg == back_right:
        leg_name = 'back_right'
    elif leg == back_left:
        leg_name = 'back_left'

    # Define the multipliers for knee, shoulder, and hip for each leg
    multipliers = {
        'front_right': (-1, -1, 1),
        'front_left': (1, 1, -1),
        'back_right': (1, 1, -1),
        'back_left': (-1, -1, 1),
    }

    # Define offsets for the front legs
    offsets = {
        'front_right': (0, 0),
        'front_left': (0, 0),
        #'front_right': (5.8, 4.2),
        #'front_left': (5.8, 4.2),
    }

    # Get the multipliers for the current leg
    knee_mult, shoulder_mult, hip_mult = multipliers.get(leg_name, (1, 1, 1))

    # Get the offsets for the front legs, default to (0, 0) if back leg
    knee_offset, shoulder_offset = offsets.get(leg_name, (0, 0))

    while True:
        for position in gait:
            # Apply offsets to the knee and shoulder positions for front legs
            knee_position = (position[0] + knee_offset) * knee_mult
            shoulder_position = (position[1] + shoulder_offset) * shoulder_mult
            hip_position = position[2] * hip_mult

            # Set positions for each motor
            leg[0].set_position(knee_position)       # Knee
            leg[1].set_position(shoulder_position)   # Shoulder
            leg[2].set_position(hip_position)        # Hip

            await asyncio.sleep(delay)  # Delay between each movement

#await leg_square_gait(back_left, square_gait_v1)

#Example of how you can create a controller to get data from the O-Drives and then send motor comands based on that data.
async def controller():
        await clear_buffer()
        await asyncio.sleep(0.2)
        await clear_errors()
        await asyncio.sleep(0.2)
        #clear_buffer()
        #await asyncio.sleep(0.5)
        #await set_closed_loop()
        #await asyncio.sleep(0.2)
        
        # You must calibrate when the O-Drives are first powered up.
        await calibrate()
        await asyncio.sleep(10)
        
        
        #await set_all_filtered_pos_control()
        #await closedloop_lower()
        await asyncio.sleep(2)
        
        
        """
        hip_position = 2.4
        front_right_hip.set_position(hip_position)
        front_left_hip.set_position(-hip_position)
        back_right_hip.set_position(-hip_position)
        back_left_hip.set_position(hip_position)
        await asyncio.sleep(2)
        
        
        # Square Gait all four Legs
        tasks = [
            leg_square_gait(front_left, front_square_gait_v1),
            leg_square_gait(front_right, front_square_gait_v1),
            leg_square_gait(back_left, square_gait_v1),
            leg_square_gait(back_right, square_gait_v1),
            print_positions_continuously(1000)
        ]

        await asyncio.gather(*tasks)
        """


        # Testing just one (back left) leg with square gait
        #await asyncio.gather(leg_square_gait(back_left, square_gait_v1), print_positions_continuously(1000))
        """
        
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
            print_positions_continuously(1000)
            # Add tasks for other joints as necessary
        ]
        
        
        await asyncio.gather(*tasks)
        """

        #await idle_lower()

        #stand()

        # This is for setting a set of legs to idle and printing positions.
        #await asyncio.gather(front_idle_lower(), back_idle_lower(), print_positions_continuously(1000))

        #await front_idle_lower()
        await set_idle()
        await print_positions_continuously(1000)
        
        """
        

        await clear_buffer()
        await asyncio.sleep(0.5)

        await set_idle()

        
        await set_closed_loop()
        await asyncio.sleep(2)

        await set_closed_loop()
        await asyncio.sleep(2)
        """

        
            #pass
        
            #odrive1.set_position(0)
            #print("Set odrive to postion 0")
            #await asyncio.sleep(3)
            #odrive1.set_position(3)
            #print("Set odrive to postion 3")
            #await asyncio.sleep(3)
            


    



# Run multiple busses.
async def main():
    await clear_buffer()
    await asyncio.sleep(1)
    await clear_errors()

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