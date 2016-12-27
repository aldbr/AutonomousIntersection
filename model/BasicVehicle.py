from Vehicle import *
from KmUnityConverter import *

import time

class BasicVehicle(Vehicle):

	
	def __init__(self, traficPath, traffic):	
		Vehicle.__init__(self,traficPath, KMUnityConverter.convert_KmH_to_unit(50))
		self.traffic = traffic
		self.is_on = False
		


	def run(self):
		Vehicle.run(self)

	def accelerate(self, speed):
		if speed > 0 :
			self.speed += KMUnityConverter.convert_KmH_to_unit(speed)

	def slow_down(self, speed):
		if speed > 0 and speed < self.speed:
			self.speed -= KMUnityConverter.convert_KmH_to_unit(speed)
		else:
			self.speed = 0



	def rouler(self):
		state_change = 0
		i = 0
		length = len(self._traficPath.positions)
		while i < length :
			if self.is_on:
				if self.speed < 10:
					self.accelerate(5)
			else:
				if self.speed > 1:
					self.slow_down(5)

			self._position = self._traficPath.positions[i]
			i += self.speed
			time.sleep(0.05)
			
		self._position = None


