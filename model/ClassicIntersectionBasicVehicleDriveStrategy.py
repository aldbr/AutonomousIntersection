from Vehicle import *
from BasicVehicleDriveStrategy import *
from KmUnityConverter import *

from math import *

import time

class ClassicIntersectionBasicVehicleDriveStrategy(BasicVehicleDriveStrategy):
	"""Drive strategy management for basic vehicles on classic intersection"""

	def drive(self, vehicle):
		"""Drive strategy method : not complete"""
		i = 0
		j = 0

		acceleration_is_define = False

		length = len(vehicle._traficPath.positions)
		while i < length :
			if vehicle.traficPath.signs[0].is_green :
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
		"""Calculate deceleration to reach a point at 0km/h : not complete"""
		red_light = vehicle._traficPath.signs[0]

		dist = sqrt(pow(vehicle._position.x-red_light.position.x,2)+pow(vehicle._position.y-red_light.position.y,2))*(1/KMUnityConverter.step)
		a = pow(vehicle.speed,2)/(2*dist)
		return int(a)
