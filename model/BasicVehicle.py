from Vehicle import *
from KmUnityConverter import *
from ClassicIntersectionBasicVehicleDriveStrategy import *

import time

class BasicVehicle(Vehicle):

	
	def __init__(self, traficPath, traffic):	
		Vehicle.__init__(self,traficPath, KMUnityConverter.convert_KmH_to_unit(50))
		self.traffic = traffic
		self.is_on = False

		self.driveStrategy = ClassicIntersectionBasicVehicleDriveStrategy()
		


	def run(self):
		self.driveStrategy.drive(self)

	def accelerate(self, speed):
		if speed > 0 :
			self.speed += KMUnityConverter.convert_KmH_to_unit(speed)

	def slow_down(self, speed):
		if speed > 0 and speed < self.speed:
			self.speed -= KMUnityConverter.convert_KmH_to_unit(speed)
		else:
			self.speed = 0


