from math import *
import time

import sys
sys.path.append('..')
from converter.KmUnityConverter import *
from BasicVehicleDriveStrategy import *
from vehicle.Vehicle import *



class AutonomousIntersectionBasicVehicleDriveStrategy(BasicVehicleDriveStrategy):
	"""Drive strategy management for basic vehicles on autonomous intersection"""

	def drive(self, vehicle):
		"""Drive strategy method : not complete"""
		vehicle.speed = KMUnityConverter.convert_KmH_to_unit(50)
		i = 0

		length = len(vehicle.traficPath.positions)
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

	def calculate_acceleration_with_distance(self, vehicle, distance):
		"""Calculate deceleration to reach a point at 0km/h : not complete"""
		if distance != 0 :
			a = pow(vehicle.speed,2)/(2*distance) #warning speed = 0
		else : 
			vehicle.position = None #vehicle is at the beginning of the intersection with another vehicle
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

	def vehicle_in_front_of(self, vehicle):
		direction = vehicle.position.axis.x
		if direction == 0 :
				vehicles_in_front_of = vehicle.traffic.road3
		elif direction == 90 :
				vehicles_in_front_of = vehicle.traffic.road1
		elif direction == 180 :
				vehicles_in_front_of = vehicle.traffic.road2
		else :
				vehicles_in_front_of = vehicle.traffic.road4

		face_vehicle = None
		i = 0
		fin = False
		while not fin and i < len(vehicles_in_front_of) is not None and vehicles_in_front_of[i].position is not None : 
			if (vehicles_in_front_of[i].position.axis.x - vehicle.position.axis.x)%360 == 180 :
				face_vehicle = vehicles_in_front_of[i]
				fin = True
			i += 1
		return face_vehicle


		


