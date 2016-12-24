from Vehicle import *
import time

class BasicVehicle(Vehicle):

	
	def __init__(self, traficPath):	
		Vehicle.__init__(self,traficPath)
		pass


	def run(self):
		Vehicle.run(self)


	def rouler(self):
		for pos in self._traficPath.positions:
			self._position = pos
			time.sleep(0.05)
		self._position = None


