from Vehicle import *
from BasicVehicleDriveStrategy import *
from KmUnityConverter import *

from math import *

import time

class ClassicIntersectionBasicVehicleDriveStrategy(BasicVehicleDriveStrategy):

	def drive(self, vehicle):
		i = 0
		j = 0

		acceleration_is_define = False

		length = len(vehicle._traficPath.positions)
		while i < length :
			if vehicle.is_on:
				acceleration_is_define = False
				if vehicle.speed < KMUnityConverter.convert_KmH_to_unit(50):
					vehicle.accelerate(KMUnityConverter.convert_KmH_to_unit(0.41))
			else:
				if not acceleration_is_define :
					a = self.calculate_acceleration(vehicle)
					acceleration_is_define = True
				vehicle.slow_down(a)

			vehicle._position = vehicle._traficPath.positions[i]
			i += vehicle.speed
			time.sleep(0.05)
			
		vehicle._position = None

	def calculate_acceleration(self, vehicle):
		redlight_x_pos = 2.5 #TODO
		redlight_y_pos = 7 #TODO

		dist = sqrt(pow(vehicle._position.x-redlight_x_pos,2)+pow(vehicle._position.y-redlight_y_pos,2))*(1/KMUnityConverter.step)
		a = pow(vehicle.speed,2)/(2*dist)
		return int(a)
