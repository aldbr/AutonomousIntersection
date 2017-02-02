import sys
import os
CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
PARENT_FOLDER = os.path.dirname(CURRENT_FOLDER)
sys.path.append(PARENT_FOLDER)

from trafficFactory.TrafficPathFactory import *

from abc import ABCMeta, abstractmethod
from threading import Thread

class Traffic(Thread):
	__metaclass__=ABCMeta
	"""Traffic management"""

	def __init__(self, filename, trafficName):
		Thread.__init__(self)
		self.paths = []
		self.filename = filename
		self.trafficName = trafficName

	def initialize(self):
		self.paths = TrafficPathFactory.load_from_CSV_file(self.filename)


	@abstractmethod
	def __getitem__(self, index):
		pass

	@abstractmethod
	def __delitem__(self, index):
		pass

	@abstractmethod
	def run(self):
		pass
	
