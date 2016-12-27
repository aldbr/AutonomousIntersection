from threading import Thread
import time
import random
import numpy

from ClassicTrafficIntersection import *
from BasicVehicle import *

class Model(Thread): 

	def __init__(self, traffic):
		Thread.__init__(self)
		self.vehicles = []
		self.count = 0
		self.traffic = traffic

	def run(self):
		numpy.random.seed(242)
		poisson = numpy.random.poisson(2, 100)

		self.traffic.start()
		while 1:
			for p in poisson:
				i = 0
				while i < p:
					#self.vehicles.append(BasicVehicle(self.traffic.paths[random.randint(1, len(self.traffic.paths))-1], self.traffic))
					#self.vehicles[self.count].start()
					v = BasicVehicle(self.traffic.paths[random.randint(1, len(self.traffic.paths))-1], self.traffic)
					self.traffic.add(v)
					v.start()
					
					self.count += 1
					time.sleep(0.25)
					i += 1
				time.sleep(1)




