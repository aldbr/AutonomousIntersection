from abc import ABCMeta, abstractmethod

class RoadSign: 
	__metaclass__=ABCMeta

	def __init__(self, position):
		self.position = position
