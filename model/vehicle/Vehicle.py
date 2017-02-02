from abc import ABCMeta, abstractmethod
from threading import Thread

class Vehicle(Thread): 
	__metaclass__=ABCMeta
	"""Vehicle agent management"""

	def __init__(self, traficPath, speed, next_vehicle):
		Thread.__init__(self)
		self.speed = speed
		self.acceleration = 0
		self.traficPath = traficPath
		self.position = traficPath.positions[0]
		self.next_vehicle = next_vehicle
		self.timeStart = 0

	@abstractmethod
	def accelerate(self, speed):
		pass

	def slow_down(self, speed):
		pass
	
	@abstractmethod
	def run(self):
		pass


