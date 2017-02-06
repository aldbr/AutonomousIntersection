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
		"""Drive strategy method : not complete"""
		vehicle.speed = KMUnityConverter.convert_KmH_to_unit(50)
		
		i = 0
		length = len(vehicle.traficPath.positions)
		insertArea = length/8
		acceleration_is_define = False

		j = 0

		while i < insertArea and vehicle.position is not None :
			vehicle.position = vehicle.traficPath.positions[i]
			i += vehicle.speed
			time.sleep(0.05)
		self.outOfTheAreaEvent.notifyObservers()
		while i < length and vehicle.position is not None :
			#if red light
			if not self.is_on :
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
					if j > 10000 :
						self.intersectionCrossedNotifier.notifyObservers()

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

	def is_after_light(self, vehicle):
		is_after = False
		try:
			red_light = vehicle.traficPath.signs[0]
			if red_light.position.axis.x == 0 :
				is_after = red_light.position.localization.x > vehicle.position.localization.x
			elif red_light.position.axis.x == 90 :
				is_after = red_light.position.localization.y < vehicle.position.localization.y
			elif red_light.position.axis.x == 180 :
				is_after = red_light.position.localization.x < vehicle.position.localization.x
			else :
				is_after = red_light.position.localization.y > vehicle.position.localization.y
		except AttributeError, e:
			is_after = True
		except Exception, e :
			print("Unknown error.")
		finally:
			return is_after

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





		


