from Vehicle import *

from abc import ABCMeta, abstractmethod

class DriveStrategy:
	__metaclass__=ABCMeta

	@abstractmethod
	def drive(self, vehicle):
		pass