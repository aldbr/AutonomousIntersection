from Vehicle import *

from abc import ABCMeta, abstractmethod

class DriveStrategy:
	__metaclass__=ABCMeta
	"""Drive strategy for vehicles"""

	@abstractmethod
	def drive(self, vehicle):
		pass