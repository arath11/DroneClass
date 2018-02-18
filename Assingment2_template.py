#dronekit-sitl copter --home=20.737213,-103.456819,01633,180


import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
import Tkinter as tk

#****************************************************************************
#   Method Name     : set_velocity_body
#
#   Description     : Sends a MAVLINK velocity command in body frame reference
#                     This means that the X, Y, Z axis will be in relation to the 
#                     vehicle. 
#                     Positive X values will move the drone forward
#                     Positive Y values will move the drone Right
#                     Positive Z values will move the drone down
#                     The values for vx, vy and vz are in m/s, so sending a value
#                     of say 5 in vx will move the drone forward at 5 m/s
#
#                     More information can be found here:
#                     http://ardupilot.org/dev/docs/copter-commands-in-guided-mode.html
#
#   Parameters      : vehicle:  vehicle instance to send the command to
#                     vx:       Velocity in the X axis 
#                     vy
#                     vz
#
#   Return Value    : None
#
#   Author           : tiziano fiorenzani
#
#****************************************************************************
#se define el movimiento del dron con velocidades en x,y y z. Despues se envia al simulador mediante mavlink
def set_velocity_body(vehicle, vx, vy, vz):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
            0,
            0, 0,
            mavutil.mavlink.MAV_FRAME_BODY_NED,
            0b0000111111000111, #-- BITMASK -> Consider only the velocities
            0, 0, 0,        #-- POSITION
            vx, vy, vz,     #-- VELOCITY
            0, 0, 0,        #-- ACCELERATIONS
            0, 0)
    vehicle.send_mavlink(msg)
    vehicle.flush()

#****************************************************************************
#   Method Name     : arm_and_takeoff
#
#   Description     : Add your takeoff function from your last assignment here
#
#   Parameters      : targetAltitude
#
#   Return Value    : None
#
#   Author           : You
#
#****************************************************************************
def arm_and_takeoff(TargetAltitude):
    print ("Executing takeoff")
    #dice que se comenzara 


    while not drone.is_armable:
        print ("Vehicle is not armable, waiting......")
        time.sleep(1)

    #Lo pone en modo guiado 
    print ("Ready to arm")
    drone.mode = VehicleMode("GUIDED")
    drone.armed = True

    #en caso de que no este armado, dira que aun no esta armado 
    while not drone.armed:
        print("Waiting for arming...")
        time.sleep(1)

    #el dron despegara
    print("ready for takeoff, taking off..")
    drone.simple_takeoff(TargetAltitude)

    #verifica que el dron este a la altura desead, en este caso 20 metros 
    while True:
        Altitude = drone.location.global_relative_frame.alt
        print("Altitude", Altitude)
        time.sleep(1)
        #el dron se tarda en llegar a los 20 metros exactos as que usamos esto para que simule que llego a 20 metros 
        if Altitude >= TargetAltitude * 0.95:
            print("Altitude Reached")
            break


#****************************************************************************
#   Method Name     : key
#
#   Description     : Callback for TkInter Key events
#
#   Parameters      : Event: tkinter event containing the key that was pressed
#
#   Return Value    : None
#
#   Author           : You
#
#****************************************************************************
def key(event):
    if event.char == event.keysym: #si se presiona r, el dron regresara al punto de lanzamiento 
        if event.keysym == 'r':
            drone.mode = VehicleMode("RTL")            
    else: #cada una de las siguientes opcines mueve al dron mediante x y y
        if event.keysym == 'Up':
            set_velocity_body(drone,5,0,0)
        elif event.keysym == 'Down':
            set_velocity_body(drone,5,0,0)
        elif event.keysym == 'Left':
            set_velocity_body(drone,0,5,0)
        elif event.keysym == 'Right':
            set_velocity_body(drone,0,5,0)

#****************************************************************************
#   MAIN CODE
#
#****************************************************************************

### add your code to connect to the drone here ###

drone = connect('127.0.0.1:14551', wait_ready=True)
arm_and_takeoff(10)
 
# Read the keyboard with tkinter
#aqui se activa la funcion key, con la cual se puede asignar el movimiento al dron mediante un if
root = tk.Tk() 
print(">> Control the drone with the arrow keys. Press r for RTL mode")
root.bind_all('<Key>', key) 
root.mainloop() #repite 