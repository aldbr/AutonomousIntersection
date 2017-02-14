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
		self.intersectionCrossedNotifier = \
		AutonomousIntersectionBasicVehicleDriveStrategy.IntersectionCrossedNotifier()
		self.is_on = False
	
	def drive(self, vehicle):
		"""Drive strategy method"""
		vehicle.speed = KMUnityConverter.convert_KmH_to_unit(50)
		
		i = 0
		length = len(vehicle.traficPath.positions)
		insertArea = length/8
		acceleration_is_define = False
		distance_is_define = False

		j = 0
		fin = 0

		while i < insertArea and vehicle.position is not None :
			vehicle.position = vehicle.traficPath.positions[i]
			i += vehicle.speed
			time.sleep(0.05)
		self.outOfTheAreaEvent.notifyObservers()
		while i < length and vehicle.position is not None :
			#if red light
			if not self.is_on :
				if vehicle.next_vehicle is not None and vehicle.next_vehicle.position is not None and \
				 not vehicle.next_vehicle.driveStrategy.is_on :
					
					if not distance_is_define :
						distance1 = self.calculate_distance(vehicle.next_vehicle)
						distance2 = self.calculate_euclidean_distance(vehicle.next_vehicle.position.localization, vehicle.position.localization)
						distance = distance1 + distance2 - 5000
						distance_is_define = True

						if not acceleration_is_define : 
							vehicle.acceleration = self.calculate_acceleration_with_distance(vehicle, distance)
							acceleration_is_define = True
				else :
					if not acceleration_is_define :
						vehicle.acceleration = self.calculate_acceleration(vehicle, vehicle.traficPath.signs[0].position.localization)
						acceleration_is_define = True
				
				vehicle.slow_down(vehicle.acceleration)
			#if green light
			else :
				if vehicle.speed < KMUnityConverter.convert_KmH_to_unit(50):
					vehicle.accelerate(KMUnityConverter.convert_KmH_to_unit(0.60))

				if self.is_after_light(vehicle) :
					j += vehicle.speed
					if j > 10000 and not fin: #distance to travel intersection
						self.intersectionCrossedNotifier.notifyObservers()
						fin = 1

			vehicle.position = vehicle.traficPath.positions[i]
			i += vehicle.speed
			time.sleep(0.05)


		vehicle.position = None			
					


	class OutOfTheAreaNotifier(Observable):
		def __init__(self):
			Observable.__init__(self)
		def notifyObservers(self):
			self.setChanged()
			Observable.notifyObservers(self)


	class IntersectionCrossedNotifier(Observable):
		def __init__(self):
			Observable.__init__(self)
		def notifyObservers(self):
			self.setChanged()
			Observable.notifyObservers(self)





		


