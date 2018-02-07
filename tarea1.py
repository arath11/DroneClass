from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal
import time 

#conectar y despejar
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

#Velocidad
drone.airspeed = 10

#Primer punto
parada1 = LocationGlobalRelative(20.737395, -103.456960, 20)
print("El despegue fue exitoso")
print("EL dron va al primer vertice")
drone.simple_goto(parada1)
time.sleep(25)
print("Vertice 1 completado")
print("Volando al vertice dos")

parada2 = LocationGlobalRelative(20.737370, -103.456715, 20)
drone.simple_goto(parada2)
time.sleep(25)
print("Vertice 2 completado")
print("Volando al velrtice 3")

parada3 = LocationGlobalRelative(20.7370528, -103.4567228, 20)
drone.simple_goto(parada3)
time.sleep(25)
print("Vertice 3 completado")
print("Volando al vertice 4")

parada4 = LocationGlobalRelative(20.737084, -103.456945, 20)
drone.simple_goto(parada4)
time.sleep(25)
print("Vertice 4 completado")

drone.simple_goto(parada1)
time.sleep(25)
print("Vertice 4 completado")
print("Volando al vertice 5")

print("Regresando a punto de despegue")
drone.mode = VehicleMode("RTL")
print("El dron regreso exitosamente")

print(drone.battery.voltage, "v")
