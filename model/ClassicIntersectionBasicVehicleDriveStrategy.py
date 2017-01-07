from Vehicle import *
from BasicVehicleDriveStrategy import *
from KmUnityConverter import *

from math import *

import time

class ClassicIntersectionBasicVehicleDriveStrategy(BasicVehicleDriveStrategy):
	"""Drive strategy management for basic vehicles on classic intersection"""

	def drive2(self, vehicle):
		"""Drive strategy method : not complete"""
		i = 0
		j = 0

		acceleration_is_define = False

		length = len(vehicle.traficPath.positions)
		while i < length :
			if vehicle.traficPath.signs[0].is_green :
				acceleration_is_define = False
				if vehicle.speed < KMUnityConverter.convert_KmH_to_unit(50):
					vehicle.accelerate(KMUnityConverter.convert_KmH_to_unit(0.41))
			else:
				if not acceleration_is_define :
					a = self.calculate_acceleration(vehicle, vehicle.traficPath.signs[0].position.localization)
					acceleration_is_define = True
				vehicle.slow_down(a)

			vehicle.position = vehicle.traficPath.positions[i]
			i += vehicle.speed
			time.sleep(0.05)
			
		vehicle.position = None


	def drive(self, vehicle):
		"""Drive strategy method : not complete"""
		i = 0
		j = 0

		acceleration_is_define = False
		distance_is_define = False
		position_light_is_define = False

		length = len(vehicle.traficPath.positions)
		while i < length and vehicle.position is not None :
			if not vehicle.traficPath.signs[0].is_green :
				
				if not position_light_is_define : 
					after_light = self.is_after_light(vehicle)
					next_after_light = self.is_after_light(vehicle.next_vehicle)
					position_light_is_define = True
				
				if not after_light : 
					if vehicle.next_vehicle is not None and not next_after_light :
						
						if vehicle.next_vehicle.acceleration != 0 : #this line is not normal
							if not distance_is_define :
								distance1 = self.calculate_distance(vehicle.next_vehicle)
								distance2 = self.calculate_euclidean_distance(vehicle.next_vehicle.position.localization, vehicle.position.localization)
								distance = distance1 + distance2 - 3000

								distance_is_define = True

							if not acceleration_is_define : 
								vehicle.acceleration = self.calculate_acceleration_with_distance(vehicle, distance)
								acceleration_is_define = True
							vehicle.slow_down(vehicle.acceleration)
					else :
						
						if not acceleration_is_define :
							vehicle.acceleration = self.calculate_acceleration(vehicle, vehicle.traficPath.signs[0].position.localization)
							acceleration_is_define = True
						vehicle.slow_down(vehicle.acceleration)
				else :
					if vehicle.speed < KMUnityConverter.convert_KmH_to_unit(50):
						vehicle.accelerate(KMUnityConverter.convert_KmH_to_unit(0.41))
			else :
				acceleration_is_define = False
				distance_is_define = False
				position_light_is_define = False

				if vehicle.next_vehicle :
					vehicle.speed = vehicle.next_vehicle.speed
				else :
					if vehicle.speed < KMUnityConverter.convert_KmH_to_unit(50):
						vehicle.accelerate(KMUnityConverter.convert_KmH_to_unit(0.41))

			vehicle.position = vehicle.traficPath.positions[i]
			i += vehicle.speed
			time.sleep(0.05)

		vehicle.position = None			
					


	def calculate_acceleration(self, vehicle, localization):
		"""Calculate deceleration to reach a point at 0km/h : not complete"""

		dist = sqrt(pow(vehicle.position.localization.x-localization.x,2)\
			+pow(vehicle.position.localization.y-localization.y,2))*(1/KMUnityConverter.step)
		a = pow(vehicle.speed,2)/(2*dist)

		return int(a)

	def calculate_acceleration_with_distance(self, vehicle, distance):
		"""Calculate deceleration to reach a point at 0km/h : not complete"""
		try:
			a = pow(vehicle.speed,2)/(2*distance)
		except ZeroDivisionError, e:
			vehicle.position = None #vehicle is at the beginning of the intersection with another vehicle
			a = 0
		finally:
			return int(a)

	def calculate_distance(self, vehicle):
		try:
			distance = pow(vehicle.speed,2)/(2*vehicle.acceleration)
		except ZeroDivisionError, e:
			distance = 20000 #TODO
			print(vehicle.acceleration)
		finally:
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
		


