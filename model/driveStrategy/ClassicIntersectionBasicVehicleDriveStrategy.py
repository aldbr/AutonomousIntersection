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

		all_is_define = False


		length = len(vehicle.traficPath.positions)
		while i < length and vehicle.position is not None :
			#if the light is red
			if not vehicle.traficPath.signs[0].is_green :
				
				all_is_define = False

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
				if not all_is_define :
					acceleration_is_define = False
					distance_is_define = False
					position_light_is_define = False

				#if there is a next vehicle			
				if vehicle.next_vehicle is not None and vehicle.next_vehicle.position is not None \
				and vehicle.position.axis.x == vehicle.next_vehicle.position.axis.x : 
					
					if vehicle.speed < vehicle.next_vehicle.speed :
						vehicle.speed = vehicle.next_vehicle.speed
						#acceleration_is_define = False
						#distance_is_define = False
					else :
						if not distance_is_define :
							distance1 = self.calculate_distance(vehicle.next_vehicle)
							distance2 = self.calculate_euclidean_distance(vehicle.next_vehicle.position.localization, vehicle.position.localization) #try catch
							distance = distance1 + distance2 - 5000
							distance_is_define = True

						if not acceleration_is_define : 
							vehicle.acceleration = self.calculate_acceleration_with_distance(vehicle, distance)
							acceleration_is_define = True
							all_is_define = True

						vehicle.slow_down(vehicle.acceleration)

				else :
					destination_direction = vehicle.traficPath.positions[-1].axis.x
					difference = (vehicle.position.axis.x - destination_direction)%360
					#if vehicle turn left
					if difference == 270 :
						face_vehicle = self.vehicle_in_front_of(vehicle) 
						if face_vehicle is not None : 
							#if both vehicles want to turn left
							if face_vehicle.traficPath.positions is not None \
							and (face_vehicle.traficPath.positions[-1].axis.x - vehicle.traficPath.positions[-1].axis.x)%360 == 180 :
								acceleration_is_define = False
								if vehicle.speed < KMUnityConverter.convert_KmH_to_unit(50):
									vehicle.accelerate(KMUnityConverter.convert_KmH_to_unit(0.60))
							else : 
								#if not self.is_after_light(face_vehicle) :
								if self.vehicule_can_pass(vehicle, face_vehicle):
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
		while not fin and i < len(vehicles_in_front_of) and vehicles_in_front_of[i].position is not None : 
			##if (vehicles_in_front_of[i].position.axis.x - vehicle.position.axis.x)%360 == 180 :
			if direction == 0 :
				if vehicle.position.localization.x < vehicles_in_front_of[i].position.localization.x:
					face_vehicle = vehicles_in_front_of[i]
					fin = True
			elif direction == 90 :
				if vehicle.position.localization.y > vehicles_in_front_of[i].position.localization.y:
					face_vehicle = vehicles_in_front_of[i]
					fin = True
			elif direction == 180 :
				if vehicle.position.localization.x > vehicles_in_front_of[i].position.localization.x:
					face_vehicle = vehicles_in_front_of[i]
					fin = True
			else :
				if vehicle.position.localization.y < vehicles_in_front_of[i].position.localization.y:
					face_vehicle = vehicles_in_front_of[i]
					fin = True
			i += 1
		return face_vehicle

	def vehicule_can_pass(self, vehicle, face_vehicle):
		if face_vehicle is None:
			return True
		direction = vehicle.position.axis.x
		if direction == 0 :
			return face_vehicle.position.localization.x > vehicle.position.localization.x
		elif direction == 90 :
			return face_vehicle.position.localization.y < vehicle.position.localization.y
		elif direction == 180 :
			return face_vehicle.position.localization.x < vehicle.position.localization.x
		else :
			return face_vehicle.position.localization.y > vehicle.position.localization.y
#return face_vehicle is not None and face_vehicle.position.localization.x > vehicle.position.localization.x

		


