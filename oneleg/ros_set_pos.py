import socket
import pyodrivecan
import asyncio
from datetime import datetime, timedelta
import time


positions = []


# Raspberry Pi's IP address and port
HOST = '0.0.0.0'  # All available interfaces
PORT = 3333

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)
print("Server listening on port", PORT)

# Accept a connection
client_socket, addr = server_socket.accept()
print("Connection from", addr)


# This async function will constantly get postion data from the socket.
async def get_socket(client_socket):
    while True:
        # Receive the command from the client
        command = client_socket.recv(1024).decode()
        positions = list(map(float,command.split(',')))
        print(positions)



async def controller(odrive1, odrive2, odrive3):
    global positions
    while True:
        if positions:
            print(f"Setting positions to: {positions}")
            if len(positions) == 3:
                odrive1.set_position(positions[0])
                await asyncio.sleep(0.05)
                odrive2.set_position(positions[1])
                await asyncio.sleep(0.05)
                odrive3.set_position(positions[2])
                await asyncio.sleep(0.05)

    stop_at = datetime.now() + timedelta(seconds=60)
    while datetime.now() < stop_at:
        
        #odrive1.set_position(10)  
        #odrive2.set_position(20)  
        #odrive3.set_position(30)

        print(f"Odrive1 Position: {odrive1.position}, Odrive2 Position: {odrive2.position}, Odrive3 Position: {odrive3.position}")
            




#This will calibrate the 0 postion to the current postion of the dog leg when the function is ran.
async def calibrate(odrive1, odrive2, odrive3):
    odrive1.set_absolute_position(0)
    odrive2.set_absolute_position(0)
    odrive3.set_absolute_position(0)
    await asyncio.sleep(0.2)


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
        time.sleep(0.2)
        odrive.clear_errors(identify=False)
        await asyncio.sleep(0.2)
        odrive.set_controller_mode(control_mode_name="position_control", input_mode_name="pos_filter")
        await asyncio.sleep(0.2)  # Delay to prevent command overlap on CAN bus
        time.sleep(0.2)

    #Calibrate first time O-Drive is powered up. 
    #Then comment out, if O-Drive is powered off, must calibrate again.
    await calibrate()



    try:
        await asyncio.gather(
        odrive1.loop(),
        odrive2.loop(),
        odrive3.loop(),
        controller(odrive1, odrive2, odrive3),
        get_socket(client_socket)
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
