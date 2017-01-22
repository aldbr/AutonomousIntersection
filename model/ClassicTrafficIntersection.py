from threading import Thread
import time

from IntersectionTraffic import *
from datetime import datetime

class ClassicTrafficIntersection(IntersectionTraffic):
	"""Classic intersection agent management : subclass of IntersectionTraffic"""

	def __init__(self, filenamePaths, trafficName):
		Thread.__init__(self)
		IntersectionTraffic.__init__(self, filenamePaths, trafficName)
		self.road1 = []
		self.road2 = []
		self.road3 = []
		self.road4 = []
		self.is_green = True

		self.maxVehiculeTimePath = 0 # Maximum travel time of a vehicle
		self.minVehiculeTimePath = 999 # Minimum travel time of a vehicle
		self.sumVehiculeTimePath = 0 # Sum of travel times of all vehicles
		self.nbVehicules = 0 #Number of vehicles which have crossed the intersection

	def add(self, vehicle):
		"""Add the car on the correct road depending on its source position"""		
		vehicle.timeStart = datetime.now()

		if vehicle.position.localization.x < 0 and vehicle.position.localization.y < 0:
			if len(self.road1) > 0 :
				vehicle.next_vehicle = self.road1[-1]
			self.road1.append(vehicle)
		elif vehicle.position.localization.x < 0 and vehicle.position.localization.y > 0:
			if len(self.road2) > 0 :
				vehicle.next_vehicle = self.road2[-1]
			self.road2.append(vehicle)
		elif vehicle.position.localization.x > 0 and vehicle.position.localization.y < 0:
			if len(self.road3) > 0 :
				vehicle.next_vehicle = self.road3[-1]
			self.road3.append(vehicle)
		else:
			if len(self.road4) > 0 :
				vehicle.next_vehicle = self.road4[-1]
			self.road4.append(vehicle)

	def __getitem__(self, index):
		"""Return a car depending on the index : used for browse all the items"""
		elt = None
		
		s1 = len(self.road1)
		s2 = len(self.road2)
		s3 = len(self.road3)
		s4 = len(self.road4)
		if s1 > index:
			elt = self.road1[index]
		elif s1+s2 > index:
			elt = self.road2[index-s1]
		elif s1+s2+s3 > index:
			elt = self.road3[index-(s1+s2)]
		else:
			elt = self.road4[index-(s1+s2+s3)]
		return elt

	def __delitem__(self, index):
		"""Delete a car depending on the index : used for delete all the items"""
		s1 = len(self.road1)
		s2 = len(self.road2)
		s3 = len(self.road3)
		s4 = len(self.road4)
		
		
		if s1 > index:
			diff = datetime.now() - self.road1[index].timeStart		
			del self.road1[index]
		elif s1+s2 > index:
			diff = datetime.now() - self.road2[index-s1].timeStart
			del self.road2[index-s1]
		elif s1+s2+s3 > index:
			diff = datetime.now() - self.road3[index-(s1+s2)].timeStart
			del self.road3[index-(s1+s2)]
		else:
			diff = datetime.now() - self.road4[index-(s1+s2+s3)].timeStart
			del self.road4[index-(s1+s2+s3)]

		vehiculeTimePath = diff.total_seconds() #Travel time of a vehicle

		if vehiculeTimePath < self.minVehiculeTimePath:
			self.minVehiculeTimePath = vehiculeTimePath
		elif vehiculeTimePath > self.maxVehiculeTimePath:
			self.maxVehiculeTimePath = vehiculeTimePath 

		self.sumVehiculeTimePath += vehiculeTimePath 
		self.nbVehicules += 1
		if self.nbVehicules%30 ==0:
			filenameSaveTimes = self.trafficName+"_times.txt"
			#Save of travel times
			try:
				file = open(filenameSaveTimes, "w")
				file.write("Mean={}\nMin={}\nMax={}\n".format(self.sumVehiculeTimePath/self.nbVehicules, self.minVehiculeTimePath, self.maxVehiculeTimePath))
				file.close()
			except IOError:
				print "Could not open file {} !".format(filenameSaveTimes)
	   

	def run(self):
		"""Social behaviour of the classic intersection"""
		while 1 : 
			start = time.time()
			
			if self.is_green :
				self.is_green = False
			else :
				self.is_green = True

			total = 0
			while total < 30:
				if self.is_green :
					for v in self.road1:
						v.traficPath.signs[0].is_green = True
					for v in self.road4:
						v.traficPath.signs[0].is_green = True
					for v in self.road2:
						v.traficPath.signs[0].is_green = False
					for v in self.road3:
						v.traficPath.signs[0].is_green = False
				else:
					for v in self.road1:
						v.traficPath.signs[0].is_green = False
					for v in self.road4:
						v.traficPath.signs[0].is_green = False
					for v in self.road2:
						v.traficPath.signs[0].is_green = True
					for v in self.road3:
						v.traficPath.signs[0].is_green = True
				time.sleep(0.1)
				end = time.time()
				total = end - start




