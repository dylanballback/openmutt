import pyodrivecan
import asyncio
from datetime import datetime, timedelta


#Example of how you can create a controller to get data from the O-Drives and then send motor comands based on that data.
async def controller(odrive1, odrive2, odrive3):
        #odrive1.set_position(0)
        #odrive2.set_position(0)
        #odrive3.set_position(0)

        #Run for set time delay example runs for 15 seconds.
        stop_at = datetime.now() + timedelta(seconds=15)
        while datetime.now() < stop_at:
            await asyncio.sleep(0) #Need this for async to work.

            
    
            

        #await asyncio.sleep(15) #no longer need this the timedelta =15 runs the program for 15 seconds.
        odrive1.running = False
        odrive2.running = False
        odrive3.running = False



# Run multiple busses.
async def main():
    #Set up Node_ID 1
    odrive1 = pyodrivecan.ODriveCAN(1)
    odrive1.initCanBus()

    #Set up Node_ID 2 
    odrive2 = pyodrivecan.ODriveCAN(2)
    odrive2.initCanBus()

    #Set up Node_ID 3 
    odrive3 = pyodrivecan.ODriveCAN(3)
    odrive3.initCanBus()

    #add each odrive to the async loop so they will run.
    await asyncio.gather(
        odrive1.loop(),
        odrive2.loop(),
        odrive3.loop(),
        controller(odrive1, odrive2, odrive3) 
    )

if __name__ == "__main__":
    asyncio.run(main())