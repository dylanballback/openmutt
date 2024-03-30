import pyodrivecan
import asyncio
from datetime import datetime, timedelta
import time

async def controller(odrive1, odrive2, odrive3):
    # Example trajectory control
    #odrive1.set_position(10)  # Set a desired position as an example
    #odrive2.set_position(20)  # Similarly, for other ODrives
    #odrive3.set_position(30)

    # Initialize positions for odrive1
    target_position_1 = 6.5
    position_limit1_1 = 6.5
    position_limit2_1 = -1.5


    # Initialize positions for odrive2
    target_position_2 = 4.1
    position_limit1_2 = 4.1
    position_limit2_2 = -1.2

    # Set trajectory limits for smooth motion for odrive1
    odrive1.set_traj_vel_limit(1.0)  # Example velocity limit
    await asyncio.sleep(0.1)
    odrive1.set_traj_accel_limits(0.1, 0.1)  # Example accel/decel limits
    await asyncio.sleep(0.1)

    # Set trajectory limits for smooth motion for odrive2
    odrive2.set_traj_vel_limit(1.0)  # Example velocity limit
    await asyncio.sleep(0.1)
    odrive2.set_traj_accel_limits(0.1, 0.1)  # Example accel/decel limit
    await asyncio.sleep(0.1)


    stop_at = datetime.now() + timedelta(seconds=60)
    while datetime.now() < stop_at:
        while datetime.now() < stop_at and odrive1.running and odrive2.running:
            # Move ODrive 1 to the target position
            odrive1.set_position(target_position_1)
            # Move ODrive 2 to the target position
            odrive2.set_position(target_position_2)

            # Wait before checking position again
            await asyncio.sleep(2)  # Adjust sleep time based on actual movement speed and distance

            # Switch target position for odrive1
            if target_position_1 == position_limit1_1:
                target_position_1 = position_limit2_1
            else:
                target_position_1 = position_limit1_1

            # Switch target position for odrive2
            if target_position_2 == position_limit1_2:
                target_position_2 = position_limit2_2
            else:
                target_position_2 = position_limit1_2

            print(f"Odrive1 Position: {odrive1.position}, Odrive2 Position: {odrive2.position}, Odrive3 Position: {odrive3.position}")
            

    odrive1.running = False
    odrive2.running = False
    odrive3.running = False




def estop_all(odrive1, odrive2, odrive3):
    odrive1.estop()
    odrive2.estop()
    odrive3.estop()
    print("Emergency stop activated for all ODrives.")


def shutdown_all(odrive1, odrive2, odrive3):
    odrive1.bus_shutdown()
    odrive2.bus_shutdown()
    odrive3.bus_shutdown()



current_limit = 35.0
velocity_limit = 10.0

traj_vel_limit = 1.0
traj_accel_limit = 0.5

async def main():
    # Set up Node_ID 1
    odrive1 = pyodrivecan.ODriveCAN(1)
    odrive1.initCanBus()
    #odrive1.setAxisState("closed_loop_control")

    # Set up Node_ID 2
    odrive2 = pyodrivecan.ODriveCAN(2)
    odrive2.initCanBus()
    

    # Set up Node_ID 3
    odrive3 = pyodrivecan.ODriveCAN(3)
    odrive3.initCanBus()

    # Configure each ODrive
    for odrive in (odrive1, odrive2, odrive3):
        odrive.set_limits(velocity_limit=velocity_limit, current_limit=current_limit)
        time.sleep(0.1)
        odrive.set_traj_vel_limit(traj_vel_limit)
        time.sleep(0.1)
        odrive.set_traj_accel_limits(traj_accel_limit, traj_accel_limit)
        time.sleep(0.1)


    try:
        await asyncio.gather(
        odrive1.loop(),
        odrive2.loop(),
        odrive3.loop(),
        controller(odrive1, odrive2, odrive3)
        )
    except KeyboardInterrupt:
        estop_all(odrive1, odrive2, odrive3)
    finally:
        shutdown_all(odrive1, odrive2, odrive3)

    

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Program terminated with keyboard interrupt.")
