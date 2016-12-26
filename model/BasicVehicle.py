from Vehicle import *
from KmUnityConverter import *

import time

class BasicVehicle(Vehicle):

	
	def __init__(self, traficPath):	
		Vehicle.__init__(self,traficPath, KMUnityConverter.convert_KmH_to_unit(50))
		pass


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
		i = 0
		length = len(self._traficPath.positions)
		while i < length :
			self._position = self._traficPath.positions[i]
			i += self.speed
			time.sleep(0.05)
			#self.slow_down(5)
		self._position = None


