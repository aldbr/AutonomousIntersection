from TrafficPathFactory import *

from abc import ABCMeta, abstractmethod
from threading import Thread

class Traffic(Thread):
	__metaclass__=ABCMeta
	"""Traffic management"""

	def __init__(self, filename):
		Thread.__init__(self)
		self.paths = TrafficPathFactory.load_from_CSV_file(filename)


	@abstractmethod
	def __getitem__(self, index):
		pass

	@abstractmethod
	def __delitem__(self, index):
		pass

	@abstractmethod
	def run(self):
		pass
	
