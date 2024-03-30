import pyodrivecan
import asyncio
from datetime import datetime, timedelta
import time
# Points for ODrive movements
points = [
    [-0.75, 3.12],  # point1
    [-0.38, 3.84],  # point2
    [-0.04, 3.58],  # point3
    [-0.94, 2.52]   # point4
]

async def controller(odrive1, odrive2, odrive3):
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
    point_index = 0

    while datetime.now() < stop_at:
        # Get the target positions for ODrive1 and ODrive2 from the points list
        target_position_1, target_position_2 = points[point_index]

        # Move ODrive1 and ODrive2 to the target positions
        odrive1.set_position(target_position_1)
        odrive2.set_position(target_position_2)

        # Wait before moving to the next point
        await asyncio.sleep(1.2)  # Adjust sleep time based on actual movement speed and distance

        # Update point_index to move to the next set of points
        point_index = (point_index + 1) % len(points)

        print(f"Odrive1 Position: {odrive1.position}, Odrive2 Position: {odrive2.position}, Odrive3 Position: {odrive3.position}")

    # Stop the loop after the time expires
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
    odrive1 = pyodrivecan.ODriveCAN(1)
    odrive1.initCanBus()

    odrive2 = pyodrivecan.ODriveCAN(2)
    odrive2.initCanBus()

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
    asyncio.run(main())
