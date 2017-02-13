from threading import Thread
import time
import numpy

from traffic.ClassicTrafficIntersection import *
from vehicle.BasicVehicle import *

class Model(Thread):
	"""Simulation management""" 

	def __init__(self, traffic):
		Thread.__init__(self)
		self.vehicles = []
		self.count = 0
		self.traffic = traffic
		self.rand_generator = numpy.random.RandomState(242)


	def run(self):
		"""Create agent on the road environment"""
		poisson = self.rand_generator.poisson(2, 100)
		self.traffic.initialize()
		self.traffic.start()

		while 1:
			for p in poisson:
				i = 0
				while i < p:
					v = BasicVehicle(self.traffic.paths[self.rand_generator.randint(1, len(self.traffic.paths))-1], \
						self.traffic, None)
					self.traffic.add(v)
					v.start()
					
					self.count += 1
					time.sleep(0.25)
					i += 1
				time.sleep(2)
			#v = BasicVehicle(self.traffic.paths[4], \
			#			self.traffic, None)
			#self.traffic.add(v)
			#v5 = BasicVehicle(self.traffic.paths[4], \
			#			self.traffic, None)
			#self.traffic.add(v5)
			#v6 = BasicVehicle(self.traffic.paths[4], \
			#			self.traffic, None)
			#self.traffic.add(v6)
			#v2 = BasicVehicle(self.traffic.paths[6], \
			#			self.traffic, None)
			#self.traffic.add(v2)
			#v3 = BasicVehicle(self.traffic.paths[6], \
			#			self.traffic, None)
			#self.traffic.add(v3)
			#v4 = BasicVehicle(self.traffic.paths[6], \
			#			self.traffic, None)
			#self.traffic.add(v4)
			#v.start()
			#time.sleep(0.25)
			#v5.start()
			#time.sleep(0.25)
			#v6.start()
			#time.sleep(0.25)
			#v2.start()
			#time.sleep(0.25)
			#v3.start()
			#time.sleep(0.25)
			#v4.start()
#
			#self.count += 6
			#time.sleep(5)




