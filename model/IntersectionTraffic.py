from Traffic import *

from abc import ABCMeta, abstractmethod


class IntersectionTraffic(Traffic):
	__metaclass__=ABCMeta
	"""Intersection agent management : subclass of Traffic"""

	def __init__(self, filename, trafficName):
		Traffic.__init__(self, filename, trafficName)


	@abstractmethod
	def __getitem__(self, index):
		pass

	@abstractmethod
	def __delitem__(self, index):
		pass
		
	@abstractmethod
	def run(self):
		pass