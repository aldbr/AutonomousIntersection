from math import *

import sys
sys.path.append('..')
from converter.KmUnityConverter import *
from vehicle.Vehicle import *
from DriveStrategy import *

from abc import ABCMeta, abstractmethod

class BasicVehicleDriveStrategy(DriveStrategy):
	__metaclass__=ABCMeta
	"""Drive strategy management for basic vehicles"""

	@abstractmethod
	def drive(self, vehicle):
		pass


	def calculate_acceleration(self, vehicle, localization):
		"""Calculate deceleration to reach a point at 0km/h : not complete"""

		dist = sqrt(pow(vehicle.position.localization.x-localization.x,2)\
			+pow(vehicle.position.localization.y-localization.y,2))*(1/KMUnityConverter.step)
		if dist != 0 :
			a = pow(vehicle.speed,2)/(2*dist)
		else :
			a = vehicle.speed

		return int(a)

	def calculate_distance(self, vehicle):
		if vehicle.acceleration != 0 :
			distance = pow(vehicle.speed,2)/(2*vehicle.acceleration)
		else : 
			distance = 20000
		return int(distance)

	def calculate_euclidean_distance(self, local1, local2):
		dist = sqrt(pow(local1.x-local2.x,2)\
			+pow(local1.y-local2.y,2))*(1/KMUnityConverter.step)
		return dist

	def calculate_acceleration_with_distance(self, vehicle, distance):
		"""Calculate deceleration to reach a point at 0km/h : not complete"""
		if distance != 0 :
			a = pow(vehicle.speed,2)/(2*distance) #warning speed = 0
		else : 
			vehicle.position = None #vehicle is at the beginning of the intersection with another vehicle
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