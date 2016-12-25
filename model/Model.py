from threading import Thread
import time
import random
import numpy

from IntersectionTraffic import *
from BasicVehicle import *

class Model(Thread): 

	def __init__(self):
		Thread.__init__(self)
		self.vehicles = []
		self.count = 0

	def run(self):
		numpy.random.seed(242)
		poisson = numpy.random.poisson(2, 100)

		t = IntersectionTraffic("ressources/intersectionPaths.csv")
		while 1:
			for p in poisson:
				i = 0
				while i < p:
					self.vehicles.append(BasicVehicle(t.paths[random.randint(1, len(t.paths))-1]))
					self.vehicles[self.count].start()
					self.count += 1
					time.sleep(0.25)
					i += 1
				time.sleep(1)




