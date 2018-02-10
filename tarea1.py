from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal
import time 
#dronekit-sitl copter --home:20.737213,-103.456819,1633,180
 
#conectar y despejar
def arm_and_takeoff(TargetAltitude):
	print ("Executing takeoff")
	#dice que se comenzara 

	#
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


#Vehicle Connection 
drone = connect('127.0.0.1:14551', wait_ready=True)
arm_and_takeoff(20)

#Velocidad
drone.airspeed = 10

#Primer punto
parada1 = LocationGlobalRelative(20.7374535, -103.4571305, 20)
print("El despegue fue exitoso")
print("EL dron va al primer vertice")
#dice que ira al punto
drone.simple_goto(parada1)
time.sleep(31)
print("Vertice 1 completado")
print("Volando al vertice dos")
#Segundo punto
parada2 = LocationGlobalRelative(20.7374018, -103.4565112, 20)
#dice que ira al punto
drone.simple_goto(parada2)
time.sleep(25)
print("Vertice 2 completado")
print("Volando al velrtice 3")
#Tercer punto
parada3 = LocationGlobalRelative(20.7369534, -103.4565377, 20)
#Dice que ira al punto 
drone.simple_goto(parada3)
time.sleep(25)
print("Vertice 3 completado")
print("Volando al vertice 4")
#Cuarto punto
parada4 = LocationGlobalRelative(20.7369985, -103.4571415, 20)
#Dice que ira al punto
drone.simple_goto(parada4)
time.sleep(25)
print("Vertice 4 completado")
#Vuelve a ir al punto 1
drone.simple_goto(parada1)
time.sleep(25)
print("Vertice 4 completado")
print("Volando al vertice 5")
#EL dron se pone en modo return to launch
print("Regresando a punto de despegue")
drone.mode = VehicleMode("RTL")
print("El dron regreso exitosamente")
#se muestra la bateria 
print("Battery level:")
print(drone.battery.voltage, "v")
