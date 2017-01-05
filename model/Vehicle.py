from abc import ABCMeta, abstractmethod
from threading import Thread

class Vehicle(Thread): 
	__metaclass__=ABCMeta
	"""Vehicle agent management"""

	def __init__(self, traficPath, speed):
		Thread.__init__(self)
		self.speed = speed
		self.traficPath = traficPath
		self.position = traficPath.positions[0]

	@abstractmethod
	def accelerate(self, speed):
		pass

	def slow_down(self, speed):
		pass
	
	@abstractmethod
	def run(self):
		pass


