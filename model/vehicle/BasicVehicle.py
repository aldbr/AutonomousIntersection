from Vehicle import *
import time

import sys
sys.path.append('..')

from converter.KmUnityConverter import *
from driveStrategy.ClassicIntersectionBasicVehicleDriveStrategy import *
from driveStrategy.AutonomousIntersectionBasicVehicleDriveStrategy import *

class BasicVehicle(Vehicle):
	"""Basic vehicle agent management : subclass of Vehicle"""

	
	def __init__(self, traficPath, traffic, next_vehicle):	
		Vehicle.__init__(self,traficPath, KMUnityConverter.convert_KmH_to_unit(50), next_vehicle)
		self.traffic = traffic
		self.driveStrategy = None
		
	def run(self):
		self.driveStrategy.drive(self)

	def accelerate(self, speed):
		"""Increase vehicle speed"""
		if speed > 0 :
			self.speed += speed

	def slow_down(self, speed):
		"""Decrease vehicle speed"""
		if speed >= 0 and speed < self.speed:
			self.speed -= speed
		else:
			self.speed = 0


