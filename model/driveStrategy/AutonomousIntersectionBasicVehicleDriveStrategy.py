from math import *
import time

import sys
sys.path.append('..')
from converter.KmUnityConverter import *
from BasicVehicleDriveStrategy import *
from vehicle.Vehicle import *
from observer.Observable import *



class AutonomousIntersectionBasicVehicleDriveStrategy(BasicVehicleDriveStrategy):
	"""Drive strategy management for basic vehicles on autonomous intersection"""

	def __init__(self) :
		self.outOfTheAreaEvent = AutonomousIntersectionBasicVehicleDriveStrategy.OutOfTheAreaNotifier()
	
	def drive(self, vehicle):
		"""Drive strategy method : not complete"""
		vehicle.speed = KMUnityConverter.convert_KmH_to_unit(50)
		i = 0

		length = len(vehicle.traficPath.positions)
		insertArea = length/10
		while i < insertArea and vehicle.position is not None :
			vehicle.position = vehicle.traficPath.positions[i]
			i += vehicle.speed
			time.sleep(0.05)
		self.outOfTheAreaEvent.notifyObservers()
		while i < length and vehicle.position is not None :
			vehicle.position = vehicle.traficPath.positions[i]
			i += vehicle.speed
			time.sleep(0.05)


		vehicle.position = None			
					


	def calculate_acceleration(self, vehicle, localization):
		"""Calculate deceleration to reach a point at 0km/h : not complete"""

		dist = sqrt(pow(vehicle.position.localization.x-localization.x,2)\
			+pow(vehicle.position.localization.y-localization.y,2))*(1/KMUnityConverter.step)
		if dist != 0 :
			a = pow(vehicle.speed,2)/(2*dist)
		else :
			a = vehicle.speed

		return int(a)

	class OutOfTheAreaNotifier(Observable):
		def __init__(self):
			Observable.__init__(self)
		def notifyObservers(self):
			self.setChanged()
			Observable.notifyObservers(self)



		


