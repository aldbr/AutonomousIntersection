import sys
import os
 
CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
PARENT_FOLDER = os.path.dirname(CURRENT_FOLDER)
sys.path.append(PARENT_FOLDER)
from vehicle.Vehicle import *
from BasicVehicleDriveStrategy import *
from converter.KmUnityConverter import *

from math import *

import time

class ClassicIntersectionBasicVehicleDriveStrategy(BasicVehicleDriveStrategy):
	"""Drive strategy management for basic vehicles on classic intersection"""

	def drive(self, vehicle):
		"""Drive strategy method : not complete"""
		i = 0

		acceleration_is_define = False
		distance_is_define = False
		position_light_is_define = False


		length = len(vehicle.traficPath.positions)
		while i < length and vehicle.position is not None :
			#if the light is red
			if not vehicle.traficPath.signs[0].is_green :
				if vehicle.speed < KMUnityConverter.convert_KmH_to_unit(50) and not acceleration_is_define : #avoid speed = 0 at the beginning because of light change
					vehicle.speed = KMUnityConverter.convert_KmH_to_unit(50)

				#define the position of the vehicle and the next vehicle
				if not position_light_is_define : 
					after_light = self.is_after_light(vehicle)
					next_after_light = self.is_after_light(vehicle.next_vehicle)
					position_light_is_define = True
				#if the vehicle is before the red light
				if not after_light : 
					#if the next vehicle is before the red light
					if vehicle.next_vehicle is not None and vehicle.next_vehicle.position is not None and not next_after_light :
						
						if not distance_is_define :
							distance1 = self.calculate_distance(vehicle.next_vehicle)
							distance2 = self.calculate_euclidean_distance(vehicle.next_vehicle.position.localization, vehicle.position.localization)
							distance = distance1 + distance2 - 5000
							distance_is_define = True

						if not acceleration_is_define : 
							vehicle.acceleration = self.calculate_acceleration_with_distance(vehicle, distance)
							acceleration_is_define = True

						vehicle.slow_down(vehicle.acceleration)

					#if the next vehicle is after the red light
					else :
						
						if not acceleration_is_define :
							vehicle.acceleration = self.calculate_acceleration(vehicle, vehicle.traficPath.signs[0].position.localization)
							acceleration_is_define = True
						vehicle.slow_down(vehicle.acceleration)
				#if the vehicle is after the red light
				else :
					if vehicle.speed < KMUnityConverter.convert_KmH_to_unit(50):
						vehicle.accelerate(KMUnityConverter.convert_KmH_to_unit(0.60))
			#if the light is green
			else :
				acceleration_is_define = False
				distance_is_define = False
				position_light_is_define = False

				#if there is a next vehicle
				if vehicle.next_vehicle is not None and vehicle.next_vehicle.position is not None \
				and vehicle.position.axis.x == vehicle.next_vehicle.position.axis.x : 
					
					if vehicle.speed < vehicle.next_vehicle.speed :
						vehicle.speed = vehicle.next_vehicle.speed
						acceleration_is_define = False
						distance_is_define = False
					else :
						if not distance_is_define :
							distance1 = self.calculate_distance(vehicle.next_vehicle)
							distance2 = self.calculate_euclidean_distance(vehicle.next_vehicle.position.localization, vehicle.position.localization) #try catch
							distance = distance1 + distance2 - 5000
							distance_is_define = True

						if not acceleration_is_define : 
							vehicle.acceleration = self.calculate_acceleration_with_distance(vehicle, distance)
							acceleration_is_define = True

						vehicle.slow_down(vehicle.acceleration)

				else :
					destination_direction = vehicle.traficPath.positions[-1].axis.x
					difference = (vehicle.position.axis.x - destination_direction)%360
					#if vehicle turn left
					if difference == 270 : 
						face_vehicle = self.vehicle_in_front_of(vehicle) #strange
						if face_vehicle is not None : 
							#if both vehicles want to turn left
							if face_vehicle.traficPath.positions is not None \
							and (face_vehicle.traficPath.positions[-1].axis.x - vehicle.traficPath.positions[-1].axis.x)%360 == 180 :
								acceleration_is_define = False
								if vehicle.speed < KMUnityConverter.convert_KmH_to_unit(50):
									vehicle.accelerate(KMUnityConverter.convert_KmH_to_unit(0.60))
							else : 
								if not self.is_after_light(face_vehicle) :
									if not acceleration_is_define :
										vehicle.acceleration = self.calculate_acceleration(vehicle, vehicle.traficPath.signs[0].position.localization)
										acceleration_is_define = True
									vehicle.slow_down(vehicle.acceleration)
								else :
									if vehicle.speed < KMUnityConverter.convert_KmH_to_unit(50):
										vehicle.accelerate(KMUnityConverter.convert_KmH_to_unit(0.60))

						else :
							if vehicle.speed < KMUnityConverter.convert_KmH_to_unit(50):
								vehicle.accelerate(KMUnityConverter.convert_KmH_to_unit(0.60))

					else :
						if vehicle.speed < KMUnityConverter.convert_KmH_to_unit(50):
							vehicle.accelerate(KMUnityConverter.convert_KmH_to_unit(0.60))

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


		


