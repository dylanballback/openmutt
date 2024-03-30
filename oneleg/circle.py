import pyodrivecan
import asyncio
from datetime import datetime, timedelta

async def controller(odrive1, odrive2, odrive3):
    # Example trajectory control
    #odrive1.set_position(10)  # Set a desired position as an example
    #odrive2.set_position(20)  # Similarly, for other ODrives
    #odrive3.set_position(30)

    # Initialize positions
    target_position = 6.5
    position_limit1 = 6.5
    position_limit2 = -1.5

    # Set trajectory limits for smooth motion
    odrive1.set_traj_vel_limit(1.0)  # Set a low velocity limit for slow movement
    odrive1.set_traj_accel_limits(0.5, 0.5)  # Set low acceleration/deceleration for smoothness

    stop_at = datetime.now() + timedelta(seconds=60)
    while datetime.now() < stop_at:
        while odrive1.running:
            # Move ODrive 1 to the target position
            odrive1.set_position(target_position)
            
            # Wait until ODrive reaches the target position
            # This is a simple way to check - you might want to use a more sophisticated condition in practice
            await asyncio.sleep(5)  # Adjust sleep time based on actual movement speed and distance

            # Switch target position
            if target_position == position_limit1:
                target_position = position_limit2
            else:
                target_position = position_limit1

            print(f"ODrive1 Position: {odrive1.position}")
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
        odrive.set_traj_vel_limit(traj_vel_limit)
        odrive.set_traj_accel_limits(traj_accel_limit, traj_accel_limit)


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
