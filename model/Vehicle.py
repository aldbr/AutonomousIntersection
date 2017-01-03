from abc import ABCMeta, abstractmethod
from threading import Thread

class Vehicle(Thread): 
	__metaclass__=ABCMeta
	"""Vehicle agent management"""

	def __init__(self, traficPath, speed):
		Thread.__init__(self)
		self._speed = speed
		self._traficPath = traficPath
		self._position = traficPath.positions[0]

	def _get_speed(self):
		return self._speed
	def _set_speed(self, speed):
		self._speed = speed
	speed = property(_get_speed, _set_speed)

	def _get_path(self):
		return self._traficPath
	def _set_path(self, traficPath):
		self._traficPath = traficPath
	traficPath = property(_get_path, _set_path)

	def _get_position(self):
		return self._position
	def _set_position(self, pos):
		self._position = pos
	position = property(_get_position, _set_position)

	@abstractmethod
	def accelerate(self, speed):
		pass

	def slow_down(self, speed):
		pass
	
	@abstractmethod
	def run(self):
		pass


