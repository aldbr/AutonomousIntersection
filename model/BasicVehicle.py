from Vehicle import *
import time

class BasicVehicle(Vehicle):

	
	def __init__(self, traficPath):	
		Vehicle.__init__(self,traficPath, 10)
		pass


	def run(self):
		Vehicle.run(self)

	def accelerate(self, speed):
		pass

	def slow_down(self, speed):
		pass


	def rouler(self):
		i = 0
		length = len(self._traficPath.positions)
		while i < length :
			self._position = self._traficPath.positions[i]
			#i += 6 #30km/h
			i += self.speed #50km/h
			time.sleep(0.05)
		self._position = None


