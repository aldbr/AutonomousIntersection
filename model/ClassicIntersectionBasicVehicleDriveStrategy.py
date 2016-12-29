from Vehicle import *
from BasicVehicleDriveStrategy import *

import time

class ClassicIntersectionBasicVehicleDriveStrategy(BasicVehicleDriveStrategy):

	def drive(self, vehicle):
		state_change = 0
		i = 0
		length = len(vehicle._traficPath.positions)
		while i < length :
			if vehicle.is_on:
				if vehicle.speed < 10:
					vehicle.accelerate(5)
			else:
				if vehicle.speed > 1:
					vehicle.slow_down(5)

			vehicle._position = vehicle._traficPath.positions[i]
			i += vehicle.speed
			time.sleep(0.05)
			
		vehicle._position = None
