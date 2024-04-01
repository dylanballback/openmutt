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


def calibrate():
    front_left_knee.set_absolute_position(0)
    front_left_shoulder.set_absolute_position(0)
    front_left_hip.set_absolute_position(0)

    front_right_knee.set_absolute_position(0)
    front_right_shoulder.set_absolute_position(0)
    front_right_hip.set_absolute_position(0)

    back_left_knee.set_absolute_position(0)
    back_left_shoulder.set_absolute_position(0)
    back_left_hip.set_absolute_position(0)

    back_right_knee.set_absolute_position(0)
    back_right_shoulder.set_absolute_position(0)
    back_right_hip.set_absolute_position(0)
    print("Calibration Complete: Absolute Position Set.")


def print_positions():
    print(f"Front Left Knee Position: {front_left_knee.position}")
    print(f"Front Left Shoulder Position: {front_left_shoulder.position}")
    print(f"Front Left Hip Position: {front_left_hip.position}")

    print(f"Front Right Knee Position: {front_right_knee.position}")
    print(f"Front Right Shoulder Position: {front_right_shoulder.position}")
    print(f"Front Right Hip Position: {front_right_hip.position}")

    print(f"Back Left Knee Position: {back_left_knee.position}")
    print(f"Back Left Shoulder Position: {back_left_shoulder.position}")
    print(f"Back Left Hip Position: {back_left_hip.position}")

    print(f"Back Right Knee Position: {back_right_knee.position}")
    print(f"Back Right Shoulder Position: {back_right_shoulder.position}")
    print(f"Back Right Hip Position: {back_right_hip.position}")
    for i in range(5):
        print("      ")


def clear_errors():
    front_left_knee.clear_errors(identify=False)
    front_left_shoulder.clear_errors(identify=False)
    front_left_hip.clear_errors(identify=False)

    front_right_knee.clear_errors(identify=False)
    front_right_shoulder.clear_errors(identify=False)
    front_right_hip.clear_errors(identify=False)

    back_left_knee.clear_errors(identify=False)
    back_left_shoulder.clear_errors(identify=False)
    back_left_hip.clear_errors(identify=False)

    back_right_knee.clear_errors(identify=False)
    back_right_shoulder.clear_errors(identify=False)
    back_right_hip.clear_errors(identify=False)


def set_closed_loop():
    front_left_knee.setAxisState("closed_loop_control")
    front_left_shoulder.setAxisState("closed_loop_control")
    front_left_hip.setAxisState("closed_loop_control")

    front_right_knee.setAxisState("closed_loop_control")
    front_right_shoulder.setAxisState("closed_loop_control")
    front_right_hip.setAxisState("closed_loop_control")

    back_left_knee.setAxisState("closed_loop_control")
    back_left_shoulder.setAxisState("closed_loop_control")
    back_left_hip.setAxisState("closed_loop_control")

    back_right_knee.setAxisState("closed_loop_control")
    back_right_shoulder.setAxisState("closed_loop_control")
    back_right_hip.setAxisState("closed_loop_control")


def set_idle():
    state = "idle"
    front_left_knee.setAxisState(state)
    front_left_shoulder.setAxisState(state)
    front_left_hip.setAxisState(state)

    front_right_knee.setAxisState(state)
    front_right_shoulder.setAxisState(state)
    front_right_hip.setAxisState(state)

    back_left_knee.setAxisState(state)
    back_left_shoulder.setAxisState(state)
    back_left_hip.setAxisState(state)

    back_right_knee.setAxisState(state)
    back_right_shoulder.setAxisState(state)
    back_right_hip.setAxisState(state)


#Example of how you can create a controller to get data from the O-Drives and then send motor comands based on that data.
async def controller():
        
        clear_errors()
        
        set_closed_loop()
        print_positions()
        await asyncio.sleep(2)
        calibrate()

        print("Standing")

        
        set_idle()
        #Run for set time delay example runs for 15 seconds.
        stop_at = datetime.now() + timedelta(seconds=1000)
        while datetime.now() < stop_at:
            print_positions()
            await asyncio.sleep(1) #Need this for async to work.
            pass
        
            #odrive1.set_position(0)
            #print("Set odrive to postion 0")
            #await asyncio.sleep(3)
            #odrive1.set_position(3)
            #print("Set odrive to postion 3")
            #await asyncio.sleep(3)
            


    



# Run multiple busses.
async def main():

    
    
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
        front_left_knee.estop()
        front_left_shoulder.estop()
        front_left_hip.estop()
        front_right_knee.estop()
        front_right_shoulder.estop()
        front_right_hip.estop()
        back_left_knee.estop()
        back_left_shoulder.estop()
        back_left_hip.estop()
        back_right_knee.estop()
        back_right_shoulder.estop()
        back_right_hip.estop()
    finally:
        front_left_knee.estop()
        front_left_shoulder.estop()
        front_left_hip.estop()
        front_right_knee.estop()
        front_right_shoulder.estop()
        front_right_hip.estop()
        back_left_knee.estop()
        back_left_shoulder.estop()
        back_left_hip.estop()
        back_right_knee.estop()
        back_right_shoulder.estop()
        back_right_hip.estop()
        front_left_knee.bus_shutdown()
        front_left_shoulder.bus_shutdown()
        front_left_hip.bus_shutdown()
        front_right_knee.bus_shutdown()
        front_right_shoulder.bus_shutdown()
        front_right_hip.bus_shutdown()
        back_left_knee.bus_shutdown()
        back_left_shoulder.bus_shutdown()
        back_left_hip.bus_shutdown()
        back_right_knee.bus_shutdown()
        back_right_shoulder.bus_shutdown()
        back_right_hip.bus_shutdown()


if __name__ == "__main__":
    asyncio.run(main())