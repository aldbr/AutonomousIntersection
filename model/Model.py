from threading import Thread
import time
import numpy

from ClassicTrafficIntersection import *
from BasicVehicle import *

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
					v = BasicVehicle(self.traffic.paths[self.rand_generator.randint(1, len(self.traffic.paths))-1], self.traffic, None)
					self.traffic.add(v)
					v.start()
					
					self.count += 1
					time.sleep(0.25)
					i += 1
				time.sleep(1)


