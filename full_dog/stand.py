import pyodrivecan
import asyncio
from datetime import datetime, timedelta
import time

#Node ID for each leg (goes from hip, shoulder, knee)
front_left = [2, 1, 0]
front_right = [3, 4, 5]

back_left = [8, 7, 6]
back_right = [9, 10, 11]



#Example of how you can create a controller to get data from the O-Drives and then send motor comands based on that data.
async def controller(front_left_knee, front_left_shoulder, front_left_hip,
                    front_right_knee, front_right_shoulder, front_right_hip,
                    back_left_knee, back_left_shoulder, back_left_hip,
                    back_right_knee, back_right_shoulder, back_right_hip):
        
        sleep_time = 10
        
        front_left_knee.clear_errors(identify=True)
        await asyncio.sleep(sleep_time)
        front_left_shoulder.clear_errors(identify=True)
        await asyncio.sleep(sleep_time)
        front_left_hip.clear_errors(identify=True)
        await asyncio.sleep(sleep_time)

        front_right_knee.clear_errors(identify=True)
        await asyncio.sleep(sleep_time)
        front_right_shoulder.clear_errors(identify=True)
        await asyncio.sleep(sleep_time)
        front_right_hip.clear_errors(identify=True)
        await asyncio.sleep(sleep_time)

        back_left_knee.clear_errors(identify=True)
        await asyncio.sleep(sleep_time)
        back_left_shoulder.clear_errors(identify=True)
        await asyncio.sleep(sleep_time)
        back_left_hip.clear_errors(identify=True)
        await asyncio.sleep(sleep_time)

        back_right_knee.clear_errors(identify=True)
        await asyncio.sleep(sleep_time)
        back_right_shoulder.clear_errors(identify=True)
        await asyncio.sleep(sleep_time)
        back_right_hip.clear_errors(identify=True)
        await asyncio.sleep(sleep_time)
        """
        front_left_knee.setAxisState("closed_loop_control")
        await asyncio.sleep(0.2)
        front_left_shoulder.setAxisState("closed_loop_control")
        await asyncio.sleep(0.2)
        front_left_hip.setAxisState("closed_loop_control")
        await asyncio.sleep(0.2)
        front_right_knee.setAxisState("closed_loop_control")
        await asyncio.sleep(0.2)
        front_right_shoulder.setAxisState("closed_loop_control")
        await asyncio.sleep(0.2)
        front_right_hip.setAxisState("closed_loop_control")
        await asyncio.sleep(0.2)
        back_left_knee.setAxisState("closed_loop_control")
        await asyncio.sleep(0.2)
        back_left_shoulder.setAxisState("closed_loop_control")
        await asyncio.sleep(0.2)
        back_left_hip.setAxisState("closed_loop_control")
        await asyncio.sleep(0.2)
        back_right_knee.setAxisState("closed_loop_control")
        await asyncio.sleep(0.2)
        back_right_shoulder.setAxisState("closed_loop_control")
        await asyncio.sleep(0.2)
        back_right_hip.setAxisState("closed_loop_control")
        await asyncio.sleep(0.2)
        """

        #Run for set time delay example runs for 15 seconds.
        stop_at = datetime.now() + timedelta(seconds=15)
        while datetime.now() < stop_at:
            await asyncio.sleep(0) #Need this for async to work.
            print("Standing")
            #odrive1.set_position(0)
            #print("Set odrive to postion 0")
            #await asyncio.sleep(3)
            #odrive1.set_position(3)
            #print("Set odrive to postion 3")
            #await asyncio.sleep(3)
            



# Run multiple busses.
async def main():
    sleep_time = 5
    #Front of Dog
         
    front_left_knee = pyodrivecan.ODriveCAN(0)
    front_left_knee.initCanBus()
    time.sleep(sleep_time)
    #front_left_knee.clear_errors(identify=False)

    front_left_shoulder = pyodrivecan.ODriveCAN(1)
    front_left_shoulder.initCanBus()
    time.sleep(sleep_time)

    front_left_hip = pyodrivecan.ODriveCAN(2)
    front_left_hip.initCanBus()
    time.sleep(sleep_time)

    #Front Right 
    front_right_knee = pyodrivecan.ODriveCAN(5)
    front_right_knee.initCanBus()
    time.sleep(sleep_time)

    front_right_shoulder = pyodrivecan.ODriveCAN(4)
    front_right_shoulder.initCanBus()
    time.sleep(sleep_time)

    front_right_hip = pyodrivecan.ODriveCAN(3)
    front_right_hip.initCanBus()
    time.sleep(sleep_time)
    #Back of Dog

    #Back Left 
    back_left_knee = pyodrivecan.ODriveCAN(6)
    back_left_knee.initCanBus()
    time.sleep(sleep_time)

    back_left_shoulder = pyodrivecan.ODriveCAN(7)
    back_left_shoulder.initCanBus()
    time.sleep(sleep_time)

    back_left_hip = pyodrivecan.ODriveCAN(8)
    back_left_hip.initCanBus()
    time.sleep(sleep_time)
    
    #Back Right 
    back_right_knee = pyodrivecan.ODriveCAN(11)
    back_right_knee.initCanBus()
    time.sleep(sleep_time)
    
    back_right_shoulder = pyodrivecan.ODriveCAN(10)
    back_right_shoulder.initCanBus()
    time.sleep(sleep_time)

    back_right_hip = pyodrivecan.ODriveCAN(9)
    back_right_hip.initCanBus()
    time.sleep(sleep_time)

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
            controller(front_left_knee, front_left_shoulder, front_left_hip,
                        front_right_knee, front_right_shoulder, front_right_hip,
                        back_left_knee, back_left_shoulder, back_left_hip,
                        back_right_knee, back_right_shoulder, back_right_hip) 
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