from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal
import time 


def arm_and_takeoff(TargetAltitude):
	print ("Executing takeoff")


	while not drone.is_armable:
		print ("Vehicle is not armable, waiting......")
		time.sleep(1)

	print ("Ready to arm")
	drone.mode = VehicleMode("GUIDED")
	drone.armed = True

	while not drone.armed:
		print("Waiting for arming...")
		time.sleep(1)

	print("ready for takeoff, taking off..")
	drone.simple_takeoff(TargetAltitude)

	while True:
		Altitude = drone.location.global_relative_frame.alt
		print("Altitude", Altitude)
		time.sleep(1)

		if Altitude >= TargetAltitude * 0.95:
			print("Altitude Reached")
			break


#Vehicle Connection 
drone = connect('127.0.0.1:14551', wait_ready=True)
arm_and_takeoff(20)

drone.airspeed = 10 

comienzo = LocationGlobalRelative(20.7372177, -103.4567878, 20)
punto1 = LocationGlobalRelative(20.7377382, -103.4570051, 20)
punto2 = LocationGlobalRelative(20.7376852, -103.4565226, 20)
punto3 = LocationGlobalRelative(20.7366728, -103.4565947, 20)
punto4 = LocationGlobalRelative(20.7367120, -103.4570822, 20)



drone.simple_goto(comienzo)
time.sleep(10)
print("Despegue exitoso")
print("Volando al punto1")

drone.simple_goto(punto1)
time.sleep(10)
print("Punto1 completado")
print("Volando al punto2")

drone.simple_goto(punto2)
time.sleep(10)
print("Punto2 completado")
print("Volando al punto3")

drone.simple_goto(punto3)
time.sleep(10)
print("Punto3 completado")
print("Volando al punto4")

drone.simple_goto(punto4)
time.sleep(10)
print("Punto 4 completado")
print("Volando al punto de despegue")

print("Regresando a punto de despegue")
drone.mode = VehicleMode("RTL")
print("El dron regreso exitosamente")

print(" Battery: %s" % vehicle.battery", "V")

