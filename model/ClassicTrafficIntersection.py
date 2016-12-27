from threading import Thread
import time

from IntersectionTraffic import *

class ClassicTrafficIntersection(IntersectionTraffic):

	def __init__(self, filename):
		Thread.__init__(self)
		IntersectionTraffic.__init__(self, filename)
		self.road1 = []
		self.road2 = []
		self.road3 = []
		self.road4 = []
		self.is_green = True

	def add(self, vehicle):
		if vehicle.position.x < 0 and vehicle.position.y < 0:
			self.road1.append(vehicle)
		elif vehicle.position.x < 0 and vehicle.position.y > 0:
			self.road2.append(vehicle)
		elif vehicle.position.x > 0 and vehicle.position.y < 0:
			self.road3.append(vehicle)
		else:
			self.road4.append(vehicle)

	def __getitem__(self, index):
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
		s1 = len(self.road1)
		s2 = len(self.road2)
		s3 = len(self.road3)
		s4 = len(self.road4)
		
		if s1 > index:
			del self.road1[index]
		elif s1+s2 > index:
			del self.road2[index-s1]
		elif s1+s2+s3 > index:
			del self.road3[index-(s1+s2)]
		else:
			del self.road4[index-(s1+s2+s3)]

	def run(self):
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
						v.is_on = True
					for v in self.road4:
						v.is_on = True
					for v in self.road2:
						v.is_on = False
					for v in self.road3:
						v.is_on = False
				else:
					for v in self.road1:
						v.is_on = False
					for v in self.road4:
						v.is_on = False
					for v in self.road2:
						v.is_on = True
					for v in self.road3:
						v.is_on = True
				time.sleep(0.1)
				end = time.time()
				total = end - start




